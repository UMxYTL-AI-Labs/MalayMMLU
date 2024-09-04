import argparse
import pandas as pd
import os
from transformers import LlamaForCausalLM, LlamaTokenizer, AutoTokenizer, AutoModelForCausalLM
from tqdm import tqdm
from numpy import argmax
import torch
from utils import predict_classification_causal as predict_classification
from utils import predict_classification_causal_by_letter as predict_classification_by_letter

device = "cuda"
# usage: python evaluate.py  --by_letter --shot 0 --use_chat_template True  --task=MalayMMLU --base_model=google/gemma-2b-it --output_folder=$HOME/MalayMMLU/output/  --token $TOKEN

def prepare_data(playground,use_chat_template,model_name, tokenizer,task):
    if task=="MalayMMLU":
        inputs = []
        outputs = []
        outputs_options = []
        key2id = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}
        shot = 0
        data = pd.read_json(f'data/MalayMMLU_{shot}shot.json')
        if playground:
            data = data.iloc[:10]
        for idx, row in data.iterrows():
            ques =  data.iloc[idx]['prompt']

            if use_chat_template:
                if "llama" in model_name.lower():

                    p = f"Berikut adalah soalan aneka pilihan tentang {row['subject']}. Sila berikan jawapan sahaja.\n\n" + ques
                    chat = [{"role": "user", "content": p}]
                    chat = tokenizer.apply_chat_template(chat, tokenize=False, add_generation_prompt=True) + "\nJawapan:"

                else:
                    p = f"Berikut adalah soalan aneka pilihan tentang {row['subject']}. Sila berikan jawapan sahaja.\n\n" + ques + "\nJawapan:" 
                    chat = [{"role": "user", "content": p}]
                    chat = tokenizer.apply_chat_template(chat, tokenize=False, add_generation_prompt=True)                   
                inputs.append(chat)
            else:
                inputs.append(ques + "\nJawapan:")
            idx_label = key2id[row['key']]
            outputs.append(idx_label)
            outputs_options.append(row['options'])
        return inputs, outputs, outputs_options

def prepare_data_few_shot(shot,use_chat_template, model_name, tokenizer,task):
    if task == "MalayMMLU":
        inputs = []
        outputs = []
        outputs_options = []
        key2id = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}
        data = pd.read_json(f'data/MalayMMLU_{shot}shot.json')

        for i in range(len(data)):
            row = data.iloc[i]
            
            if use_chat_template:
                
                if "llama" in model_name.lower():
                    p = data.iloc[i][f'full_question_{shot}shot_llama']
                    chat = [{"role": "user", "content": p}]
                    chat = tokenizer.apply_chat_template(chat, tokenize=False, add_generation_prompt=True) +"Jawapan:"
                else:
                    p = data.iloc[i][f'full_question_{shot}shot']
                    chat = [{"role": "user", "content": p}]
                    chat = tokenizer.apply_chat_template(chat, tokenize=False, add_generation_prompt=True)
                inputs.append(chat)
            else:
                inputs.append(data.iloc[i][f'full_question_{shot}shot'])
            idx_label = key2id[row['key']]
            outputs.append(idx_label)
            outputs_options.append(row['options'])
        return inputs, outputs, outputs_options
            
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--by_letter", action='store_true')
    parser.add_argument("--base_model", type=str, help="Path to pretrained model", required=True)
    parser.add_argument("--output_folder", type=str, default="output", required=True)
    parser.add_argument("--playground", type=bool,default=False)
    parser.add_argument("--task",type=str, default="MalayMMLU")
    parser.add_argument("--shot",type=int, default=0)
    parser.add_argument("--use_chat_template",type=bool, default=False)
    parser.add_argument("--token",type=str)
    args = parser.parse_args()
    return args


def main():
    args = parse_args()

    os.makedirs(args.output_folder, exist_ok=True)
        
    tokenizer_class = LlamaTokenizer if ('llama' in args.base_model and ("Llama-3" not in args.base_model and "Llama-2" not in args.base_model)) else AutoTokenizer
    model_class = LlamaForCausalLM if ('llama' in args.base_model and ("Llama-3" not in args.base_model and "Llama-2" not in args.base_model)) else AutoModelForCausalLM

    SAVE_FILE = f'{args.output_folder}/{args.task}_result_{args.base_model.split("/")[-1]}_{args.by_letter}_{args.shot}shot_useChat{args.use_chat_template}.csv'

    tokenizer = tokenizer_class.from_pretrained(args.base_model,token=args.token,trust_remote_code=True)
    

    model = model_class.from_pretrained(args.base_model, token=args.token, torch_dtype=torch.float16, trust_remote_code=True, device_map= "cuda")

    

    model.eval()

    print(args.task)
    
    playground = args.playground # Enable testing of code with only 10 examples of questions
    if args.shot == 0:
        inputs, golds, outputs_options = prepare_data(playground, args.use_chat_template,args.base_model, tokenizer,args.task)
        print(inputs[0])
    else:
        inputs, golds, outputs_options = prepare_data_few_shot(args.shot,args.use_chat_template,args.base_model, tokenizer,args.task)
        print(inputs[0])
    preds = []
    probs = []
    for idx in tqdm(range(len(inputs))):
        if not args.by_letter: # full answer probability
            out = predict_classification(model, tokenizer, inputs[idx], outputs_options[idx], device)
            prob = [o.cpu().detach().item() for o in out]
            # Obtain full answer probability for each option. 
            # Example: P(question + options + A. cat) , P(question + options + B. dog) etc
            # The prediction would be the index with the highest probability 
            pred = argmax(prob)
            preds.append(pred)
            probs.append(prob)
        else: # first token probability
            conf, pred = predict_classification_by_letter(model, tokenizer, inputs[idx], outputs_options[idx], device)
            probs.append(conf)
            preds.append(pred)

    output_df = pd.DataFrame()
    output_df['input'] = inputs
    output_df['golds'] = golds
    output_df['options'] = outputs_options
    output_df['preds'] = preds
    output_df['probs'] = probs
    print(output_df.iloc[0])
    output_df.to_csv(SAVE_FILE, index=False)

if __name__ == "__main__":
    main()
