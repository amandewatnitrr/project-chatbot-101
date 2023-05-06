import pandas as pd
import numpy as np
import statsmodels.api as sm

# Load data from CSV file
data = pd.read_csv("DATASET_LOCATION")

# Formula for the hierarchical GLM model
formula = "category ~ location + filename"

# Fit the model using the Poisson family and log link function
model = sm.GLM.from_formula(formula, data=data, family=sm.families.Poisson())

# Predict the category of a new file
new_file_location = "NEW_FILE_LOCATION"
new_file_name = "NEW_FILE_NAME"
new_file_data = {"location": new_file_location, "filename": new_file_name}
new_file_df = pd.DataFrame(new_file_data, index=[0])
predicted_category = model.predict(new_file_df)[0]

print("The predicted category of the file is:", predicted_category)
