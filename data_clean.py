# importing necessary libraries
import pandas as pd
import numpy as np

# loading the dataset
df = pd.read_csv(r"C:\Users\ANIK0101\Desktop\numpy\coding with sagar\employee_dataset\employee_data.csv")
print("Original Dataset Head:")
print(df.head())

# 1. First, convert infinite values to NaN so they don't corrupt the mean calculations
df.replace([np.inf, -np.inf], np.nan, inplace=True)

# 2. Fix negative salaries *before* filling NaNs, replacing them with NaN temporarily
df['Salary (INR)'] = np.where(df['Salary (INR)'] < 0, np.nan, df['Salary (INR)'])

# 3. Fill missing values column by column (Safe for Pandas 3.0+)
df['Salary (INR)'] = df["Salary (INR)"].fillna(df["Salary (INR)"].mean())
df['Performance Rating'] = df["Performance Rating"].fillna(df["Performance Rating"].median())
df['Experience (Years)'] = df["Experience (Years)"].fillna(df["Experience (Years)"].mean())


# 4. Remove duplicate records
df.drop_duplicates(inplace=True)

# 5. Outlier detection using 3 Standard Deviations
salary_mean = df['Salary (INR)'].mean()
salary_std = df['Salary (INR)'].std()
lower_bound = salary_mean - (3 * salary_std)
upper_bound = salary_mean + (3 * salary_std)

# Remove rows where salary is an outlier
df = df[(df['Salary (INR)'] >= lower_bound) & (df['Salary (INR)'] <= upper_bound)]

# Save the final cleaned data
df.to_csv('Cleaned_Employee_Data.csv', index=False)

print("\nData cleaning completed successfully!")
print("Saved as 'Cleaned_Employee_Data.csv'")
