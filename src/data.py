import pandas as pd

# Load the preprocessed data once at the start to avoid reloading it on each callback.
preprocessed_rf_data = pd.read_parquet(
    "data/preprocessing/rf_type_data.parquet")
rf_data = pd.read_parquet("data/preprocessing/rf_data.parquet")
tb_data = pd.read_parquet("data/preprocessing/tb_data.parquet")
