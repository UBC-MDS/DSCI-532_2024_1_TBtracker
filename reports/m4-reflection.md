# Reflections and Updates on the TB Tracker Dashboard

## Dashboard Enhancements and Feedback Integration

Throughout the development of the TB Tracker Dashboard, our team implemented several optimizations and refinements to enhance performance, functionality, and user experience:

### Performance Optimizations


We've made several optimizations to enhance data processing efficiency in our application. Firstly, we switched our data loading mechanism to a **binary format (parquet)**, which allows for faster processing. Additionally, we created a **processed data file** that is loaded directly into the app, effectively minimizing redundant data manipulation tasks. To further improve performance, we utilized the **lru_cache decorator** to cache key functions, which has significantly reduced reload times. 

### User Interface and Usability Enhancements


We've made several updates to enhance the visual and functional aspects of our app, including a **new logo** and the **new title** "TB Tracker". To improve the accuracy and informativeness of our analytics, we **refined the metric calculations** for relative metrics. 
Additionally, we enhanced the readability and functionality of country-specific charts by implementing **clearer labeling** and adding **descriptive selection tabs**. Further improvements were made to the global visuals by **adjusting color scales** and incorporating **detailed tooltips** and interactive elements.

### Feedback Incorporation
Our revisions addressed specific feedback points from our peer reviews and user comments, including the following:
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
