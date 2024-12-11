# Dataset Analysis
## Summary
Shape: (2652, 8)

### Missing Values
{'date': 99, 'language': 0, 'type': 0, 'title': 0, 'by': 262, 'overall': 0, 'quality': 0, 'repeatability': 0}

### Summary Statistics
{'date': {'count': 2553, 'unique': 2055, 'top': '21-May-06', 'freq': 8, 'mean': nan, 'std': nan, 'min': nan, '25%': nan, '50%': nan, '75%': nan, 'max': nan}, 'language': {'count': 2652, 'unique': 11, 'top': 'English', 'freq': 1306, 'mean': nan, 'std': nan, 'min': nan, '25%': nan, '50%': nan, '75%': nan, 'max': nan}, 'type': {'count': 2652, 'unique': 8, 'top': 'movie', 'freq': 2211, 'mean': nan, 'std': nan, 'min': nan, '25%': nan, '50%': nan, '75%': nan, 'max': nan}, 'title': {'count': 2652, 'unique': 2312, 'top': 'Kanda Naal Mudhal', 'freq': 9, 'mean': nan, 'std': nan, 'min': nan, '25%': nan, '50%': nan, '75%': nan, 'max': nan}, 'by': {'count': 2390, 'unique': 1528, 'top': 'Kiefer Sutherland', 'freq': 48, 'mean': nan, 'std': nan, 'min': nan, '25%': nan, '50%': nan, '75%': nan, 'max': nan}, 'overall': {'count': 2652.0, 'unique': nan, 'top': nan, 'freq': nan, 'mean': 3.0475113122171944, 'std': 0.7621797580962717, 'min': 1.0, '25%': 3.0, '50%': 3.0, '75%': 3.0, 'max': 5.0}, 'quality': {'count': 2652.0, 'unique': nan, 'top': nan, 'freq': nan, 'mean': 3.2092760180995477, 'std': 0.7967426636666686, 'min': 1.0, '25%': 3.0, '50%': 3.0, '75%': 4.0, 'max': 5.0}, 'repeatability': {'count': 2652.0, 'unique': nan, 'top': nan, 'freq': nan, 'mean': 1.4947209653092006, 'std': 0.598289430580212, 'min': 1.0, '25%': 1.0, '50%': 1.0, '75%': 2.0, 'max': 3.0}}

## Correlation Matrix
{'overall': {'overall': 1.0, 'quality': 0.8259352331454309, 'repeatability': 0.5126000083900123}, 'quality': {'overall': 0.8259352331454309, 'quality': 1.0, 'repeatability': 0.31212651153886395}, 'repeatability': {'overall': 0.5126000083900123, 'quality': 0.31212651153886395, 'repeatability': 1.0}}

## Narrative
### Narrative About the Data

The dataset consists of 2,652 entries, each containing information related to various items characterized by attributes such as date, language, type, title, the individual responsible for the item, and quantitative ratings on overall reception, quality, and repeatability. 

The data reveals several points of interest:
- **Dates**: There are 99 missing values in the date column, and while it includes numerous unique entries, the most frequent date appears to be '21-May-06'.
- **Language**: The dataset contains entries in 11 different languages, with 'English' being the most prevalent, accounting for 49% of the entries.
- **Type**: There are 8 distinct types, predominantly 'movie' which features prominently, suggesting a heavy bias towards cinematic content.
- **Titles and Creators**: The titles are diverse, with 2,312 unique titles and a frequent contributor being 'Kiefer Sutherland' with 48 entries attributed to him.
- **Ratings**: Quantitative ratings for 'overall', 'quality', and 'repeatability' demonstrate a mostly positive reception, with scores averaging 3.05, 3.21, and 1.49, respectively. 

However, it's important to note that the 'by' attribute has a substantial number of missing values (262), which may affect the analysis of creator-specific influences on ratings.

### Key Insights and Patterns

1. **Rating Correlation**: There is a strong positive correlation between 'overall' ratings and 'quality' ratings (0.83), indicating that items evaluated highly on quality are also given high overall ratings. A moderate correlation exists between 'overall' ratings and 'repeatability' (0.51), as well as between 'quality' and 'repeatability' (0.31), suggesting that while quality significantly impacts overall satisfaction, repeatability has a more modest relationship.
   
2. **Language and Content Type**: The dominance of English and the movie type suggests potential biases in audience engagement across different languages and genres. Further analysis could investigate how these factors influence overall and quality ratings.

3. **Rating Distributions**: The ratings show considerable clustering around mid-range values (1 to 5), with means slightly above the midpoint, indicating a generally favorable reception across most items. This may suggest that while there are standout hits, many items received average to good ratings, possibly reflecting the quality spectrum of the dataset.

### Recommended Visualizations

1. **Heatmap of Correlation Matrix**: A heatmap can effectively visualize the correlations between overall ratings, quality, and repeatability. This would highlight the strong correlation between overall ratings and quality, and provide insights into the relationships in one clear visual representation.

2. **Bar Chart of Ratings Distribution**: A bar chart depicting the distribution of 'overall', 'quality', and 'repeatability' scores (1-5 ratings) would help visualize how frequently certain ratings are assigned and reveal any skewness or clustering patterns in the ratings.

3. **Box Plot of Ratings by Language or Type**: A box plot could be constructed to compare the distribution of ratings (overall, quality, repeatability) across different languages or content types. This would help to uncover insights related to how rating patterns may vary by language and type of content, informing potential biases or differences in audience engagement.

By utilizing these visualizations, deeper insights can be attained, enriching the understanding of patterns and relationships present in the dataset.

## Visualizations
![media\scatter_plot.png](media\scatter_plot.png)
![media\heatmap.png](media\heatmap.png)
