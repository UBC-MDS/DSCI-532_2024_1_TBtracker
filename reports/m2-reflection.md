## Implementation Overview
Our dashboard's main page features a geospatial heatmap and a histogram, which align with our initial proposal. Users can toggle between 'Incidence' or 'Mortality' of TB for a selected year and scale ('absolute' or 'relative'). Clicking on a country in the heatmap navigates to a dedicated tab displaying country-specific TB trends through five visualizations: three line plots (TB Mortality and Incidence, TB Case Fatality Ratio, TB-HIV Coinfection), a demographic-specific barchart, and a piechart for incidence by risk factors.

## Deviations from Proposal
We have slightly deviated from our original design in the following ways:

- The 'Year' selection was changed from a slider to a dropdown to avoid confusion about it being a single year versus a range.
- The method to transition to country-specific data was reconsidered for better user experience, opting for a separate tab rather than a pop-up replacement.
- The layout was changed on the global tab to group shared options affecting both graphs on the left-hand side, rather than having them above and below the graphs. Additionally, the charts were moved on top of each other to better fill the remaining vertical space.

## Known Issues
We have yet to implement confidence intervals on the line charts for country-specific trends, which is a priority for the next iteration. Additionally, we are aware of the need to enhance the dashboard's aesthetics.

## Limitations and Future Improvements
Our dashboard excels in interactive data visualization and ease of use. However, it currently lacks the display of statistical uncertainties, such as confidence intervals, which is crucial for informed decision-making. For future iterations, we plan to include these statistical elements and explore more engaging and aesthetic visualization options to improve the overall user experience.