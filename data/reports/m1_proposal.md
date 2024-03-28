### Section 1: Motivation and purpose

Our role: Public Health Organization

Target Audience: NGO, Policymakers, Public Health Organizations

Tuberculosis (TB) is a pervasive infectious disease primarily affecting the lungs and stands as the principal cause of mortality among individuals with HIV. Annually, it afflicts approximately 10 million individuals globally, leading to around 1.5 million deaths (WHO, 2019). To curb the spread of TB and mitigate its impact, it necessitates strategic allocation of medical resources and medications by non-governmental organizations (NGOs), given the current global prevalence of this disease (TB Alliance, n.d.). Despite the urgency, NGOs frequently encounter obstacles in obtaining timely, detailed, and comprehensive data on TB incidence, treatment outcomes, and main risk factors. The process of gathering, processing, and analyzing such data is often fraught with challenges, including time constraints and a lack of necessary programming skills, which impedes efficient and effective data utilization. To bridge this gap, we envision the development of a data visualization application specifically designed to empower NGOs and public health entities. This tool will provide an intuitive interface to explore the global dynamics of tuberculosis, monitoring its prevalence and trends over time across different nations. Moreover, it will offer insights into critical risk factors, including age, HIV status, and gender, thereby equipping NGOs with the necessary knowledge to optimize their resource distribution and intervention strategies. Our app generally aims to streamline the decision-making process for health professionals and policy-makers, fostering more targeted and impactful responses to the global TB crisis.

### Section 2: Data Description

We will be developing a dashboard to visualize the **global prevalence of Tuberculosis (TB) over time** and the **associated risk factors per country**.

We are using two datasets from the World Health Organization (WHO) which can be found [here](https://www.google.com/url?q=https://extranet.who.int/tme/generateCSV.asp?ds%3Destimates&sa=D&source=docs&ust=1711469479701182&usg=AOvVaw2Uui8IYP7fyZ3E0_nXPnGw) and [here](https://www.google.com/url?q=https://extranet.who.int/tme/generateCSV.asp?ds%3Destimates_age_sex&sa=D&source=docs&ust=1711469600536959&usg=AOvVaw3O2Ts9QUTKv5xk08Arn6fE). The first dataset summarizes global trends of TB for 217 countries from 2000 to 2022.

-   Geographic and demographic information: `iso2 code`

-   Annual data per country (identified by `year`):

    -   Population (`e_pop_num`),

    -   WHO-generated estimates:

        -   Absolute estimates and confidence intervals of TB incidence with and without HIV: 
            - without HIV: `e_inc_num`, `e_inc_num_hi`, `e_inc_num_lo`
            - with HIV: `e_inc_tbhiv_num`, `e_inc_tbhiv_num_hi`, `e_inc_tbhiv_num_lo`

        -   Absolute estimates and confidence intervals TB-HIV coinfection (`e_inc_tbhiv_num`, `e_inc_tbhiv_num_hi`, `e_inc_tbhiv_num_lo`)

        -   Absolute estimates and confidence intervals of mortality in the population with and without HIV: 
        - without HIV: `e_mort_exc_tbhiv_num`, `e_mort_exc_tbhiv_hi`, `e_mort_exc_tbhiv_lo`
        - with HIV: `e_mort_tbhiv_num`, `e_mort_tbhiv_num_hi`, `e_mort_tbhiv_num_lo`

        -   Case fatality ratio (`cfr`) and confidence intervals (`c_cdr_hi`, `c_cdr_lo`): calculated as mortality/incidence

We will visualize the different WHO-generated estimates to gain an understanding of the epidemiological landscape of TB. Additionally, since HIV is known to strongly increase the risk of TB (Bell & Noursadeghi, 2017), we want to look at **TB incidence, mortality** (for the population with and without HIV) in conjuction with the **TB-HIV coinfection estimates** to visually display the interplay between the two.

The second dataset summarizes the TB incidence estimates for 215 countries (missing data for 'Netherlands Antilles', 'Serbia & Montenegro') aggregated by **Age, Sex and Risk factors** for the year 2022. Age: '0-14', '0-4', '15-24', '15plus', '18plus', '25-34', '35-44', '45-54', '5-14', '55-64', '65plus' Sex: ‘female’, ‘male’ Risk factors: alc=Harmful use of alcohol; dia=Diabetes; hiv=HIV; smk=Smoking; und=Undernourishment. Finally, we want to visualize other global risk factors associated with TB as measured by the incidence estimates. Unfortunately, since we only have this data for 2022, we will not be able to look at the effects of these risk factors over time.

Additional data that would be useful for us would be the rate of drug-resistant TB, as the treatment schedule and types of drugs needed differs depending on the type of drug-resistance (Mase SR, Chorba T., 2019). It would also be helpful to have the prevalence rate of latent TB in the population - Since active cases are often seen in individuals with pre-existing latent infections. For example, more than 80% of cases in the US result from latent TB infection (CDC, 2022). Unfortunately this is not something that can be inferred directly from the available data on incidence and mortality, as this is only a measurement of the active cases.

## Section 3: Research Questions and Usage Scenario

Belinda is a director of Clinical Operations at the NGO TB Alliance. Part of her job involves forecasting the number of TB drugs that will need to be developed and allocated to each country, based on their TB case load. The forecasted amount she’ll need to submit will be informed by trends from previous years, so she wants to explore historical trends in TB prevalence across different countries, including the case occurrence and mortality rate. Additionally, since the treatment protocol may differ when considering co-infection with HIV (Bhatt A, Quazi Syed Z, Singh H, 2023), she wants a breakdown for those numbers as well.


When Belinda logs in to the TB Tracker app, she’ll be presented with a global view of the caseload across different countries displayed on a map, along with a summary graph of the total caseload per country for the current year - Filters on the top will allow her to look at the incidence or mortality rate, and on the bottom she can switch the year the data is plotted. She can then click on individual countries to get a more detailed breakdown, allowing her to see trends across different years, along with the caseload for HIV-TB coinfection. Additionally, she will get to explore a breakdown by risk factor for the most recent year, if she needs to look at different treatment plans for patients based on their age or other medical conditions. 


Based on this data, Belinda will be able to get a good sense of the incidence rate across different countries which will inform her discussions with drug manufacturers, and the amount of money allocated towards production of drugs. The risk factor breakdown can give critical insights into the need for development of new drugs targetting specific age groups or other risk factors.

**References**:

Mase SR, Chorba T. Treatment of Drug-Resistant Tuberculosis. Clin Chest Med. 2019 Dec;40(4):775-795. doi: 10.1016/j.ccm.2019.08.002. PMID: 31731984; PMCID: PMC7000172.

Bell, L., & Noursadeghi, M. (2017). Pathogenesis of HIV-1 and Mycobacterium tuberculosis co-infection. *Nature Reviews Microbiology*, *16*(2), 80–90. https://doi.org/10.1038/nrmicro.2017.128

Bhatt A, Quazi Syed Z, Singh H. Converging Epidemics: A Narrative Review of Tuberculosis (TB) and Human Immunodeficiency Virus (HIV) Coinfection. Cureus. 2023 Oct 25;15(10):e47624. doi: 10.7759/cureus.47624. PMID: 38021882; PMCID: PMC10667792.

TB Alliance (n.d). https://www.tballiance.org/

WHO. (2019). Tuberculosis. https://www.who.int/health-topics/tuberculosis#tab=tab_1

CDC (2022). Latent TB Infection in the United States – Published Estimates. https://www.cdc.gov/tb/statistics/ltbi.htm