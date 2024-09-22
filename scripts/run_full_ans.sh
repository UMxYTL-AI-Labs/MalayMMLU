TOKEN=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
SHOT=0

python src/evaluate.py  --shot $SHOT --use_chat_template True  --task=MalayMMLU \
                    --base_model=meta-llama/Meta-Llama-3-8B-Instruct  \
                    --output_folder=output/ --token $TOKEN

python src/evaluate.py  --shot $SHOT --use_chat_template True  --task=MalayMMLU \
                    --base_model=meta-llama/Llama-2-13b-chat-hf  \
                    --output_folder=output/ --token $TOKEN


python src/evaluate.py  --shot $SHOT --use_chat_template True  --task=MalayMMLU \
                    --base_model=meta-llama/Llama-2-7b-chat-hf  \
                    --output_folder=output/ --token $TOKEN


python src/evaluate.py  --shot $SHOT --use_chat_template True  --task=MalayMMLU \
                    --base_model=mistralai/Mistral-7B-Instruct-v0.3  \
                    --output_folder=output/ --token $TOKEN

python src/evaluate.py  --shot $SHOT --use_chat_template True  --task=MalayMMLU \
                    --base_model=mistralai/Mistral-7B-Instruct-v0.2  \
                    --output_folder=output/ --token $TOKEN

python src/evaluate.py  --shot $SHOT --use_chat_template True  --task=MalayMMLU \
                    --base_model=sail/Sailor-7B-Chat \
                    --output_folder=output/ --token $TOKEN

python src/evaluate.py  --shot $SHOT --use_chat_template True  --task=MalayMMLU \
                    --base_model=SeaLLM-7B-v2.5  \
                    --output_folder=output/ --token $TOKEN

python src/evaluate.py  --shot $SHOT --use_chat_template True  --task=MalayMMLU \
                    --base_model=microsoft/Phi-3-medium-4k-instruct  \
                    --output_folder=output/ --token $TOKEN

python src/evaluate.py  --shot $SHOT --use_chat_template True  --task=MalayMMLU \
                    --base_model=microsoft/Phi-3-mini-4k-instruct \
                    --output_folder=output/ --token $TOKEN

python src/evaluate.py  --shot $SHOT --use_chat_template True  --task=MalayMMLU \
                    --base_model=Qwen/Qwen1.5-7B-Chat  \
                    --output_folder=output/ --token $TOKEN

python src/evaluate.py  --shot $SHOT --use_chat_template True  --task=MalayMMLU \
                    --base_model=Qwen/Qwen1.5-4B-Chat  \
                    --output_folder=output/ --token $TOKEN

python src/evaluate.py  --shot $SHOT --use_chat_template True  --task=MalayMMLU \
                    --base_model=Qwen/Qwen1.5-1.8B-Chat  \
                    --output_folder=output/ --token $TOKEN

python src/evaluate.py  --shot $SHOT --use_chat_template True  --task=MalayMMLU \
                    --base_model=google/gemma-7b-it  \
                    --output_folder=output/ --token $TOKEN

python src/evaluate.py  --shot $SHOT --use_chat_template True  --task=MalayMMLU \
                    --base_model=google/gemma-2b-it  \
                    --output_folder=output/ --token $TOKEN

python src/evaluate.py  --shot $SHOT --use_chat_template True  --task=MalayMMLU \
                    --base_model=Yellow-AI-NLP/komodo-7b-base  \
                    --output_folder=output/ --token $TOKEN

python src/evaluate.py  --shot $SHOT --use_chat_template True  --task=MalayMMLU \
                    --base_model=mesolitica/mallam-5b-20k-instructions-v2 \
                    --output_folder=output/ --token $TOKEN