# Tuberculosis Tracker <img src="img/Logo.png" align="right" width=175 height=175 alt="" />

[![GitHub issues](https://img.shields.io/github/issues/UBC-MDS/DSCI-532_2024_1_TBtracker.svg)](https://github.com/UBC-MDS/DSCI-532_2024_1_TBtracker/issues)
[![GitHub last commit](https://img.shields.io/github/last-commit/UBC-MDS/DSCI-532_2024_1_TBtracker.svg)](https://github.com/UBC-MDS/DSCI-532_2024_1_TBtracker/commits/main)
[![GitHub release](https://img.shields.io/github/release/UBC-MDS/DSCI-532_2024_1_TBtracker.svg)](https://github.com/UBC-MDS/DSCI-532_2024_1_TBtracker/releases)



Visualize global and country-specific trends in tuberculosis incidence and mortality over time.

For easy navigation, you can click on the links below to jump directly to a specific section or simply scroll through the page.

- [About the Project](#about-the-project)
- [Usage for users](#usage-for-users)
- [Usage for Users](#usage-for-users)
- [Data Sources and Structure](#data-sources-and-structure)
- [Usage for Developers](#usage-for-developers)
- [How to Contribute](#how-to-contribute)
- [Contributors](#contributors)

## About the Project

![Demo GIF](https://github.com/UBC-MDS/DSCI-532_2024_1_TBtracker/blob/main/img/demo.gif?raw=true)

We're students from the UBC Master of Data Science program, and we've developed The Global Tuberculosis Tracker as a resource for easy access to global TB trends. This tool is designed for NGOs, policymakers, and public health organizations to streamline the analysis of TB incidence, its trends, and associated risk factors through straightforward visualizations. By leveraging data from the WHO, our application supports well-informed decision-making in the battle against TB, emphasizing the disease's progression and its association with risk factors such as HIV. Our objective is to equip stakeholders with precise data to aid strategic planning and intervention efforts.

## Usage for Users

The live application can be visited [here!](https://dsci-532-2024-1-tbtracker.onrender.com/)

The dashboard features a sidebar for user input and a main section for data display. In the sidebar, users can select the metric type (absolute or relative, which is proportional to the population size), the variable of interest (incidence or mortality), and the desired time range. The data display section includes an interactive global map where hovering over a country provides a brief statistical summary for that country and its global context. Clicking on a specific country directs users to a detailed tab, offering in-depth information about that country's risk factors and historical trends. Additionally, users can directly access this country-specific information through the "Country-Specific" tab in the top menu.
In this tab, you can filter for desired risk factors using the dropdown menu or by clicking on elements within the pie chart's legend. For some countries, data is unavailable, and these will be colored in grey.

## Data Sources and Structure

The application leverages two WHO datasets covering TB data for 217 countries from 2000 to 2022. Key data points include geographic information, annual TB incidence and mortality (with and without HIV), risk Factors such as age, sex, as well alcohol abuse, diabetes, HIV, smoking, and undernourishment for 2022.

## Usage for Developers

### Installation For Local Development

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

## How to Contribute

Contributions are welcome! Please refer to our [Contributing Guidelines](/CONTRIBUTING.md). We accept contributions ranging from data updates to feature enhancements. All contributors are expected to follow our [Code of Conduct](/CODE_OF_CONDUCT.md).

## Contributors

Sandra Gross, Sean McKay, Hina Bandukwala, Yiwei Zhang

