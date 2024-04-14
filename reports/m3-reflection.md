## New Implementations:
- We've implemented a new card that displays global TB statistics for a selected year. Users can toggle between "absolute" and "relative" scales, or choose between "mortality" and "incidence" values. These statistics are dynamically updated and supplemented with percentage changes from the previous year (YoN) and the next year (NoY). Changes are displayed in 'red' for increases and 'blue' for decreases.
- A 'Learn More' button has been added, allowing users to access additional details about the dashboard.

## Modifications:
- We removed the histogram as it did not provide additional data beyond what was already visible in the global map.
- The color scheme of the map has been updated to enhance contrast between values.
- We did several small changes to the layout of the main page such as font size/type, 
- We established a consistent color theme across the main page.
- Modifications to the global map now highlight areas when hovered over to encourage user interaction.

## Issues:
- We encountered several layout challenges with the main page. The global map visualization, being a central feature, required enlargement, which was not straightforward. Fitting the new card on the page and adjusting the height of the column in the database object proved difficult. Ultimately, we had to position the card closer to the sidebar than originally intended, as adjusting the column width was more feasible than altering its height.
- Issues with missing countries on the global map: some countries were in the original raw data but were filtered out due to processing. We had to include those back into the map. However, there were some countries that had no data at all. To deal with those without leaving gaps in the map we imputed them by filling them with -1 and colouring those in gray

## Feedback:
We have incorporated feedback from our peers and professor by:
- Reordering the widgets, placing the scale option before the value selection.
- Eliminating scrolling on the main page to streamline the user experience.

## Challenge question:
- We incorporated group 18's approach of dynamically displaying statistics on a card along with associated increase/decrease compared to previous/next year. 
- Inspired by Group 2, we revised the color scheme of our map to improve data visibility and contrast. Although we are using different plotting libraries, we selected the closest available color scale.