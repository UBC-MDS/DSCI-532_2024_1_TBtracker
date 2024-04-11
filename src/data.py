import pandas as pd

# Load the preprocessed data once at the start to avoid reloading it on each callback.
preprocessed_rf_data = pd.read_csv("data/preprocessing/rf_type_data.csv")
rf_data = pd.read_csv("data/preprocessing/rf_data.csv")
tb_data = pd.read_csv("data/preprocessing/tb_data.csv")
