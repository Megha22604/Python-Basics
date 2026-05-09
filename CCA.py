import pandas as pd

df = pd.read_csv('dirty_cafe_sales.csv')


cols_with_missing = [v for v in df.columns if df[v].isnull().sum() > 0]
print(f"Columns with missing values: {cols_with_missing}")


missing_percent = df.isnull().mean() * 100
print("\nMissing percentage in each column:")
print(missing_percent)


cols_to_keep = [v for v in df.columns if df[v].isnull().mean() < 0.5]
print(f"\nColumns with <50% missing: {cols_to_keep}")

#
clean_df = df[cols_to_keep].dropna()

print(f"\nOriginal rows: {len(df)}")
print(f"Rows after CCA: {len(clean_df)}")
print(f"Retained: {(len(clean_df)/len(df))*100:.1f}%")


print("\nMissing after cleaning:")
print(clean_df.isnull().mean() * 100)