import argparse
import pandas as pd
from zhipuai import ZhipuAI

# usage python evaluate_glm.py --model gpt-3.5-turbo --api_key $API_KEY --shot 0

def main(api_key, model,shot):
    client = ZhipuAI(api_key=api_key)
    inputs = []
    outputs = []
    outputs_options = []
    key2id = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}
    
    data = pd.read_json(f'data/MalayMMLU_{shot}shot.json')
    print(data)

    if shot == 0:
        for idx,row in data.iterrows():
            ques = row['prompt']
            p = f"Berikut adalah soalan aneka pilihan tentang {row['subject']}. Sila berikan jawapan sahaja.\n\n" + ques + "\nJawapan:" 
            inputs.append(p)
        
            idx_label = key2id[row['key']]
            outputs.append(idx_label)
            outputs_options.append(row['options'])
    else:
        for idx, row in data.iterrows():
            ques =  data.iloc[idx][f'full_question_{shot}shot']
                
            inputs.append(ques)

            idx_label = key2id[row['key']]
            outputs.append(idx_label)
            outputs_options.append(row['options'])
    

    print(inputs[0])
    batch_requests = [
        {
            "custom_id": str(data.iloc[i].id),
            "method": "POST",
            "url": "/v4/chat/completions",
            "body": {
                "model": model,
                "messages": [{"role": "user", "content": inputs[i]}],
                "max_tokens": 50
            }
        } for i in range(len(inputs))
    ]
    
    batch_df = pd.DataFrame(batch_requests)
    batch_df.to_json(f"MalayMMLU-{shot}shot_{model}_batch_requests.jsonl", lines=True, orient="records")
    
    batch_input_file = client.files.create(
        file=open(f"MalayMMLU-{shot}shot_{model}_batch_requests.jsonl", "rb"),
        purpose="batch"
    )
    
    batch_input_file_id = batch_input_file.id
    
    client.batches.create(
        input_file_id=batch_input_file_id,
        endpoint="/v4/chat/completions",
        completion_window="24h",
        metadata={
            "description": f"MalayMMLU-0shot_{model}"
        }
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Benchmarking MalayMMLU on Zhipu's GLM models")
    parser.add_argument("--model",required=True, type=str, help="Model name of the GLM model. Example: glm-4-plus", default="glm-4-plus")
    parser.add_argument("--api_key", required=True, help="Zhipu API Key")
    parser.add_argument("--shot",
                        type=int, 
                        default=0,
                        help="Provide the number of shots: 0,1,2 or 3")
    args = parser.parse_args()
    main(api_key=args.api_key,model=args.model, shot=args.shot)