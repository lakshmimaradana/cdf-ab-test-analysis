# A/B Test Statistical Analysis Script
# Dataset: Kaggle A/B Testing Dataset
# Source: kaggle.com/datasets/zhangluyuan/ab-testing

import pandas as pd
import numpy as np
from scipy import stats

# Load data
df = pd.read_csv('ab_test_clean.csv')

# Remove mismatches
mismatch = df[((df['group'] == 'control') & 
               (df['landing_page'] == 'new_page')) |
              ((df['group'] == 'treatment') & 
               (df['landing_page'] == 'old_page'))]
df = df[~df.index.isin(mismatch.index)]

# Conversion rates
summary = df.groupby('group')['converted'].agg(
    total_users='count',
    total_conversions='sum',
    conversion_rate='mean'
).reset_index()
summary['conversion_rate'] = (summary['conversion_rate'] * 100).round(4)

control_rate = summary[summary['group'] == 'control']['conversion_rate'].values[0]
treatment_rate = summary[summary['group'] == 'treatment']['conversion_rate'].values[0]
lift = round(treatment_rate - control_rate, 4)
relative_lift = round((lift / control_rate) * 100, 2)

# Statistical test
control_data = df[df['group'] == 'control']['converted']
treatment_data = df[df['group'] == 'treatment']['converted']
t_stat, p_value = stats.ttest_ind(control_data, treatment_data)

# Confidence intervals
def confidence_interval(data, confidence=0.95):
    n = len(data)
    mean = data.mean()
    se = stats.sem(data)
    margin = se * stats.t.ppf((1 + confidence) / 2, n - 1)
    return mean, mean - margin, mean + margin

control_mean, control_lower, control_upper = confidence_interval(control_data)
treatment_mean, treatment_lower, treatment_upper = confidence_interval(treatment_data)

diff = treatment_mean - control_mean
diff_lower = diff - 1.96 * np.sqrt(
    (control_mean*(1-control_mean)/len(control_data)) +
    (treatment_mean*(1-treatment_mean)/len(treatment_data)))
diff_upper = diff + 1.96 * np.sqrt(
    (control_mean*(1-control_mean)/len(control_data)) +
    (treatment_mean*(1-treatment_mean)/len(treatment_data)))

# Print results
print("=" * 55)
print("   A/B TEST STATISTICAL ANALYSIS REPORT")
print("=" * 55)
print()
print("DATASET")
print(f"Source    : Kaggle A/B Testing Dataset")
print(f"Total rows: {len(df)}")
print()
print("CONVERSION RATES")
print(f"Control   : {control_rate}%")
print(f"Treatment : {treatment_rate}%")
print(f"Lift      : {lift}%")
print(f"Rel. Lift : {relative_lift}%")
print()
print("STATISTICAL TEST (T-Test)")
print(f"T-statistic : {t_stat:.4f}")
print(f"P-value     : {p_value:.4f}")
print()
print("CONFIDENCE INTERVALS (95%)")
print(f"Control   : ({control_lower*100:.4f}%, {control_upper*100:.4f}%)")
print(f"Treatment : ({treatment_lower*100:.4f}%, {treatment_upper*100:.4f}%)")
print(f"Difference: ({diff_lower*100:.4f}%, {diff_upper*100:.4f}%)")
print()
print("CONCLUSION")
if p_value < 0.05:
    print("STATISTICALLY SIGNIFICANT")
    if lift > 0:
        print("Recommendation: Switch to new page")
    else:
        print("Recommendation: Keep old page")
else:
    print("NOT STATISTICALLY SIGNIFICANT")
    print("Recommendation: Do not switch pages yet")
    print("Consider running the test longer")
print("=" * 55)