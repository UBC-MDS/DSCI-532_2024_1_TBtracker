# DSCI-532_2024_1_TBtracker - Global Tuberculosis Tracker

## Table of Contents

- [About the Project](#about-the-project)
- [Access the Application](#access-the-application)
- [Data Sources and Structure](#data-sources-and-structure)
- [Application Features](#application-features)
- [How to Contribute](#how-to-contribute)
- [Running the Application Locally](#run-locally)
- [Stakeholders](#stakeholders)

## What are we doing?

![image](https://github.com/UBC-MDS/DSCI-532_2024_1_TBtracker/assets/18610590/acab8f88-a3c3-44ee-8f8a-49fd29280461)

We're students from the UBC Master of Data Science program, and we've developed The Global Tuberculosis Tracker as a resource for easy access to global TB trends. This tool is designed for NGOs, policymakers, and public health organizations to streamline the analysis of TB incidence, its trends, and associated risk factors through straightforward visualizations. By leveraging data from the WHO, our application supports well-informed decision-making in the battle against TB, emphasizing the disease's progression and its association with risk factors such as HIV. Our objective is to equip stakeholders with precise data to aid strategic planning and intervention efforts.


## Dahsboard Functionality Overview

Our dashboard provides an interactive visualization of WHO Tuberculosis (TB) data across global and country-specific levels. Here is an outline of its capabilities:
- Geospatial Heatmap: A world map visualizes TB 'Incidence' or 'Mortality' rates by country for a selected year. The map allows for two modes of data representation—absolute numbers or rates relative to population size.
- Data Selection: Users can refine the data displayed based on the year of interest and choose between displaying incidence or mortality data. This selection impacts both the heatmap and accompanying histogram.
- Interactive Elements: Hovering over countries on the heatmap reveals specific data points through tooltips. By selecting a country, users are directed to a detailed analysis in a separate tab.
    - Country-Specific Trends: Within this tab, the TB trends of the selected country are dissected through five distinct visualizations:
    - Line Plots: Three line plots track 'TB Mortality and Incidence', 'TB Case Fatality Ratio', and 'TB-HIV Coinfection' rates over time.
    -  Bar Chart: TB incidence rates are broken down by demographic groups. Users can choose multiple age groups at a time and one of the two categories for sex provided. (disclaimer: The sex information is restricted by WHO's categorizations).
    -  Pie Chart: A pie chart presents the distribution of TB incidence by various risk factors, such as smoking and alcohol use, providing insights into potential areas for public health interventions.
Each visualization has been designed with user interactivity in mind, offering the ability to customize the data displayed according to demographic and risk factor breakdowns.

## Access the Application

Visit the live application [here!](https://dsci-532-2024-1-tbtracker.onrender.com/)

## Data Sources and Structure

The application leverages two WHO datasets covering TB data for 217 countries from 2000 to 2022. Key data points include:

- **Geographic and Demographic Information:** Country ISO2 codes.
- **Annual TB Incidence and Mortality:** With and without HIV, including absolute estimates and confidence intervals.
- **Risk Factors:** Data on age, sex, and specific risk factors like harmful use of alcohol, diabetes, HIV, smoking, and undernourishment for 2022.
- **Additional Insights:** TB-HIV coinfection rates, case fatality ratios, and more.

This dataset, encompassing over two decades, provides a comprehensive overview of the TB epidemiological landscape globally, enabling detailed analysis and insights into the disease's trends and associated risk factors.

## Application Features

**Key Features Include:**

- **Interactive Global Map:** Visual representation of TB incidence and mortality rates across countries, with options to filter by year and view detailed country profiles.
- **Historical Trends and Distribution:** Analysis of global TB trends over time, allowing users to track changes in incidence, mortality, and co-infection rates.
- **Risk Factor Breakdown:** Detailed insights into the impact of various risk factors on TB incidence, offering a deeper understanding of the disease's dynamics.
- **Custom Data Views:** Options to view data in absolute terms or normalized by population, alongside the ability to toggle between TB metrics.

Developed with accessibility and user engagement in mind, the tracker aims to provide an intuitive platform for exploring and understanding TB data.

## How to Contribute

Contributions are welcome! Please refer to our [Contributing Guidelines](/CONTRIBUTING.md). We accept contributions ranging from data updates to feature enhancements. All contributors are expected to follow our [Code of Conduct](/CODE_OF_CONDUCT.md).

Given the GitHub repository URL and the details for the `environment.yml` file, here's how you can adjust the instructions to run the project locally, including how to install dependencies using Conda:

## Run Locally

To run the **Global Tuberculosis Tracker** project locally on your machine, follow these steps:

1. **Clone the Repository**

    First, clone the repository using Git:

    ```bash
    git clone https://github.com/UBC-MDS/DSCI-532_2024_1_TBtracker.git
    ```

2. **Navigate to the Project Directory**

    After cloning, change into the project directory:

    ```bash
    cd DSCI-532_2024_1_TBtracker
    ```

3. **Create a Conda Environment**

    Create a Conda environment named `TBtracker` using the `environment.yml` file located in the root of the directory. This file includes all necessary dependencies:

    ```bash
    conda env create -f environment.yml
    ```
    It will create a new environment named `TBtracker` and install the specified packages and their dependencies.

4. **Activate the Conda Environment**

    Once the environment is created, activate it:

    ```bash
    conda activate TBtracker
    ```

5. **Run the Application**

    With the `TBtracker` environment activated, you can now run the application:

    ```bash
    python app.py
    ```

    This command will start the application. Follow any on-screen instructions to access it in your web browser.
    By default, you will see `Dash is running on http://127.0.0.1:8000/`. So just copy and paste the URL into your browser.

By following these instructions, users will be able to set up and run the **Global Tuberculosis Tracker** application locally, ensuring they have all the required dependencies installed through the Conda environment named `TBtracker`.

## Support

If you want to report a problem or suggest an enhancement please open an issue on this github repository.


## Stakeholders
- [Sandra Gross](https://github.com/sandygross)
- [Sean Mckay](https://github.com/sean-m-mckay)
- [Hina Bandukwala](https://github.com/hbandukw)
- [Yiwei Zhang](https://github.com/zywkloo)

