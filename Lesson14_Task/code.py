import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#VALUE COUNT - counts the frequency of each unique value in a dataset (how many times a value repeats)
dataset = pd.read_csv('/content/transaction_dataset.csv')
df = pd.DataFrame(dataset)

# Convert 'Gender' column to string to avoid float issues
dataset['Gender'] = dataset['Gender'].astype(str)

gender_data = dataset['Gender'].value_counts(dropna=False).reset_index() # resets index and outputs a usable DataFrame
gender_data.columns = ['Gender', 'Count']
plt.bar(gender_data['Gender'], gender_data['Count'], color=['thistle','skyblue', 'beige'], edgecolor='maroon')

plt.title('Customers per Gender') 
plt.xlabel('Gender')
plt.ylabel('Amount')

name_df = pd.DataFrame(dataset['Name'].value_counts().reset_index())
name_df.columns = ['Name', 'Counts']

filtered_names = name_df.iloc[:5]

plt.barh(filtered_names['Name'], filtered_names['Counts'], color='skyblue') 
plt.title('Top 5 names')
plt.ylabel('Names')
plt.xlabel('Frequency')

plt.show()

filtered_df = df[df['Gender'] == 'M'][df['Category'] == 'Clothing']
rows = len(filtered_df)
print(f'The filtered DataFrame has {rows} rows.')
