import pandas as pd
tb_data = pd.read_csv("data/TB_burden_countries_2024-03-26.csv")

tb_data_preprocess = tb_data[["country", "iso2", "year", "e_pop_num", 
        "e_inc_num", "e_inc_num_hi", "e_inc_num_lo", 
        "e_inc_tbhiv_num", "e_inc_tbhiv_num_hi", "e_inc_tbhiv_num_lo",
        "e_mort_exc_tbhiv_num", "e_mort_exc_tbhiv_num_hi", "e_mort_exc_tbhiv_num_lo",
        "e_mort_tbhiv_num", "e_mort_tbhiv_num_hi", "e_mort_tbhiv_num_lo",
        "cfr", "cfr_hi", "cfr_lo"]]

tb_data_preprocess['incidence_total'] = tb_data_preprocess['e_inc_num'] + tb_data_preprocess['e_inc_num_hi']
tb_data_preprocess['incidence_rate'] = tb_data_preprocess['incidence_total']/tb_data_preprocess['e_pop_num']

tb_data_preprocess['mortality_total'] = tb_data_preprocess['e_mort_exc_tbhiv_num'] + tb_data_preprocess['e_mort_tbhiv_num']
tb_data_preprocess['mortality_rate'] = tb_data_preprocess['mortality_total']/tb_data_preprocess['e_pop_num']

tb_data_preprocess = tb_data_preprocess.dropna()
(tb_data_preprocess.to_csv('tb_data.csv', index=False))
