# A/B Test Analysis — Landing Page Optimization

## Business Question
Does the new landing page drive higher conversion 
rates than the existing page?

## Tools Used
- Python
- Pandas
- NumPy
- SciPy
- Matplotlib
- Seaborn
- Jupyter Notebook

## Dataset
- Name: Kaggle A/B Testing Dataset
- Source: kaggle.com/datasets/zhangluyuan/ab-testing
- Total rows: 294,478
- Clean rows: 290,585 (after removing 3,893 mismatches)

## Hypothesis
- H0: No difference in conversion rates between pages
- H1: New page has higher conversion rate

## Key Results
| Metric | Control (Old Page) | Treatment (New Page) |
|---|---|---|
| Total Users | 145,274 | 145,311 |
| Total Conversions | 17,489 | 17,264 |
| Conversion Rate | 12.04% | 11.88% |
| 95% CI | (11.87%, 12.21%) | (11.71%, 12.05%) |

## Statistical Test Results
- T-statistic : 1.3116
- P-value     : 0.1897
- Result      : NOT STATISTICALLY SIGNIFICANT

## Confidence Interval for Difference
- Difference  : -0.1579%
- 95% CI      : (-0.3939%, +0.0781%)
- CI crosses zero — confirms not significant

## Recommendation
Do not switch to the new landing page at this time.
The evidence does not support that the new page
drives meaningfully different conversion rates.

Next steps:
1. Run the test longer to gather more data
2. Test a more dramatically different page design
3. Segment results by device type and traffic source
4. Consider multivariate testing to isolate specific
   elements driving conversions

## Gist Link
https://gist.github.com/lakshmimaradana/851d53850ad918b5575042d990a244cb

## How to Run
1. Clone this repository
2. Install requirements:
   pip install pandas numpy scipy matplotlib seaborn
3. Open ab_test_analysis.ipynb in Jupyter Notebook
4. Run all cells
