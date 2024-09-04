# MalayMMLU

# Introduction

MalayMMLU is the first multitask language understanding (MLU) for Malay Language. The benchmark comprises 24,213 questions spanning both primary (Year 1-6) and secondaary (Form 1-5) education levels in Malaysia, encompassing 5 broad topics that further divide into 22 subjects. 

# Installation 

```
git clone https://github.com/YTLAILabs/MalayMMLU
cd MalayMMLU
pip install -r requirements.txt
```
# Quickstart

1. Evaluation by first token accuracy
```
python src/evaluate.py  --by_letter --shot $SHOT --use_chat_template True  --task=MalayMMLU \
                    --base_model=meta-llama/Meta-Llama-3-8B-Instruct  \
                    --output_folder=$HOME/MalayMMLU/output/ --token $TOKEN

```
2. Evaluation by full answer probability
```
python src/evaluate.py  --shot $SHOT --use_chat_template True  --task=MalayMMLU \
                    --base_model=meta-llama/Meta-Llama-3-8B-Instruct  \
                    --output_folder=$HOME/MalayMMLU/output/ --token $TOKEN

python calculate_accuracies.py --pred_files $PRED_FILE \
    --data_file=$SHOT \
    --output_dir=$HOME/MalayMMLU/output/

```

3. Evaluation for GPT

```
python src/evaluate_gpt.py --model gpt-3.5-turbo --api_key $API_KEY --shot $SHOT
```

# Acknowledgement

The code base is based on [IndoMMLU](https://github.com/fajri91/IndoMMLU)
