import pandas as pd
import geopandas as gpd

# Load the preprocessed data once at the start to avoid reloading it on each callback.
preprocessed_rf_data = pd.read_parquet(
    "data/processed/rf_type_data.parquet")
rf_data = pd.read_parquet("data/processed/rf_data.parquet")
tb_data = pd.read_parquet("data/processed/tb_data.parquet")
world_shp = gpd.read_file("data/processed/world.shp")
