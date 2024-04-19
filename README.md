# Tuberculosis Tracker <img src="img/Logo.png" align="right" width=175 height=175 alt="" />

[![GitHub issues](https://img.shields.io/github/issues/UBC-MDS/DSCI-532_2024_1_TBtracker.svg)](https://github.com/UBC-MDS/DSCI-532_2024_1_TBtracker/issues)
[![GitHub last commit](https://img.shields.io/github/last-commit/UBC-MDS/DSCI-532_2024_1_TBtracker.svg)](https://github.com/UBC-MDS/DSCI-532_2024_1_TBtracker/commits/main)
[![GitHub release](https://img.shields.io/github/release/UBC-MDS/DSCI-532_2024_1_TBtracker.svg)](https://github.com/UBC-MDS/DSCI-532_2024_1_TBtracker/releases)



Visualize global and country-specific trends in tuberculosis incidence and mortality over time.

For easy navigation, you can click on the links below to jump directly to a specific section or simply scroll through the page.

- [About the Project](#about-the-project)
- [Usage](#general-usage)
- [Data Sources and Structure](#data-sources-and-structure)
- [Usage for Developers](#usage-for-developers)
- [How to Contribute](#how-to-contribute)
- [Contributors](#contributors)

## About the Project

![Demo GIF](https://github.com/UBC-MDS/DSCI-532_2024_1_TBtracker/blob/main/img/demo.gif?raw=true)

We're students from the UBC Master of Data Science program, and we've developed The Global Tuberculosis Tracker as a resource for easy access to global TB trends. This tool is designed for NGOs, policymakers, and public health organizations to streamline the analysis of TB incidence, its trends, and associated risk factors through straightforward visualizations. By leveraging data from the WHO, our application supports well-informed decision-making in the battle against TB, emphasizing the disease's progression and its association with risk factors such as HIV. Our objective is to equip stakeholders with precise data to aid strategic planning and intervention efforts.

## General Usage

The live application can be visited [here!](https://dsci-532-2024-1-tbtracker.onrender.com/)

### Global tab
1. Widgets:
- Metric Type: Select whether you want to view the data in absolute or relative terms. The relative metric is proportonal to the population size.
- Variable of Interest: Choose between "incidence" or "mortality". Links to definitions of these terms can be found here for incidence and here for mortality.
- Year: Pick the Year for which you want the data to be displayed.

2. View Data on the Interactive Global Map:
- Hover Over Countries: Move your cursor over any country on the map to see a brief relevant metrics for that country. 
- Click on Countries: For a more detailed analysis, click on any country. This will direct you to the country-specific tab that provides in-depth information about that country’s risk factors and historical data trends. 
Note: Grey-Colored Countries: Notice that some countries might be colored in grey on the map, indicating that data for these countries is unavailable.

### Country tab
- Directly access the country tab: Click on the "Country-Specific" tab in the dashboard’s top menu to view detailed information for a specific country. 
- If you do not want to go back and forth between the main and country-specific tabs, we have provided functionality to directly select a country on the country-specifc tab.


## Data Sources and Structure

The application leverages two WHO datasets covering TB data for 217 countries from 2000 to 2022. Key data points include geographic information, annual TB incidence and mortality (with and without HIV), risk Factors such as age, sex, as well alcohol abuse, diabetes, HIV, smoking, and undernourishment for 2022.

## Need support?

If you want to report a problem or give an suggestion, we would love for you to open an issue at this github repository and we will get on to it in a timely manner.

## Usage for Developers

### Installation For Local Development

To run the **Global Tuberculosis Tracker** project locally on your machine, follow these steps:

1. **Clone the Repository**

    Open your terminal, go to the desired directory, and clone the repository by executing this Git command:

    ```bash
    git clone https://github.com/UBC-MDS/DSCI-532_2024_1_TBtracker.git
    ```

2. **Navigate to the Project Directory**

    Once you've cloned the repository, switch to the project directory by running the following command in your terminal:

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

    After creating the environment, activate it with the following command:

    ```bash
    conda activate TBtracker
    ```

5. **Run the Application**

    With the `TBtracker` environment activated, you can now start the application:

    ```bash
    python app.py
    ```

    This command will start the application. Follow any on-screen instructions to access it in your web browser.
    By default, you will see `Dash is running on http://127.0.0.1:8000/`. So just copy and paste the URL into your browser.

## How to Contribute

Contributions are welcome! Please refer to our [Contributing Guidelines](/CONTRIBUTING.md). We accept contributions ranging from data updates to feature enhancements. All contributors are expected to follow our [Code of Conduct](/CODE_OF_CONDUCT.md).

## Contributors

Sandra Gross, Sean McKay, Hina Bandukwala, Yiwei Zhang

