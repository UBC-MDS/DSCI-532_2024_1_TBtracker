# DSCI-532_2024_1_TBtracker - Global Tuberculosis Tracker

## Table of Contents

- [About the Project](#what-are-we-doing)
- [Access the Application](#access-the-application)
- [Data Sources and Structure](#data-sources-and-structure)
- [Application Features](#dashboard-functionality-overview)
- [How to Contribute](#how-to-contribute)
- [Run the Application Locally](#run-locally)
- [Stakeholders](#stakeholders)

## What are we doing?

![Demo GIF](https://github.com/UBC-MDS/DSCI-532_2024_1_TBtracker/blob/main/img/demo.gif?raw=true)

Welcome to the Global Tuberculosis Tracker! We're students from the UBC Master of Data Science program, and we've developed this tracker as a resource for easy access to global TB trends. Tuberculosis remains a significant global health issue, and our goal is to provide stakeholders like NGOs, policymakers, and public health organizations with a tool to streamline the analysis of TB incidence, trends, and associated risk factors through straightforward visualizations. By leveraging data from the WHO, our application supports well-informed decision-making in the battle against TB, emphasizing the disease's progression and its association with risk factors such as HIV.

**Using the Dashboard:**
You can access the live application [here!](https://dsci-532-2024-1-tbtracker.onrender.com/). The dashboard provides an interactive visualization of WHO Tuberculosis (TB) data across global and country-specific levels. You can explore TB incidence and mortality rates across countries, filter data based on the year of interest, and choose between displaying incidence or mortality data. Hovering over countries on the heatmap reveals specific data points through tooltips, and selecting a country directs you to a detailed analysis. 

**Getting Support:**
If you encounter any issues or have suggestions for enhancements, please open an issue [here](https://github.com/UBC-MDS/DSCI-532_2024_1_TBtracker/issues). We're here to help!

## Dashboard Functionality Overview

Our dashboard provides the following features:

- **Geospatial Heatmap:** Visual representation of TB incidence and mortality rates across countries.
- **Data Selection:** Refine data displayed based on the year of interest and choose between displaying incidence or mortality data.
- **Interactive Elements:** Hover over countries on the heatmap to reveal specific data points through tooltips. Selecting a country directs you to a detailed analysis tab.
    - **Country-Specific Trends:** Explore TB trends of the selected country through various visualizations including line plots, bar charts, and pie charts.

## Access the Application

Visit the live application [here!](https://dsci-532-2024-1-tbtracker.onrender.com/)

## Data Sources and Structure

The application leverages WHO datasets covering TB data for 217 countries from 2000 to 2022. Key data points include geographic and demographic information, annual TB incidence and mortality rates, risk factors, and additional insights such as TB-HIV coinfection rates and case fatality ratios.

## How to Contribute

Contributions are welcome! Please refer to our [Contributing Guidelines](/CONTRIBUTING.md) for more information. Whether you're interested in data updates, feature enhancements, or bug fixes, we value your contributions. You can also find our [Code of Conduct](/CODE_OF_CONDUCT.md) to ensure a positive and inclusive community.

## Run Locally

To run the **Global Tuberculosis Tracker** project locally on your machine, follow these steps:

1. **Clone the Repository**

    ```bash
    git clone https://github.com/UBC-MDS/DSCI-532_2024_1_TBtracker.git
    ```

2. **Navigate to the Project Directory**

    ```bash
    cd DSCI-532_2024_1_TBtracker
    ```

3. **Create a Conda Environment**

    ```bash
    conda env create -f environment.yml
    ```

4. **Activate the Conda Environment**

    ```bash
    conda activate TBtracker
    ```

5. **Run the Application**

    ```bash
    python app.py
    ```

    By following these instructions, users will be able to set up and run the **Global Tuberculosis Tracker** application locally, ensuring they have all the required dependencies installed through the Conda environment named `TBtracker`.

## Support

If you want to report a problem or suggest an enhancement please open an issue on this github repository.

## Stakeholders
- [Sandra Gross](https://github.com/sandygross)
- [Sean Mckay](https://github.com/sean-m-mckay)
- [Hina Bandukwala](https://github.com/hbandukw)
- [Yiwei Zhang](https://github.com/zywkloo)
