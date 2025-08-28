# GPT-5-mini MalayMMLU Evaluation

## Overview
This contribution adds GPT-5-mini evaluation results to the MalayMMLU benchmark, achieving **84.93%** overall first token accuracy, ranking 3rd among all evaluated models.

## Results Summary
- **Model**: GPT-5-mini
- **Overall Accuracy**: 84.93%
- **Evaluation Method**: 0-shot, first token accuracy
- **Dataset Size**: 24,213 questions
- **Ranking**: 3/10 models

### Category-wise Performance
| Category | Accuracy |
|----------|----------|
| Humanities | 87.12% |
| Language | 86.32% |
| STEM | 86.29% |
| Others | 84.67% |
| Social Science | 81.93% |

### Level-wise Performance
| Level | Accuracy |
|-------|----------|
| Primary | 89.24% |
| Secondary | 82.74% |

## Files Added
1. `GPT5_Mini_MalayMMLU_Evaluation.ipynb` - Comprehensive evaluation notebook
2. `src/evaluate_gpt5_mini.py` - Evaluation script for GPT-5-mini
3. Updated `README.md` with results in leaderboard

## Methodology
- Used OpenAI Batch API for efficient evaluation
- Followed established MalayMMLU evaluation protocol
- First token accuracy measurement (industry standard)
- Full dataset evaluation (not sampled)

## Key Features of Evaluation
- Comprehensive error handling and validation
- Detailed results analysis and visualization
- Benchmark comparison with existing models
- Category and subject-level performance breakdown
- Production-ready evaluation framework

## Usage
To reproduce the evaluation:
```bash
python src/evaluate_gpt5_mini.py --api_key $OPENAI_API_KEY --shot 0
```

Or use the Jupyter notebook for interactive evaluation:
```bash
jupyter notebook GPT5_Mini_MalayMMLU_Evaluation.ipynb
```

## Impact
GPT-5-mini demonstrates strong performance across all categories, particularly excelling in:
- Humanities (87.12%) - highest among all categories
- Language (86.32%) - strong Malay language understanding
- STEM (86.29%) - competitive technical knowledge

The results show GPT-5-mini as a highly capable model for Malay language tasks, positioning between GPT-4o (84.98%) and GPT-4 (80.11%) in the leaderboard.
