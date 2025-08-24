import pandas as pd
import os
import json
import argparse

def calculate_accuracy(task,mmlu,filename,closed_flag, keep_idxs=None):
    if task == "MalayMMLU":
        if keep_idxs == None:
            if closed_flag:
                result = pd.read_json(filename, lines=True)
                correct_first = 0
                correct_full = 0
                for i in range(len(result)):
                    id = result.iloc[i].custom_id
                    ground_truth = mmlu[mmlu.id == id].iloc[0]
                    if result.iloc[i]['response']['body']['choices'][0]['message']['content'] != "":
                        if result.iloc[i]['response']['body']['choices'][0]['message']['content'][0] == ground_truth.key: #mmlu.iloc[i].key:
                            correct_first += 1
                        if result.iloc[i]['response']['body']['choices'][0]['message']['content'] == ground_truth.answer: #mmlu.iloc[i].answer:
                            correct_full += 1
                return correct_first/len(mmlu)*100, correct_full/len(mmlu)*100
            
            else: 
                
                result = pd.read_csv(filename)
                
                # Fixed filename parsing logic
                base_filename = os.path.basename(filename)
                # For filename with hyphens, like: MalayMMLU_result_Malaysian-Qwen2.5-14B-Reasoning-SFT_False_0shot.csv
                # We need to find the last two underscores to get by_letter and shot info
                parts = base_filename.split("_")
                by_letter = parts[-2]  # "False" part of the evaluation file name generated from evaluation
                shot_part = parts[-1].replace(".csv", "")  # "0shot"
                
                if by_letter == "True":
            
                    correct_org = 0
                    for i in range(len(result)):
                        if result.iloc[i].preds == mmlu.iloc[i].key:
                            correct_org += 1
    
                    return  correct_org/len(mmlu)*100
    
                elif by_letter == "False":
                    correct_org = 0
                    for i in range(len(result)):
    
                        if result.iloc[i].preds == result.iloc[i].golds:
                            correct_org += 1
    
                    return  correct_org/len(mmlu)*100

        else:
            if closed_flag: 
                print(filename)
                result = pd.read_json(filename, lines=True)
                correct_first = 0
                correct_full = 0
                for i in range(len(result)):
                    id = result.iloc[i].custom_id
          
                    ground_truth = mmlu[mmlu.id == id].iloc[0]
                    
                    if result.iloc[i]['response']['body']['choices'][0]['message']['content'] != "":
                        if result.iloc[i]['response']['body']['choices'][0]['message']['content'][0] == ground_truth.key  and result.iloc[i].name in keep_idxs: #mmlu.iloc[i].key:
                            correct_first += 1
                        if result.iloc[i]['response']['body']['choices'][0]['message']['content'] == ground_truth.answer and result.iloc[i].name in keep_idxs: #: #mmlu.iloc[i].answer:
                            correct_full += 1
                return correct_first/len(keep_idxs)*100, correct_full/len(keep_idxs)*100
            
            else: 
                
                result = pd.read_csv(filename)
                
                # Fixed filename parsing logic
                base_filename = os.path.basename(filename)
                parts = base_filename.split("_")
                by_letter = parts[-2]  # "False"
                
                if by_letter == "True":
            
                    correct_org = 0
                    for i in range(len(result)):
                        if result.iloc[i].preds == mmlu.iloc[i].key and result.iloc[i].name in keep_idxs:
                            correct_org += 1
    
                    return  correct_org/len(keep_idxs)*100
    
                elif by_letter == "False":
                    correct_org = 0
                    for i in range(len(result)):
    
                        if result.iloc[i].preds == result.iloc[i].golds and result.iloc[i].name in keep_idxs:
                            correct_org += 1
    
                    return  correct_org/len(keep_idxs)*100


def main(pred_files, shot, output_dir,closed_flag):
    os.makedirs(output_dir, exist_ok=True)
    mmlu = pd.read_json(f'data/MalayMMLU_{shot}shot.json')
    print("loaded data")
    
    

    for pred_file_str in pred_files:
        
        org_accs = []
        accs = []
        models = []
        shots = []
        by_letter = []
        categories = []
        
        for cat in mmlu.category.unique():
            keep_ids = list(mmlu[mmlu.category == cat].index)

            if closed_flag: 
                first_acc, full_acc = calculate_accuracy("MalayMMLU", mmlu, pred_file_str, closed_flag, keep_ids)
                # Fixed filename parsing
                base_filename = os.path.basename(pred_file_str)
                parts = base_filename.split("_")
                # Extract model name (everything between "result_" and the last two parts)
                model_name = "_".join(parts[2:-2])
                
                models += [model_name, model_name]
                shots += [parts[-1].replace(".csv", ""), parts[-1].replace(".csv", "")]
                by_letter += ["True", "False"]
                org_accs += [first_acc, full_acc]

                categories += [cat] * 2            
            else: 
                org_acc = calculate_accuracy("MalayMMLU", mmlu, pred_file_str,  closed_flag, keep_ids)
                org_accs.append(org_acc)
                
                # Fixed filename parsing
                base_filename = os.path.basename(pred_file_str)
                parts = base_filename.split("_")
                # Extract model name (everything between "result_" and the last two parts)
                model_name = "_".join(parts[2:-2])
                
                models.append(model_name)
                by_letter.append(parts[-2])  # "False"
                shots.append(parts[-1].replace(".csv", ""))  # "0shot"
                categories += [cat]


        if closed_flag: 
            for exp in ["first","full"]:
                # Append results for the current prediction file
                df = pd.DataFrame({
                    "Model": models,
                    "Accuracy": org_accs,
                    "shot": shots,
                    "by_letter": by_letter,
                    "category": categories
                })
                if exp == "first":
                    df = df[df.by_letter == "True"]
                elif exp == "full":
                    df = df[df.by_letter == "False"]
                print(df)
                category2amount = dict(mmlu.category.value_counts())
                print(category2amount)
                sum_acc = 0

                for category in category2amount.keys():
                    category_df = df[df.category == category]
                    if not category_df.empty:
                        sum_acc += category2amount[category] * category_df.iloc[0]['Accuracy'] 
                average_acc = sum_acc / len(mmlu)

                accuracy_info = {
                    'average accuracy': average_acc
                }
                for i in range(len(df)):
                    category = df.iloc[i].category
                    accuracy_info[f'accuracy for {category}'] = df.iloc[i].Accuracy

                model_name = df['Model'].iloc[0]
                
                shot = df['shot'].iloc[0]
                print("Model :", model_name)
                print("Metric :",exp)
                print("Shot :",shot)
                for k,v in accuracy_info.items():
                    print(k,v)

                output_file = os.path.join(output_dir, f"accuracy_info_{model_name}_{shot}_{exp}.json")
                
                with open(output_file, "w") as f:
                    json.dump(accuracy_info, f, indent=4)

        else:
            # Append results for the current prediction file
            df = pd.DataFrame({
                "Model": models,
                "Accuracy": org_accs,
                "shot": shots,
                "by_letter": by_letter,
                "category": categories
            })
            print(df)
            category2amount = dict(mmlu.category.value_counts())
            print(category2amount)
            sum_acc = 0

            for category in category2amount.keys():
                category_df = df[df.category == category]
                if not category_df.empty and category_df.iloc[0]['Accuracy'] is not None:
                    sum_acc += category2amount[category] * category_df.iloc[0]['Accuracy'] 
            average_acc = sum_acc / len(mmlu)

            accuracy_info = {
                'average accuracy': average_acc
            }
            for i in range(len(df)):
                category = df.iloc[i].category
                accuracy_info[f'accuracy for {category}'] = df.iloc[i].Accuracy

            model_name = df['Model'].iloc[0]
            exp = "first" if df['by_letter'].iloc[0] == "True" else "full"
            shot = df['shot'].iloc[0]
            print("Model :", model_name)
            print("Metric :",exp)
            print("Shot :",shot)
            for k,v in accuracy_info.items():
                print(k,v)

            output_file = os.path.join(output_dir, f"accuracy_info_{model_name}_{shot}_{exp}.json")
            
            with open(output_file, "w") as f:
                json.dump(accuracy_info, f, indent=4)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Calculate model prediction accuracy.')
    parser.add_argument('--pred_files', nargs='+', type=str,  help='List of prediction files. Example: "file1.csv"  "file2.csv"')
    parser.add_argument('--all', action='store_true', help="Flag for calculate accuracy for all prediction files in a directory")
    parser.add_argument('--closed', action='store_true', help="Flag for closed source model. The prediction file should have a suffix 'closed'")
    parser.add_argument('--pred_dir',type=str, help='Directory containing prediction files. Only provide when include --all flag')
    parser.add_argument('--shot', type=str, required=True, help='Provide the number of shots: 0,1,2 or 3')
    parser.add_argument('--output_dir', type=str, required=True, help='Directory to save the accuracy JSON file.')
    
    
    args = parser.parse_args()
    if args.all:
        pred_files = [ args.pred_dir +"/" + x for x in  os.listdir(args.pred_dir)]
        print(pred_files)
        main(pred_files, args.shot, args.output_dir, args.closed)

    else:
        main(args.pred_files, args.shot, args.output_dir, args.closed)