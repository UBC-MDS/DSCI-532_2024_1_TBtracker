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

tb_data_preprocess = tb_data_preprocess.dropna()
(tb_data_preprocess.to_csv("data/preprocessing/tb_data.csv", index=False))


rf_data = pd.read_csv("data/raw/TB_burden_age_sex_2024-03-26.csv")
rf_data_preprocess = rf_data.loc[(rf_data["sex"] != 'a') & (rf_data["age_group"] != 'all')]
rf_data_preprocess = rf_data_preprocess[~rf_data_preprocess['age_group'].isin(['0-14', '15plus', '18plus'])].copy()
order_age = ['0-4', '5-14', '15-24', '25-34', '35-44', '45-54', '55-64', '65plus']
rf_data_preprocess['age_group'] = pd.Categorical(rf_data_preprocess['age_group'], categories=order_age, ordered=True)
rf_data_preprocess = rf_data_preprocess.sort_values('age_group')


(rf_data_preprocess.to_csv("data/preprocessing/rf_data.csv", index=False))