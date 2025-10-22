import whylogs as why
import pandas as pd
import os

# 1. Create a sample Pandas DataFrame
data = {
    "animal": ["cat", "dog", "cat", "dog", "cat", "dog", "pig"],
    "weight": [10.1, 20.2, 12.3, 25.4, 11.5, 22.6, 80.0],
    "legs": [4, 4, 4, 4, 4, 4, 4],
}
df = pd.DataFrame(data)

# 2. Run whylogs to generate a profile from the DataFrame
results = why.log(df)

# 3. Inspect the profile
# Get a "view" of the profile to access its contents
profile_view = results.view()

# Get a summary of the 'weight' column
weight_summary = profile_view.get_column("legs").to_summary_dict()
print("Summary for 'weight' column:")
print(weight_summary)
