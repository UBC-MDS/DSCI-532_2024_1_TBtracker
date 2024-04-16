import pandas as pd

# Load your data
tb_data = pd.read_csv("data/raw/TB_burden_countries_2024-03-26.csv")

# Initial preprocessing of the TB data
tb_data_preprocess = tb_data[
    [
        "country", "iso2", "iso3", "iso_numeric", "year", "e_pop_num",
        "e_inc_num", "e_inc_num_hi", "e_inc_num_lo", "e_inc_tbhiv_num",
        "e_inc_tbhiv_num_hi", "e_inc_tbhiv_num_lo", "e_mort_exc_tbhiv_num",
        "e_mort_exc_tbhiv_num_hi", "e_mort_exc_tbhiv_num_lo", "e_mort_tbhiv_num",
        "e_mort_tbhiv_num_hi", "e_mort_tbhiv_num_lo", "cfr", "cfr_hi", "cfr_lo"
    ]
].copy()

# Convert columns to string to ensure correct data types
for col in ['country', 'iso2', 'iso3']:
    tb_data_preprocess[col] = tb_data_preprocess[col].astype(str)

# Calculate additional metrics
tb_data_preprocess["incidence_total"] = tb_data_preprocess["e_inc_num"] + tb_data_preprocess["e_inc_num_hi"]
tb_data_preprocess["incidence_rate"] = tb_data_preprocess["incidence_total"] / tb_data_preprocess["e_pop_num"]
tb_data_preprocess["mortality_total"] = tb_data_preprocess["e_mort_exc_tbhiv_num"] + tb_data_preprocess["e_mort_tbhiv_num"]
tb_data_preprocess["mortality_rate"] = tb_data_preprocess["mortality_total"] / tb_data_preprocess["e_pop_num"]
tb_data_preprocess["cfr_total"] = tb_data_preprocess["cfr"]
tb_data_preprocess["tbhiv_coinfection_total"] = tb_data_preprocess["e_inc_tbhiv_num"] + tb_data_preprocess["e_inc_tbhiv_num_hi"]
tb_data_preprocess["tbhiv_coinfection_rate"] = tb_data_preprocess["tbhiv_coinfection_total"] / tb_data_preprocess["e_pop_num"]

# Handling missing and filling values
tb_data_preprocess["iso_numeric"] = tb_data_preprocess.groupby("country")["iso_numeric"].transform(lambda x: x.fillna(x.max()))
tb_data_preprocess.fillna(-1, inplace=True)

# Save to Parquet
try:
    tb_data_preprocess.to_parquet("data/preprocessing/tb_data.parquet", index=False)
    print("Data saved successfully to Parquet.")
except Exception as e:
    print("Failed to save data to Parquet:", e)

# Repeat the conversion and check for other datasets if necessary
try:
    rf_data = pd.read_csv("data/raw/TB_burden_age_sex_2024-03-26.csv")
    rf_data_preprocess = rf_data[(rf_data["sex"] != "a") & (rf_data["age_group"] != "all")].copy()
    rf_data_preprocess = rf_data_preprocess[~rf_data_preprocess["age_group"].isin(["0-14", "15plus", "18plus"])]
    rf_data_preprocess["age_group"] = pd.Categorical(rf_data_preprocess["age_group"], categories=[
        "0-4", "5-14", "15-24", "25-34", "35-44", "45-54", "55-64", "65plus"], ordered=True)
    rf_data_preprocess.sort_values("age_group", inplace=True)
    rf_data_preprocess.to_parquet("data/preprocessing/rf_data.parquet", index=False)

    filtered_data_2022 = rf_data[rf_data["year"] == 2022]
    filtered_data_2022 = filtered_data_2022.loc[
        (filtered_data_2022["age_group"].isin(["all", "18plus", "15plus"])) & (filtered_data_2022["sex"] == "a") & (filtered_data_2022["risk_factor"] != "all")
    ]
    pivot_data = filtered_data_2022.pivot_table(index=["country"], columns="risk_factor", values="best", aggfunc="sum").reset_index()
    pivot_data.fillna(0, inplace=True)
    pivot_data.to_parquet("data/preprocessing/rf_type_data.parquet", index=False)
    print("Risk factor and pivot data saved successfully to Parquet.")
except Exception as e:
    print("Failed to save RF or pivot data to Parquet:", e)
