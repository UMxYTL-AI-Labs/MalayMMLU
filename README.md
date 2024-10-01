# MalayMMLU: A Multitask Benchmark for the Low-Resource Malay Language (Official site)

Released on September 27, 2024

<h4 align="center">
    <p>
        <b href="https://github.com/YTLAILabs/MalayMMLU/">English</b> |
        <a href="https://github.com/YTLAILabs/MalayMMLU/blob/main/README_ms.md">Bahasa Melayu</a> 
    <p>
        <p align="center" style="display: flex; flex-direction: row; justify-content: center; align-items: center">
        📄 <a href="https://openreview.net/pdf?id=VAXwQqkp5e" target="_blank" style="margin-right: 15px; margin-left: 10px">Paper</a> • 
        🤗 <a href="https://huggingface.co/datasets/UMxYTLAILabs/MalayMMLU" target="_blank" style="margin-left: 10px">Dataset</a> 
        </p>
</h4>

## Introduction

MalayMMLU is the first multitask language understanding (MLU) for Malay Language. The benchmark comprises 24,213 questions spanning both primary (Year 1-6) and secondary (Form 1-5) education levels in Malaysia, encompassing 5 broad topics that further divide into 22 subjects. 
<p align="center">
<img src="imgs/MalayMMLU.png"   width="250" >
</p>

| **Category**   | **Subjects**                                                                                                                                                                                                                                                                                                                                                                                 |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **STEM**       | Computer Science (Secondary), Biology (Secondary), Chemistry (Secondary), Computer Literacy (Secondary), Mathematics (Primary, Secondary), Additional Mathematics (Secondary), Design and Technology (Primary, Secondary), Core Science (Primary, Secondary), Information and Communication Technology (Primary), Automotive Technology (Secondary) |
| **Language**   | Malay Language (Primary, Secondary)                                                                                                                                                                                                                                                                                                                                                          |
| **Social science** | Geography (Secondary), Local Studies (Primary), History (Primary, Secondary)                                                                                                                                                                                                                                                                                                               |
| **Others**     | Life Skills (Primary, Secondary), Principles of Accounting (Secondary), Economics (Secondary), Business (Secondary), Agriculture (Secondary)                                                                                                                                                                                                                                                  |
| **Humanities** | Quran and Sunnah (Secondary), Islam (Primary, Secondary), Sports Science Knowledge (Secondary)                                                                                                                                                                                                                                                                                                 |

## Result

#### Zero-shot results of LLMs on MalayMMLU (First token accuracy)

<table>
    <thead>
        <tr>
            <th rowspan="2">Organization</th>
            <th rowspan="2">Model</th>
            <th rowspan="2">Vision</th>
            <th colspan="7">Acc.</th>
        </tr>
        <tr>
            <th>Language</th>
            <th>Humanities</th>
            <th>STEM</th>
            <th>Social Science</th>
            <th>Others</th>
            <th>Average</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td></td>
            <td>Random</td>
            <td></td>
            <td>38.01</td>
            <td>42.09</td>
            <td>36.31</td>
            <td>36.01</td>
            <td>38.07</td>
            <td>38.02</td>
        </tr>
        <tr>
            <td rowspan="4">OpenAI</td>
            <td>GPT-4o</td>
            <td style="color: green;">✔</td>
            <td><strong>87.12</strong></td>
            <td><strong>88.12</strong></td>
            <td><strong>83.83</strong></td>
            <td><strong>82.58</strong></td>
            <td><strong>83.09</strong></td>
            <td><strong>84.98</strong></td>
        </tr>
        <tr>
            <td>GPT-4</td>
            <td style="color: green;">✔</td>
            <td><ins>82.90</ins></td>
            <td><ins>83.91</ins></td>
            <td>78.80</td>
            <td><ins>77.29</ins></td>
            <td><ins>77.33</ins></td>
            <td><ins>80.11</ins></td>
        </tr>
        <tr>
            <td>GPT-4o mini</td>
            <td style="color: green;">✔</td>
            <td>82.03</td>
            <td>81.50</td>
            <td>78.51</td>
            <td>75.67</td>
            <td>76.30</td>
            <td>78.78</td>
        </tr>
        <tr>
            <td>GPT-3.5</td>
            <td></td>
            <td>69.62</td>
            <td>71.01</td>
            <td>67.17</td>
            <td>66.70</td>
            <td>63.73</td>
            <td>67.78</td>
        </tr>
        <tr>
            <td rowspan="7">Meta</td>
            <td>LLaMA-3.1 (70B)</td>
            <td></td>
            <td>78.75</td>
            <td>82.59</td>
            <td>78.96</td>
            <td>77.20</td>
            <td>75.32</td>
            <td>78.44</td>
        </tr>
        <tr>
            <td>LLaMA-3.1 (8B)</td>
            <td></td>
            <td>65.47</td>
            <td>67.17</td>
            <td>64.10</td>
            <td>62.59</td>
            <td>62.13</td>
            <td>64.24</td>
        </tr>
        <tr>
            <td>LLaMA-3 (8B)</td>
            <td></td>
            <td>63.93</td>
            <td>66.21</td>
            <td>62.26</td>
            <td>62.97</td>
            <td>61.38</td>
            <td>63.46</td>
        </tr>
        <tr>
            <td>LLaMA-2 (13B)</td>
            <td></td>
            <td>45.58</td>
            <td>50.72</td>
            <td>44.13</td>
            <td>44.55</td>
            <td>40.87</td>
            <td>45.26</td>
        </tr>
        <tr>
            <td>LLaMA-2 (7B)</td>
            <td></td>
            <td>47.47</td>
            <td>52.74</td>
            <td>48.71</td>
            <td>50.72</td>
            <td>48.19</td>
            <td>49.61</td>
        </tr>
        <tr>
            <td>LLaMA-3.2 (3B)</td>
            <td></td>
            <td>58.52</td>
            <td>60.66</td>
            <td>56.65</td>
            <td>54.06</td>
            <td>52.75</td>
            <td>56.45</td>
        </tr>
        <tr>
            <td>LLaMA-3.2 (1B)</td>
            <td></td>
            <td>38.88</td>
            <td>43.30</td>
            <td>40.65</td>
            <td>40.56</td>
            <td>39.55</td>
            <td>40.46</td>
        </tr>
        <tr>
            <td rowspan="8">Qwen (Alibaba)</td>
            <td>Qwen 2.5 (72B)</td>
            <td></td>
            <td>79.09</td>
            <td>79.95</td>
            <td><ins>80.88</ins></td>
            <td>75.80</td>
            <td>75.05</td>
            <td>77.79</td>
        </tr>
        <tr>
            <td>Qwen-2.5 (32B)</td>
            <td></td>
            <td>76.96</td>
            <td>76.70</td>
            <td>79.74</td>
            <td>72.35</td>
            <td>70.88</td>
            <td>74.83</td>
        </tr>
        <tr>
            <td>Qwen-2-VL (7B)</td>
            <td style="color: green;">✔</td>
            <td>68.16</td>
            <td>63.62</td>
            <td>67.58</td>
            <td>60.38</td>
            <td>59.08</td>
            <td>63.49</td>
        </tr>
        <tr>
            <td>Qwen-2-VL (2B)</td>
            <td style="color: green;">✔</td>
            <td>58.22</td>
            <td>55.56</td>
            <td>57.51</td>
            <td>53.67</td>
            <td>55.10</td>
            <td>55.83</td>
        </tr>
        <tr>
            <td>Qwen-1.5 (14B)</td>
            <td></td>
            <td>64.47</td>
            <td>60.64</td>
            <td>61.97</td>
            <td>57.66</td>
            <td>58.05</td>
            <td>60.47</td>
        </tr>
        <tr>
            <td>Qwen-1.5 (7B)</td>
            <td></td>
            <td>60.13</td>
            <td>59.14</td>
            <td>58.62</td>
            <td>54.26</td>
            <td>54.67</td>
            <td>57.18</td>
        </tr>
        <tr>
            <td>Qwen-1.5 (4B)</td>
            <td></td>
            <td>48.39</td>
            <td>52.01</td>
            <td>51.37</td>
            <td>50.00</td>
            <td>49.10</td>
            <td>49.93</td>
        </tr>
        <tr>
            <td>Qwen-1.5 (1.8B)</td>
            <td></td>
            <td>42.70</td>
            <td>43.37</td>
            <td>43.68</td>
            <td>43.12</td>
            <td>44.42</td>
            <td>43.34</td>
        </tr>
        <tr>
            <td rowspan="5">Zhipu</td>
            <td>GLM-4-Plus</td>
            <td></td>
            <td>78.04</td>
            <td>75.63</td>
            <td>77.49</td>
            <td>74.07</td>
            <td>72.66</td>
            <td>75.48</td>
        </tr>
        <tr>
            <td>GLM-4-Air</td>
            <td></td>
            <td>67.88</td>
            <td>69.56</td>
            <td>70.20</td>
            <td>66.06</td>
            <td>66.18</td>
            <td>67.60</td>
        </tr>
        <tr>
            <td>GLM-4-Flash</td>
            <td></td>
            <td>63.52</td>
            <td>65.69</td>
            <td>66.31</td>
            <td>63.21</td>
            <td>63.59</td>
            <td>64.12</td>
        </tr>
        <tr>
            <td>GLM-4</td>
            <td></td>
            <td>63.39</td>
            <td>56.72</td>
            <td>54.40</td>
            <td>57.24</td>
            <td>55.00</td>
            <td>58.07</td>
        </tr>
        <tr>
            <td>GLM-4<sup>††</sup> (9B)</td>
            <td></td>
            <td>58.51</td>
            <td>60.48</td>
            <td>56.32</td>
            <td>55.04</td>
            <td>53.97</td>
            <td>56.87</td>
        </tr>
        <tr>
            <td rowspan="3">Google</td>
            <td>Gemma-2 (9B)</td>
            <td></td>
            <td>75.83</td>
            <td>72.83</td>
            <td>75.07</td>
            <td>69.72</td>
            <td>70.33</td>
            <td>72.51</td>
        </tr>
        <tr>
            <td>Gemma (7B)</td>
            <td></td>
            <td>45.53</td>
            <td>50.92</td>
            <td>46.13</td>
            <td>47.33</td>
            <td>46.27</td>
            <td>47.21</td>
        </tr>
        <tr>
            <td>Gemma (2B)</td>
            <td></td>
            <td>46.50</td>
            <td>51.15</td>
            <td>49.20</td>
            <td>48.06</td>
            <td>48.79</td>
            <td>48.46</td>
        </tr>
        <tr>
            <td rowspan="2">SAIL (Sea)</td>
            <td>Sailor<sup>†</sup> (14B)</td>
            <td></td>
            <td>78.40</td>
            <td>72.88</td>
            <td>69.63</td>
            <td>69.47</td>
            <td>68.67</td>
            <td>72.29</td>
        </tr>
        <tr>
            <td>Sailor<sup>†</sup> (7B)</td>
            <td></td>
            <td>74.54</td>
            <td>68.62</td>
            <td>62.79</td>
            <td>64.69</td>
            <td>63.61</td>
            <td>67.58</td>
        </tr>
        <tr>
            <td>Cohere for AI</td>
            <td>Command R (32B)</td>
            <td></td>
            <td>71.68</td>
            <td>71.49</td>
            <td>66.68</td>
            <td>67.19</td>
            <td>63.64</td>
            <td>68.47</td>
        </tr>
        <tr>
            <td>OpenGVLab</td>
            <td>InternVL2 (40B)</td>
            <td style="color: green;">✔</td>
            <td>70.36</td>
            <td>68.49</td>
            <td>64.88</td>
            <td>65.93</td>
            <td>60.54</td>
            <td>66.51</td>
        </tr>
        <tr>
            <td>Damo (Alibaba)</td>
            <td>SeaLLM-v2.5<sup>†</sup> (7B)</td>
            <td></td>
            <td>69.75</td>
            <td>67.94</td>
            <td>65.29</td>
            <td>62.66</td>
            <td>63.61</td>
            <td>65.89</td>
        </tr>
        <tr>
            <td rowspan="4">Mistral</td>
            <td>Pixtral (12B)</td>
            <td style="color: green;">✔</td>
            <td>64.81</td>
            <td>62.68</td>
            <td>64.72</td>
            <td>63.93</td>
            <td>59.49</td>
            <td>63.25</td>
        </tr>
        <tr>
            <td>Mistral Small (22B)</td>
            <td></td>
            <td>65.19</td>
            <td>65.03</td>
            <td>63.36</td>
            <td>61.58</td>
            <td>59.99</td>
            <td>63.05</td>
        </tr>
        <tr>
            <td>Mistral-v0.3 (7B)</td>
            <td></td>
            <td>56.97</td>
            <td>59.29</td>
            <td>57.14</td>
            <td>58.28</td>
            <td>56.56</td>
            <td>57.71</td>
        </tr>
        <tr>
            <td>Mistral-v0.2 (7B)</td>
            <td></td>
            <td>56.23</td>
            <td>59.86</td>
            <td>57.10</td>
            <td>56.65</td>
            <td>55.22</td>
            <td>56.92</td>
        </tr>
        <tr>
            <td rowspan="2">Microsoft</td>
            <td>Phi-3 (14B)</td>
            <td></td>
            <td>60.07</td>
            <td>58.89</td>
            <td>60.91</td>
            <td>58.73</td>
            <td>55.24</td>
            <td>58.72</td>
        </tr>
        <tr>
            <td>Phi-3 (3.8B)</td>
            <td></td>
            <td>52.24</td>
            <td>55.52</td>
            <td>54.81</td>
            <td>53.70</td>
            <td>51.74</td>
            <td>53.43</td>
        </tr>
        <tr>
            <td>01.AI</td>
            <td>Yi-1.5 (9B)</td>
            <td></td>
            <td>56.20</td>
            <td>53.36</td>
            <td>57.47</td>
            <td>50.53</td>
            <td>49.75</td>
            <td>53.08</td>
        </tr>
        <tr>
            <td rowspan="2">Stability AI</td>
            <td>StableLM 2 (12B)</td>
            <td></td>
            <td>53.40</td>
            <td>54.84</td>
            <td>51.45</td>
            <td>51.79</td>
            <td>50.16</td>
            <td>52.45</td>
        </tr>
        <tr>
            <td>StableLM 2 (1.6B)</td>
            <td></td>
            <td>43.92</td>
            <td>51.10</td>
            <td>45.27</td>
            <td>46.14</td>
            <td>46.75</td>
            <td>46.48</td>
        </tr>
        <tr>
            <td>Baichuan</td>
            <td>Baichuan-2 (7B)</td>
            <td></td>
            <td>40.41</td>
            <td>47.35</td>
            <td>44.37</td>
            <td>46.33</td>
            <td>43.54</td>
            <td>44.30</td>
        </tr>
        <tr>
            <td>Mesolitica</td>
            <td>MaLLaM-v2<sup>†</sup> (5B)</td>
            <td></td>
            <td>42.57</td>
            <td>46.44</td>
            <td>42.24</td>
            <td>40.82</td>
            <td>38.74</td>
            <td>42.08</td>
        </tr>
        <tr>
            <td>Yellow.ai</td>
            <td>Komodo<sup>†</sup> (7B)</td>
            <td></td>
            <td>43.62</td>
            <td>45.53</td>
            <td>39.34</td>
            <td>39.75</td>
            <td>39.48</td>
            <td>41.72</td>
        </tr>
    </tbody>
</table>
Highest scores are <strong>bolded</strong> and second highest scores are <ins>underlined</ins>. 
† denotes LLMs fine-tuned with Southeast Asia datasets.
†† denotes open-source GLM-4.

#### Few-shot results of LLMs on MalayMMLU (First token accuracy)
<p align="center">
<img src="imgs/Few-shot%20comparison.png"   width="400" >
</p>

## Installation 

```
git clone https://github.com/UMxYTL-AI-Labs/MalayMMLU.git
cd MalayMMLU
pip install -r requirements.txt
```
## Evaluation

We provide example evaluation scripts in <code>scripts</code>

#### Evaluation by first token accuracy

* <code>SHOT</code> : Number of shots 0, 1, 2 or 3
* <code>--by_letter</code>:
    * Include this flag for first token accuracy calculation

* <code>MODEL</code>: LLM's HuggingFace repository name.
    * For example, <code>meta-llama/Meta-Llama-3-8B-Instruct</code>
* <code>PRED_FILE</code>: filename of prediction file
    * For example, <code>"output/MalayMMLU_result_Meta-Llama-3-8B-Instruct_True_0shot_useChatTrue.csv"</code>

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
#### Evaluation by full answer probability
```
python src/evaluate.py  --shot $SHOT --use_chat_template True  --task=MalayMMLU \
                    --base_model=$MODEL  \
                    --output_folder=output/ --token $TOKEN

python src/calculate_accuracies.py --pred_files $PRED_FILE \
    --data_file=$SHOT \
    --output_dir=output/

```

#### Evaluation for GPT

* <code>API_KEY</code>: OpenAI API key
```
# prediction
python src/evaluate_gpt.py --model gpt-3.5-turbo --api_key $API_KEY --shot $SHOT
```
* Download the prediction file (<code>jsonl</code> file ) from [OpenAI platform](https://platform.openai.com/batches)
* Rename the file in following format: <code>MalayMMLU_{$MODEL}_{$SHOT}shot.jsonl</code>
    * Example: <code>MalayMMLU_gpt3_0shot.jsonl</code>
```
# calculate accurcacy
python src/calculate_accuracies.py --pred_files $PRED_FILE \
    --data_file=$SHOT \
    --output_dir=output/
```

## Citation

```bibtex
@InProceedings{MalayMMLU2024,
    author    = {Poh, Soon Chang and Yang, Sze Jue and Tan, Jeraelyn Ming Li and  Chieng, Lawrence Leroy Tze Yao and Tan, Jia Xuan and Yu, Zhenyu and Foong, Chee Mun and Chan, Chee Seng},
    title     = {MalayMMLU: A Multitask Benchmark for the Low-Resource Malay Language},
    booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2024},
    month     = {November},
    year      = {2024},
}
```
## Feedback
Suggestions and opinions (both positive and negative) are greatly welcome. Please contact the author by sending email to `cs.chan at um.edu.my`.


## Acknowledgement

The code base is built upon [IndoMMLU](https://github.com/fajri91/IndoMMLU)
