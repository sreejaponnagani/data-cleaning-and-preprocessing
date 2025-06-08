import pandas as pd

# Load dataset
df = pd.read_csv("C:\\Users\\Sreej\\OneDrive\\Desktop\\elevate labs internship\\DATA ANALYST\\TASK 1\\appointments.csv")

# View columns
print("Original Columns:", df.columns)

# Check for missing values
print("Missing values:\n", df.isnull().sum())

# Fill missing values (forward fill)
df.ffill(inplace=True)  # or df.dropna(inplace=True) if you prefer to remove rows

# Check and drop duplicates
print("Duplicate rows before dropping:", df.duplicated().sum())
df.drop_duplicates(inplace=True)

# Standardize 'Gender' column
df['Gender'] = df['Gender'].str.lower().str.strip()

# Convert date columns to datetime format
df['ScheduledDay'] = pd.to_datetime(df['ScheduledDay'], errors='coerce')
df['AppointmentDay'] = pd.to_datetime(df['AppointmentDay'], errors='coerce')

# Clean column names: lowercase, replace spaces with underscores
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Convert age to integer (if not already)
df['age'] = pd.to_numeric(df['age'], errors='coerce').astype('Int64')

# Save the cleaned dataset
df.to_csv("C:\\Users\\Sreej\\OneDrive\\Desktop\\elevate labs internship\\DATA ANALYST\\TASK 1\\cleaned_dataset.csv", index=False)

# Summary
print("✅ Data cleaned successfully and saved as cleaned_dataset.csv")
print("✅ Cleaned Columns:", df.columns)
