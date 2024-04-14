import pandas as pd

tb_data = pd.read_csv("data/raw/TB_burden_countries_2024-03-26.csv")

tb_data_preprocess = tb_data[
    [
        "country",
        "iso2",
        "iso3",
        "iso_numeric",
        "year",
        "e_pop_num",
        "e_inc_num",
        "e_inc_num_hi",
        "e_inc_num_lo",
        "e_inc_tbhiv_num",
        "e_inc_tbhiv_num_hi",
        "e_inc_tbhiv_num_lo",
        "e_mort_exc_tbhiv_num",
        "e_mort_exc_tbhiv_num_hi",
        "e_mort_exc_tbhiv_num_lo",
        "e_mort_tbhiv_num",
        "e_mort_tbhiv_num_hi",
        "e_mort_tbhiv_num_lo",
        "cfr",
        "cfr_hi",
        "cfr_lo",
    ]
].copy()


cols_no_na = [
    "e_pop_num",
    "e_inc_num",
    "e_inc_num_hi",
    "e_inc_num_lo",
    "e_mort_exc_tbhiv_num",
    "e_mort_exc_tbhiv_num_hi",
    "e_mort_exc_tbhiv_num_lo",
    "e_mort_tbhiv_num",
    "e_mort_tbhiv_num_hi",
    "e_mort_tbhiv_num_lo",
    "cfr",
    "cfr_hi",
    "cfr_lo",
]

tb_data_preprocess["incidence_total"] = (
    tb_data_preprocess["e_inc_num"] + tb_data_preprocess["e_inc_num_hi"]
)
tb_data_preprocess["incidence_rate"] = (
    tb_data_preprocess["incidence_total"] / tb_data_preprocess["e_pop_num"]
)

tb_data_preprocess["mortality_total"] = (
    tb_data_preprocess["e_mort_exc_tbhiv_num"] + tb_data_preprocess["e_mort_tbhiv_num"]
)
tb_data_preprocess["mortality_rate"] = (
    tb_data_preprocess["mortality_total"] / tb_data_preprocess["e_pop_num"]
)

tb_data_preprocess["cfr_total"] = tb_data_preprocess["cfr"]
tb_data_preprocess["tbhiv_coinfection_total"] = (
    tb_data_preprocess["e_inc_tbhiv_num"] + tb_data_preprocess["e_inc_tbhiv_num_hi"]
)
tb_data_preprocess["tbhiv_coinfection_rate"] = (
    tb_data_preprocess["tbhiv_coinfection_total"] / tb_data_preprocess["e_pop_num"]
)

countries = tb_data_preprocess["country"].unique()
years = range(tb_data_preprocess["year"].min(), tb_data_preprocess["year"].max() + 1)

all_combinations = pd.MultiIndex.from_product(
    [countries, years], names=["country", "year"]
).to_frame(index=False)

tb_data_preprocess = pd.merge(
    all_combinations, tb_data_preprocess, on=["country", "year"], how="left"
)


# We need the iso_numeric columns for lookup in the geomap
tb_data_preprocess["iso_numeric"] = tb_data_preprocess.groupby("country")[
    "iso_numeric"
].transform(lambda x: x.fillna(x.max()))

# We can set others to a default value of -1
tb_data_preprocess = tb_data_preprocess.fillna(-1)

(tb_data_preprocess.to_csv("data/preprocessing/tb_data.csv", index=False))


rf_data = pd.read_csv("data/raw/TB_burden_age_sex_2024-03-26.csv")
rf_data_preprocess = rf_data.loc[
    (rf_data["sex"] != "a") & (rf_data["age_group"] != "all")
]
rf_data_preprocess = rf_data_preprocess[
    ~rf_data_preprocess["age_group"].isin(["0-14", "15plus", "18plus"])
].copy()
order_age = ["0-4", "5-14", "15-24", "25-34", "35-44", "45-54", "55-64", "65plus"]
rf_data_preprocess["age_group"] = pd.Categorical(
    rf_data_preprocess["age_group"], categories=order_age, ordered=True
)
rf_data_preprocess = rf_data_preprocess.sort_values("age_group")

(rf_data_preprocess.to_csv("data/preprocessing/rf_data.csv", index=False))


# Filter the dataset for the year 2022
# Filter data for the year 2022
filtered_data_2022 = rf_data[rf_data["year"] == 2022]

# Filter data based on age_group and sex criteria
filtered_data_2022 = filtered_data_2022.loc[
    (
        (filtered_data_2022["age_group"].isin(["all", "18plus", "15plus"]))
        & (filtered_data_2022["sex"] == "a")
        & (filtered_data_2022["risk_factor"] != "all")
    )
]

pivot_data = filtered_data_2022.pivot_table(
    index=["country"], columns="risk_factor", values="best", aggfunc="sum"
).reset_index()

# Fill NaN values with 0, assuming missing values mean no reported incidences
pivot_data.fillna(0, inplace=True)

# Save the preprocessed data for the pie chart visualization
(pivot_data.to_csv("data/preprocessing/rf_type_data.csv", index=False))
