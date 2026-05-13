import pandas as pd
import numpy as np

# ============================================
# STEP 1: LOAD DATASET
# ============================================
df = pd.read_csv('dirty_cafe_sales.csv')

print("="*60)
print("STEP 1: ORIGINAL DATASET INFO")
print("="*60)
print(f"Original shape: {df.shape}")
print(f"Original missing values: {df.isnull().sum().sum()}")

# ============================================
# STEP 2: STANDARDIZE COLUMN NAMES
# ============================================
df.columns = df.columns.str.lower().str.strip()
print(f"\nColumn names: {df.columns.tolist()}")

# ============================================
# STEP 3: IDENTIFY COLUMN TYPES
# ============================================
# Numeric columns (jo numbers hone chahiye)
numeric_cols = ['quantity', 'price_per_unit', 'total_spent']

# Categorical columns (jo text hone chahiye)
categorical_cols = ['item', 'payment_method', 'location']

# Transaction columns (date and ID)
transaction_cols = ['transaction_id', 'transaction_date']

# Filter only existing columns
existing_numeric = [col for col in numeric_cols if col in df.columns]
existing_cat = [col for col in categorical_cols if col in df.columns]

print(f"\nNumeric columns found: {existing_numeric}")
print(f"Categorical columns found: {existing_cat}")

# ============================================
# STEP 4: CLEAN NUMERIC COLUMNS
# ============================================
print("\n" + "="*60)
print("STEP 4: CLEANING NUMERIC COLUMNS")
print("="*60)

for col in existing_numeric:
    # Step 4a: Replace placeholder strings with NaN
    df[col] = df[col].replace(['UNKNOWN', 'ERROR', '', 'NULL', 'null'], np.nan)
    
    # Step 4b: Convert to numeric (invalid values become NaN)
    df[col] = pd.to_numeric(df[col], errors='coerce')
    
    # Step 4c: Check missing percentage
    missing_pct = df[col].isnull().mean() * 100
    print(f"{col}: {missing_pct:.1f}% missing")

# ============================================
# STEP 5: CLEAN CATEGORICAL COLUMNS
# ============================================
print("\n" + "="*60)
print("STEP 5: CLEANING CATEGORICAL COLUMNS")
print("="*60)

for col in existing_cat:
    # Step 5a: Remove whitespace
    df[col] = df[col].astype(str).str.strip()
    
    # Step 5b: Replace empty strings with NaN
    df[col] = df[col].replace(['', 'nan', 'NaN', 'NULL'], np.nan)
    
    # Step 5c: Check missing percentage
    missing_pct = df[col].isnull().mean() * 100
    print(f"{col}: {missing_pct:.1f}% missing")

# ============================================
# STEP 6: HANDLE DATES (if exists)
# ============================================
print("\n" + "="*60)
print("STEP 6: CLEANING DATE COLUMNS")
print("="*60)

for col in transaction_cols:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col], errors='coerce')
        missing_pct = df[col].isnull().mean() * 100
        print(f"{col}: {missing_pct:.1f}% missing")

# ============================================
# STEP 7: IMPUTATION - MEAN (For numeric)
# ============================================
print("\n" + "="*60)
print("STEP 7: MEAN IMPUTATION (Numeric Columns)")
print("="*60)

for col in existing_numeric:
    if df[col].isnull().sum() > 0:
        mean_val = df[col].mean()
        df[col] = df[col].fillna(mean_val)
        print(f"{col}: filled with mean = {mean_val:.2f}")

# ============================================
# STEP 8: IMPUTATION - MODE (For categorical)
# ============================================
print("\n" + "="*60)
print("STEP 8: MODE IMPUTATION (Categorical Columns)")
print("="*60)

for col in existing_cat:
    if df[col].isnull().sum() > 0:
        mode_val = df[col].mode()[0]
        df[col] = df[col].fillna(mode_val)
        print(f"{col}: filled with mode = '{mode_val}'")

# ============================================
# STEP 9: HANDLE DATE MISSING (if any)
# ============================================
print("\n" + "="*60)
print("STEP 9: HANDLING DATE MISSING")
print("="*60)

for col in transaction_cols:
    if col in df.columns and df[col].isnull().sum() > 0:
        # Fill with most common date or forward fill
        df[col] = df[col].fillna(method='ffill')
        print(f"{col}: filled with forward fill")

# ============================================
# STEP 10: FINAL VERIFICATION
# ============================================
print("\n" + "="*60)
print("STEP 10: FINAL VERIFICATION")
print("="*60)

remaining_missing = df.isnull().sum().sum()
print(f"Remaining missing values: {remaining_missing}")

if remaining_missing == 0:
    print("✅ DATASET IS COMPLETELY CLEAN! No missing values.")
else:
    print("⚠️ Some missing values remain. Check below:")
    print(df.isnull().sum()[df.isnull().sum() > 0])

# ============================================
# STEP 11: DATA TYPES AFTER CLEANING
# ============================================
print("\n" + "="*60)
print("STEP 11: DATA TYPES AFTER CLEANING")
print("="*60)
print(df.dtypes)

# ============================================
# STEP 12: SAVE CLEANED DATASET
# ============================================
df.to_csv('cafe_sales_cleaned.csv', index=False)
print("\n✅ Cleaned dataset saved as 'cafe_sales_cleaned.csv'")

# ============================================
# STEP 13: PREVIEW CLEANED DATA
# ============================================
print("\n" + "="*60)
print("STEP 12: PREVIEW OF CLEANED DATA")
print("="*60)
print(df.head(10))