# Dataset Analysis
This README provides an analysis of the dataset provided along with key insights, recommendations, and visualizations.

## Summary
Shape of dataset: (2652, 8)

### Columns in the dataset
date, language, type, title, by, overall, quality, repeatability

### Missing Values
Below is the count of missing values per column:
- date: 99 missing values
- language: 0 missing values
- type: 0 missing values
- title: 0 missing values
- by: 262 missing values
- overall: 0 missing values
- quality: 0 missing values
- repeatability: 0 missing values

### Summary Statistics
Here are the summary statistics for numeric columns:
- date: {'count': 2553, 'unique': 2055, 'top': '21-May-06', 'freq': 8, 'mean': nan, 'std': nan, 'min': nan, '25%': nan, '50%': nan, '75%': nan, 'max': nan}
- language: {'count': 2652, 'unique': 11, 'top': 'English', 'freq': 1306, 'mean': nan, 'std': nan, 'min': nan, '25%': nan, '50%': nan, '75%': nan, 'max': nan}
- type: {'count': 2652, 'unique': 8, 'top': 'movie', 'freq': 2211, 'mean': nan, 'std': nan, 'min': nan, '25%': nan, '50%': nan, '75%': nan, 'max': nan}
- title: {'count': 2652, 'unique': 2312, 'top': 'Kanda Naal Mudhal', 'freq': 9, 'mean': nan, 'std': nan, 'min': nan, '25%': nan, '50%': nan, '75%': nan, 'max': nan}
- by: {'count': 2390, 'unique': 1528, 'top': 'Kiefer Sutherland', 'freq': 48, 'mean': nan, 'std': nan, 'min': nan, '25%': nan, '50%': nan, '75%': nan, 'max': nan}
- overall: {'count': 2652.0, 'unique': nan, 'top': nan, 'freq': nan, 'mean': 3.0475113122171944, 'std': 0.7621797580962717, 'min': 1.0, '25%': 3.0, '50%': 3.0, '75%': 3.0, 'max': 5.0}
- quality: {'count': 2652.0, 'unique': nan, 'top': nan, 'freq': nan, 'mean': 3.2092760180995477, 'std': 0.7967426636666686, 'min': 1.0, '25%': 3.0, '50%': 3.0, '75%': 4.0, 'max': 5.0}
- repeatability: {'count': 2652.0, 'unique': nan, 'top': nan, 'freq': nan, 'mean': 1.4947209653092006, 'std': 0.598289430580212, 'min': 1.0, '25%': 1.0, '50%': 1.0, '75%': 2.0, 'max': 3.0}

## Correlation Matrix
This section shows the correlations between numeric variables in the dataset:
- overall:
  - overall: 1.0
  - quality: 0.8259352331454309
  - repeatability: 0.5126000083900123
- quality:
  - overall: 0.8259352331454309
  - quality: 1.0
  - repeatability: 0.31212651153886395
- repeatability:
  - overall: 0.5126000083900123
  - quality: 0.31212651153886395
  - repeatability: 1.0

## Narrative
### 1. Narrative about the Data

The dataset comprises 2,652 entries covering eight different features. It includes information about various media types (likely movies or shows), their evaluations in terms of overall rating, quality, and repeatability, as well as metadata such as the date of release, language, type, title, and creator (by). Notably, there are some missing values, particularly in the 'date' and 'by' columns, with 99 missing dates and 262 entries missing the creator's name. The overall rating system appears to be based on a scale from 1 to 5, where the mean overall rating is approximately 3.05, suggesting a moderate reception. 

### 2. Key Insights and Patterns

- **Language and Type Distribution:** There are 11 different languages represented, with English being the most frequent. The type with the highest frequency is "movie" (2,211 occurrences), which may indicate a dataset skewed toward film rather than other media types like series or documentaries.

- **Rating Statistics:**
  - The overall rating has a mean of 3.05 with a standard deviation of 0.76, indicating moderate variability in the ratings given by users.
  - The quality rating is slightly higher on average at 3.21 and has a standard deviation of 0.80, suggesting reviewers feel more positively about the quality relative to the overall experience.
  - The repeatability rating has a mean of about 1.49, indicating that repeat viewing is not highly emphasized or encouraged, as denoted by its low ratings and close-to-minimum median.

- **Correlations:**
  - There is a strong positive correlation (0.83) between overall ratings and quality ratings, indicating that when the quality of a media piece is rated well, the overall rating tends to be high as well.
  - The correlation between overall ratings and repeatability (0.51) suggests that there is a moderate relationship—better overall scores align somewhat with higher repeatability.
  - The correlation between quality ratings and repeatability is lower (0.31), indicating that perceptions of quality do not significantly affect ratings of repeatability.

### 3. Recommended Visualizations

1. **Bar Plot for Rating Distributions:**
   A bar plot showing the distribution of the overall, quality, and repeatability ratings would effectively highlight the frequencies of each rating level (1 to 5). This plot would allow for visual comparisons between the three sets of ratings.

2. **Heatmap of the Correlation Matrix:**
   A heatmap can be a good visual aid to represent the correlations among the numeric variables (overall, quality, and repeatability). It would give a quick at-a-glance perspective of the strength and direction of associations.

3. **Box Plot for Ratings by Type or Language:**
   A box plot could illustrate the rating distribution for overall and quality ratings categorized by 'type' (movies, series, etc.) or 'language'. This would allow for the identification of any qualitative differences or trends across various media types or language groups.

These visualizations will help in understanding the underlying distributions and relationships within the dataset and can provide insights for further analysis or reporting.

## Visualizations
Below are the generated visualizations that help in understanding the relationships in the data:
![media\scatter_plot.png](media\scatter_plot.png)
![media\heatmap.png](media\heatmap.png)

