import pandas as pd
import statsmodels.api as sm

# Load the data from CSV file
data = pd.read_csv('data.csv')

# Preprocessing data
data['category'] = data['category'].astype('category')
data['location'] = data['location'].astype('category')

# One-hot encode categorical variables
encoded_data = pd.get_dummies(data, columns=['location'])

# Encoding ordinal variables
encoded_data['file_name'] = encoded_data['file_name'].astype('category')
encoded_data['file_name'] = encoded_data['file_name'].cat.codes

# Fitting  HGLM model
model = sm.GLM.from_formula(
    'category ~ file_name + location',
    data=encoded_data,
    family=sm.families.Binomial(),
    groups=encoded_data['location'].cat.codes
)
result = model.fit()

# Print the summary of the model
print(result.summary())
