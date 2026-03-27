import pandas as pd

# Load the dataset
df = pd.read_csv('dataset/legal_text_classification.csv')

print("✅ Loaded successfully!")
print("Shape:", df.shape)
print("\nColumns:", df.columns.tolist())

# See first 3 rows
print("\nFirst 3 rows:")
print(df.head(3))

# Count each outcome
print("\n📊 Case outcomes:")
print(df['case_outcome'].value_counts())

# Check for missing values
print("\n❓ Missing values:")
print(df.isnull().sum())

# Sample case text
print("\n📄 Sample case text:")
print(df['case_text'][0][:300])