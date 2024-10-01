#!/bin/bash -l

#SBATCH --partition=gpu-a100
#SBATCH --job-name=eval_mmlu
#SBATCH --output=logs/%x.out
#SBATCH --error=logs/%x.out
#SBATCH --nodes=1
#SBATCH --ntasks=16
#SBATCH --mem=250G
#SBATCH --qos=normal
#SBATCH --mail-type=ALL
#SBATCH --gpus=1


module load miniconda
source activate mmlu

TOKEN=<YOUR_HF_TOKEN>
SHOT=0

cd $HOME/MalayMMLU

## first token accuracy
python src/evaluate.py  --by_letter --shot $SHOT --task=MalayMMLU \
                    --base_model=meta-llama/Meta-Llama-3-8B-Instruct  \
                    --output_folder=output/ --token $TOKEN

python src/evaluate.py  --by_letter --shot $SHOT --task=MalayMMLU \
                    --base_model=meta-llama/Llama-2-13b-chat-hf  \
                    --output_folder=output/ --token $TOKEN


python src/evaluate.py  --by_letter --shot $SHOT --task=MalayMMLU \
                    --base_model=meta-llama/Llama-2-7b-chat-hf  \
                    --output_folder=output/ --token $TOKEN


python src/evaluate.py  --by_letter --shot $SHOT --task=MalayMMLU \
                    --base_model=mistralai/Mistral-7B-Instruct-v0.3  \
                    --output_folder=output/ --token $TOKEN

python src/evaluate.py  --by_letter --shot $SHOT --task=MalayMMLU \
                    --base_model=mistralai/Mistral-7B-Instruct-v0.2  \
                    --output_folder=output/ --token $TOKEN

python src/evaluate.py  --by_letter --shot $SHOT --task=MalayMMLU \
                    --base_model=sail/Sailor-7B-Chat \
                    --output_folder=output/ --token $TOKEN

python src/evaluate.py  --by_letter --shot $SHOT --task=MalayMMLU \
                    --base_model=SeaLLM-7B-v2.5  \
                    --output_folder=output/ --token $TOKEN

python src/evaluate.py  --by_letter --shot $SHOT --task=MalayMMLU \
                    --base_model=microsoft/Phi-3-medium-4k-instruct  \
                    --output_folder=output/ --token $TOKEN

python src/evaluate.py  --by_letter --shot $SHOT --task=MalayMMLU \
                    --base_model=microsoft/Phi-3-mini-4k-instruct \
                    --output_folder=output/ --token $TOKEN

python src/evaluate.py  --by_letter --shot $SHOT --task=MalayMMLU \
                    --base_model=Qwen/Qwen1.5-7B-Chat  \
                    --output_folder=output/ --token $TOKEN

python src/evaluate.py  --by_letter --shot $SHOT --task=MalayMMLU \
                    --base_model=Qwen/Qwen1.5-4B-Chat  \
                    --output_folder=output/ --token $TOKEN

python src/evaluate.py  --by_letter --shot $SHOT --task=MalayMMLU \
                    --base_model=Qwen/Qwen1.5-1.8B-Chat  \
                    --output_folder=output/ --token $TOKEN

python src/evaluate.py  --by_letter --shot $SHOT --task=MalayMMLU \
                    --base_model=google/gemma-7b-it  \
                    --output_folder=output/ --token $TOKEN

python src/evaluate.py  --by_letter --shot $SHOT --task=MalayMMLU \
                    --base_model=google/gemma-2b-it  \
                    --output_folder=output/ --token $TOKEN

python src/evaluate.py  --by_letter --shot $SHOT --task=MalayMMLU \
                    --base_model=Yellow-AI-NLP/komodo-7b-base  \
                    --output_folder=output/ --token $TOKEN

python src/evaluate.py  --by_letter --shot $SHOT --task=MalayMMLU \
                    --base_model=mesolitica/mallam-5b-20k-instructions-v2 \
                    --output_folder=output/ --token $TOKEN


python src/evaluate.py  --by_letter --shot $SHOT --task=MalayMMLU \
                    --base_model=mesolitica/mallam-5b-20k-instructions-v2 \
                    --output_folder=output/ --token $TOKEN

python src/evaluate.py  --by_letter --shot $SHOT --task=MalayMMLU \
                    --base_model=mesolitica/mallam-5b-20k-instructions-v2 \
                    --output_folder=output/ --token $TOKEN

# Qwen2-VL
python src/evaluate_qwen_vl.py  --by_letter --shot $SHOT --task=MalayMMLU \
                    --base_model=Qwen/Qwen2-VL-2B-Instruct \
                    --output_folder=output/ --token $TOKEN
# Pixtral
python src/evaluate_pixtral.py  --by_letter --shot $SHOT --task=MalayMMLU \
                    --base_model=mistral-community/pixtral-12b \
                    --output_folder=output/ --token $TOKEN
# InternVL2
python src/evaluate_intern_vl.py  --by_letter --shot $SHOT --task=MalayMMLU \
                    --base_model=OpenGVLab/InternVL2-40B \
                    --output_folder=output/ --token $TOKEN

python src/calculate_accuracies.py --all --pred_dir output/$SHOT/ \
		--shot $SHOT \
		--output_dir=results/$SHOT/


## full answer accuracy

python src/evaluate.py  --shot $SHOT --task=MalayMMLU \
                    --base_model=meta-llama/Meta-Llama-3-8B-Instruct  \
                    --output_folder=output/ --token $TOKEN

python src/evaluate.py  --shot $SHOT --task=MalayMMLU \
                    --base_model=meta-llama/Llama-2-13b-chat-hf  \
                    --output_folder=output/ --token $TOKEN


python src/evaluate.py  --shot $SHOT --task=MalayMMLU \
                    --base_model=meta-llama/Llama-2-7b-chat-hf  \
                    --output_folder=output/ --token $TOKEN


python src/evaluate.py  --shot $SHOT --task=MalayMMLU \
                    --base_model=mistralai/Mistral-7B-Instruct-v0.3  \
                    --output_folder=output/ --token $TOKEN

python src/evaluate.py  --shot $SHOT --task=MalayMMLU \
                    --base_model=mistralai/Mistral-7B-Instruct-v0.2  \
                    --output_folder=output/ --token $TOKEN

python src/evaluate.py  --shot $SHOT --task=MalayMMLU \
                    --base_model=sail/Sailor-7B-Chat \
                    --output_folder=output/ --token $TOKEN

python src/evaluate.py  --shot $SHOT --task=MalayMMLU \
                    --base_model=SeaLLM-7B-v2.5  \
                    --output_folder=output/ --token $TOKEN

python src/evaluate.py  --shot $SHOT --task=MalayMMLU \
                    --base_model=microsoft/Phi-3-medium-4k-instruct  \
                    --output_folder=output/ --token $TOKEN

python src/evaluate.py  --shot $SHOT --task=MalayMMLU \
                    --base_model=microsoft/Phi-3-mini-4k-instruct \
                    --output_folder=output/ --token $TOKEN

python src/evaluate.py  --shot $SHOT --task=MalayMMLU \
                    --base_model=Qwen/Qwen1.5-7B-Chat  \
                    --output_folder=output/ --token $TOKEN

python src/evaluate.py  --shot $SHOT --task=MalayMMLU \
                    --base_model=Qwen/Qwen1.5-4B-Chat  \
                    --output_folder=output/ --token $TOKEN

python src/evaluate.py  --shot $SHOT --task=MalayMMLU \
                    --base_model=Qwen/Qwen1.5-1.8B-Chat  \
                    --output_folder=output/ --token $TOKEN

python src/evaluate.py  --shot $SHOT --task=MalayMMLU \
                    --base_model=google/gemma-7b-it  \
                    --output_folder=output/ --token $TOKEN

python src/evaluate.py  --shot $SHOT --task=MalayMMLU \
                    --base_model=google/gemma-2b-it  \
                    --output_folder=output/ --token $TOKEN

python src/evaluate.py  --shot $SHOT --task=MalayMMLU \
                    --base_model=Yellow-AI-NLP/komodo-7b-base  \
                    --output_folder=output/ --token $TOKEN

python src/evaluate.py  --shot $SHOT --task=MalayMMLU \
                    --base_model=mesolitica/mallam-5b-20k-instructions-v2 \
                    --output_folder=output/ --token $TOKEN

# Qwen2-VL
python src/evaluate_qwen_vl.py --shot $SHOT --task=MalayMMLU \
                    --base_model=Qwen/Qwen2-VL-2B-Instruct \
                    --output_folder=output/ --token $TOKEN
# Pixtral
python src/evaluate_pixtral.py --shot $SHOT --task=MalayMMLU \
                    --base_model=mistral-community/pixtral-12b \
                    --output_folder=output/ --token $TOKEN
# InternVL2
python src/evaluate_intern_vl.py --shot $SHOT --task=MalayMMLU \
                    --base_model=OpenGVLab/InternVL2-40B \
                    --output_folder=output/ --token $TOKEN 

python src/calculate_accuracies.py --all --pred_dir output/$SHOT/ \
		--shot $SHOT \
		--output_dir=results/$SHOT/