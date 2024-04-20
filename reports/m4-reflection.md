# Reflections and Updates on the TB Tracker Dashboard

## Dashboard Enhancements and Feedback Integration

Throughout the development of the TB Tracker Dashboard, our team implemented several optimizations and refinements to enhance performance, functionality, and user experience:

### Performance Optimizations
- Switched data loading to a binary format (`parquet`) for faster processing.
- Created a processed data file loaded directly into the app, minimizing redundant data manipulation.
- Used `lru_cache` to cache key functions, significantly reducing reload times.

### User Interface and Usability Enhancements
- Introduced a new logo and updated the app title to "TB Tracker" to strengthen our visual identity.
- Refined the metric calculation for relative metrics to be more accurate and informative.
- Improved the readability and functionality of country-specific charts by using clearer labeling and adding descriptive selection tabs.
- Enhanced global visuals by adjusting color scales and adding detailed tooltips and interactive elements.

### Feedback Incorporation
Our revisions addressed specific feedback points from our peer reviews and user comments:
- Adjusted visualization elements like color schemes and legend placements to improve clarity and aesthetics.
- Altered the data presentation in tooltips and cards to enhance understanding of the metrics.
- Addressed technical challenges such as tooltip persistence in Altair and layout responsiveness across different resolutions.

## Reflection on Development Insights and Supports

The feedback from our instructors and peers was invaluable, especially in refining our metrics calculations and improving the interactivity and readability of our visualizations. Discussions with our mentor, Joel, provided crucial insights into handling specific technical challenges, such as the persistent tooltips and data representation issues.

While the support we received was instrumental, additional guidance on advanced data caching strategies and dynamic UI elements could further enhance our capabilities in developing more responsive and robust data applications.

## Deviations and Unimplemented Features

We intentionally deviated from some initial proposals to better align with effective visualization practices. For example, replacing a time range slider with a dropdown was a strategic decision based on user feedback and simplicity.

Some planned features, like a more dynamic time-range selection tool, were not implemented due to time constraints. If given more time, integrating these features would be a priority to improve user interaction and data exploration capabilities.

## Limitations and Future Directions

The TB Tracker Dashboard effectively provides insightful visualizations of TB data; however, it has limitations in handling dynamic data sets and varied screen resolutions. Future improvements would focus on enhancing the dashboard's adaptability to different devices and expanding its data analysis capabilities to include predictive modeling and trend analysis.

## Challenging

We add docstring to all our functions.
