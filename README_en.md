# MalayMMLU: A Multitask Benchmark for the Low-Resource Malay Language

<p align="center"> 
    <a href="#" target="_blank">Soon Chang Poh</a>, 
    <a href="#" target="_blank">Sze Jue Yang</a>, 
    <a href="#" target="_blank">Jeraelyn Ming Li Tan</a>, 
    <a href="#" target="_blank">Lawrence Leroy Tze Yao Chieng</a>, 
    <a href="#" target="_blank">Jia Xuan Tan</a>, 
    <a href="#" target="_blank">Zhenyu Yu</a>, 
    <a href="#" target="_blank">Chee Mun Foong</a>, 
    <a href="http://cs-chan.com/" target="_blank">Chee Seng Chan</a> 
</p>



# Introduction

MalayMMLU is the first multitask language understanding (MLU) for Malay Language. The benchmark comprises 24,213 questions spanning both primary (Year 1-6) and secondary (Form 1-5) education levels in Malaysia, encompassing 5 broad topics that further divide into 22 subjects. 
<p align="center">
<img src="imgs/MalayMMLU.png"   width="400" >
</p>

| **Category**   | **Subjects**                                                                                                                                                                                                                                                                                                                                                                                 |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **STEM**       | Computer Science (Secondary), Biology (Secondary), Chemistry (Secondary), Computer Literacy (Secondary), Mathematics (Primary, Secondary), Additional Mathematics (Secondary), Design and Technology (Primary, Secondary), Core Science (Primary, Secondary), Information and Communication Technology (Primary), Automotive Technology (Secondary) |
| **Language**   | Malay Language (Primary, Secondary)                                                                                                                                                                                                                                                                                                                                                          |
| **Social science** | Geography (Secondary), Local Studies (Primary), History (Primary, Secondary)                                                                                                                                                                                                                                                                                                               |
| **Others**     | Life Skills (Primary, Secondary), Principles of Accounting (Secondary), Economics (Secondary), Business (Secondary), Agriculture (Secondary)                                                                                                                                                                                                                                                  |
| **Humanities** | Quran and Sunnah (Secondary), Islam (Primary, Secondary), Sports Science Knowledge (Secondary)                                                                                                                                                                                                                                                                                                 |

# Result

### Zero-shot results of LLMs on MalayMMLU (First token accuracy)

| **Model**               | **Language** | **Humanities** | **STEM** | **Social Science** | **Others** | **Average** |
|-------------------------|-------------------|---------------------|---------------|-------------------------|-----------------|------------------|
| Random                  | 38.01             | 42.09               | 36.31         | 36.01                   | 38.07           | 38.02            |
| GPT-4                   | **82.90**         | **83.91**           | **78.80**     | **77.29**               | **77.33**       | **80.11**        |
| GPT-3.5                 | 69.62             | 71.01             | 67.17       | 66.70                 | 63.73         | 67.78          |
| LLaMA-3 (8B)            | 63.93             | 66.21               | 62.26         | 62.97                   | 61.38           | 63.46            |
| LLaMA-2 (13B)           | 45.58             | 50.72               | 44.13         | 44.55                   | 40.87           | 45.26            |
| LLaMA-2 (7B)            | 47.47             | 52.74               | 48.71         | 50.72                   | 48.19           | 49.61            |
| Mistral-v0.3 (7B)       | 56.97             | 59.29               | 57.14         | 58.28                   | 56.56           | 57.71            |
| Mistral-v0.2 (7B)       | 56.23             | 59.86               | 57.10         | 56.65                   | 55.22           | 56.92            |
| Sailor (7B)   | 74.54           | 68.62               | 62.79         | 64.69                   | 63.61           | 67.58            |
| SeaLLM-v2.5 (7B)   | 69.75             | 67.94               | 65.29         | 62.66                   | 63.61           | 65.89            |
| Phi-3 (14B)             | 60.07             | 58.89               | 60.91         | 58.73                   | 55.24           | 58.72            |
| Phi-3 (3.8B)            | 52.24             | 55.52               | 54.81         | 53.70                   | 51.74           | 53.43            |
| GLM-4 (9B)              | 58.51             | 60.48               | 56.32         | 55.04                   | 53.97           | 56.87            |
| Qwen-1.5 (7B)           | 60.13             | 59.14               | 58.62         | 54.26                   | 54.67           | 57.18            |
| Qwen-1.5 (4B)           | 48.39             | 52.01               | 51.37         | 50.00                   | 49.10           | 49.93            |
| Qwen-1.5 (1.8B)         | 42.70             | 43.37               | 43.68         | 43.12                   | 44.42           | 43.34            |
| Gemma (7B)              | 45.53             | 50.92               | 46.13         | 47.33                   | 46.27           | 47.21            |
| Gemma (2B)              | 46.50             | 51.15               | 49.20         | 48.06                   | 48.79           | 48.46            |
| Baichuan-2 (7B)         | 40.41             | 47.35               | 44.37         | 46.33                   | 43.54           | 44.30            |
| Komodo (7B)   | 43.62             | 45.53               | 39.34         | 39.75                   | 39.48           | 41.72            |
| MaLLaM-v2(5B)| 42.56             | 46.42               | 42.16         | 40.81                   | 38.81           | 42.07            |

### Few-shot results of LLMs on MalayMMLU (First token accuracy)
<p align="center">
<img src="imgs/Few-shot%20comparison.png"   width="400" >
</p>

# Installation 

```
git clone https://github.com/YTLAILabs/MalayMMLU
cd MalayMMLU
pip install -r requirements.txt
```
# Evaluation
* <code>SHOT</code> : 0, 1, 2 or 3
* <code>--by_letter</code> flag for first token evaluation
* <code>MODEL</code>: LLM's HuggingFace repo id such as <code>meta-llama/Meta-Llama-3-8B-Instruct</code>
* <code>PRED_FILE</code>: filename of prediction file
### Evaluation by first token accuracy

```
# prediction
python src/evaluate.py  --by_letter --shot $SHOT --use_chat_template True  --task=MalayMMLU \
                    --base_model=$MODEL  \
                    --output_folder=output/ --token $TOKEN

# calculate accuracy
python src/calculate_accuracies.py --pred_files $PRED_FILE \
    --data_file=$SHOT \
    --output_dir=output/
```
### Evaluation by full answer probability
```
python src/evaluate.py  --shot $SHOT --use_chat_template True  --task=MalayMMLU \
                    --base_model=$MODEL  \
                    --output_folder=output/ --token $TOKEN

python src/calculate_accuracies.py --pred_files $PRED_FILE \
    --data_file=$SHOT \
    --output_dir=output/

```

### Evaluation for GPT

* <code>API_KEY</code>: OpenAI API key
```
# prediction
python src/evaluate_gpt.py --model gpt-3.5-turbo --api_key $API_KEY --shot $SHOT
```
Download the prediction file from [OpenAI platform](https://platform.openai.com/batches)
```
# calculate accurcacy
python src/calculate_accuracies.py --pred_files $PRED_FILE \
    --data_file=$SHOT \
    --output_dir=output/
```

## Citation

```bibtex
@InProceedings{
    author = {Poh, Soon Chang and Yang, Sze Jue and Tan, Jeraelyn Ming Li and  Chieng, Lawrence Leroy Tze Yao and Tan, Jia Xuan and Yu, Zhenyu and Foong, Chee Mun and Chan, Chee Seng }
    title     = {MalayMMLU: A Multitask Benchmark for
the Low-Resource Malay Language},
    year      = {2024},
}
```
# Acknowledgement

The code base is based on [IndoMMLU](https://github.com/fajri91/IndoMMLU)
