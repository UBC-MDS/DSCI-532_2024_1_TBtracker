# DSCI-532_2024_1_TBtracker - Global Tuberculosis Tracker

## Table of Contents

- [About the Project](#about-the-project)
- [Access the Application](#access-the-application)
- [Data Sources and Structure](#data-sources-and-structure)
- [Application Features](#application-features)
- [How to Contribute](#how-to-contribute)
- [Running the Application Locally](#run-locally)
- [Stakeholders](#stakeholders)

## About the Project

![image](https://github.com/UBC-MDS/DSCI-532_2024_1_TBtracker/assets/18610590/acab8f88-a3c3-44ee-8f8a-49fd29280461)

**The Global Tuberculosis Tracker**, developed by UBC MDS students, serves as a vital tool for visualizing Tuberculosis (TB) data worldwide. Aimed at NGOs, policymakers, and public health organizations, it simplifies the analysis of TB incidence, trends, and risk factors through intuitive visualizations. Utilizing WHO data, this application facilitates informed decisions in the fight against TB, highlighting the disease's dynamics and its interplay with risk factors like HIV. Our goal is to empower stakeholders with accurate data for strategic planning and interventions.

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

## Stakeholders
- [Sandra Gross](https://github.com/sandygross)
- [Sean Mckay](https://github.com/sean-m-mckay)
- [Hina Bandukwala](https://github.com/hbandukw)
- [Yiwei Zhang](https://github.com/zywkloo)

