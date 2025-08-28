import argparse
import pandas as pd
import json
from openai import OpenAI

# usage: python evaluate_gpt5_mini.py --api_key $API_KEY --shot 0
def main(api_key, shot):
    client = OpenAI(api_key=api_key)
    inputs = []
    outputs = []
    outputs_options = []
    key2id = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}
    
    data = pd.read_json(f'data/MalayMMLU_{shot}shot.json')
    print(f"Loaded {len(data)} questions for {shot}-shot evaluation")

    if shot == 0:
        for idx, row in data.iterrows():
            ques = row['prompt']
            p = f"Berikut adalah soalan aneka pilihan tentang {row['subject']}. Sila berikan jawapan sahaja.\n\n" + ques + "\nJawapan:" 
            inputs.append(p)
        
            idx_label = key2id[row['key']]
            outputs.append(idx_label)
            outputs_options.append(row['options'])
    else:
        for idx, row in data.iterrows():
            ques = data.iloc[idx][f'full_question_{shot}shot']
            inputs.append(ques)

            idx_label = key2id[row['key']]
            outputs.append(idx_label)
            outputs_options.append(row['options'])

    print("Sample input:")
    print(inputs[0])
    
    # Create batch requests for GPT-5-mini
    batch_requests = [
        {
            "custom_id": str(data.iloc[i].id),
            "method": "POST",
            "url": "/v1/chat/completions",
            "body": {
                "model": "gpt-5-mini",
                "messages": [{"role": "user", "content": inputs[i]}]
            }
        } for i in range(len(inputs))
    ]
    
    # Save batch requests to JSONL file
    batch_file_path = f'MalayMMLU_gpt5_mini_{shot}shot_batch.jsonl'
    with open(batch_file_path, 'w', encoding='utf-8') as f:
        for request in batch_requests:
            f.write(json.dumps(request) + '\n')
    
    print(f"Batch requests saved to: {batch_file_path}")
    
    # Upload batch file and create batch
    try:
        with open(batch_file_path, 'rb') as file:
            batch_input_file = client.files.create(file=file, purpose="batch")
        
        batch = client.batches.create(
            input_file_id=batch_input_file.id,
            endpoint="/v1/chat/completions",
            completion_window="24h",
            metadata={
                "description": f"MalayMMLU GPT-5-mini {shot}-shot evaluation"
            }
        )
        
        print(f"Batch created successfully!")
        print(f"Batch ID: {batch.id}")
        print(f"Status: {batch.status}")
        print(f"Please monitor the batch status and download results when completed.")
        print(f"Use this batch ID to check status: {batch.id}")
        
    except Exception as e:
        print(f"Error creating batch: {e}")
        print(f"You can manually upload the file {batch_file_path} to OpenAI platform")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--api_key", type=str, required=True, help="OpenAI API key")
    parser.add_argument("--shot", type=int, default=0, help="Number of shots (0, 1, 2, or 3)")
    
    args = parser.parse_args()
    main(args.api_key, args.shot)
