# Dataset Analysis
## Summary
Shape: (2363, 11)

### Missing Values
{'Country name': 0, 'year': 0, 'Life Ladder': 0, 'Log GDP per capita': 28, 'Social support': 13, 'Healthy life expectancy at birth': 63, 'Freedom to make life choices': 36, 'Generosity': 81, 'Perceptions of corruption': 125, 'Positive affect': 24, 'Negative affect': 16}

### Summary Statistics
{'Country name': {'count': 2363, 'unique': 165, 'top': 'Lebanon', 'freq': 18, 'mean': nan, 'std': nan, 'min': nan, '25%': nan, '50%': nan, '75%': nan, 'max': nan}, 'year': {'count': 2363.0, 'unique': nan, 'top': nan, 'freq': nan, 'mean': 2014.7638595006347, 'std': 5.059436468192795, 'min': 2005.0, '25%': 2011.0, '50%': 2015.0, '75%': 2019.0, 'max': 2023.0}, 'Life Ladder': {'count': 2363.0, 'unique': nan, 'top': nan, 'freq': nan, 'mean': 5.483565806178587, 'std': 1.1255215132391925, 'min': 1.281, '25%': 4.647, '50%': 5.449, '75%': 6.3235, 'max': 8.019}, 'Log GDP per capita': {'count': 2335.0, 'unique': nan, 'top': nan, 'freq': nan, 'mean': 9.399671092077089, 'std': 1.1520694444710216, 'min': 5.527, '25%': 8.506499999999999, '50%': 9.503, '75%': 10.3925, 'max': 11.676}, 'Social support': {'count': 2350.0, 'unique': nan, 'top': nan, 'freq': nan, 'mean': 0.8093693617021277, 'std': 0.12121176420299144, 'min': 0.228, '25%': 0.744, '50%': 0.8345, '75%': 0.904, 'max': 0.987}, 'Healthy life expectancy at birth': {'count': 2300.0, 'unique': nan, 'top': nan, 'freq': nan, 'mean': 63.40182826086957, 'std': 6.842644351828009, 'min': 6.72, '25%': 59.195, '50%': 65.1, '75%': 68.5525, 'max': 74.6}, 'Freedom to make life choices': {'count': 2327.0, 'unique': nan, 'top': nan, 'freq': nan, 'mean': 0.750281908036098, 'std': 0.13935703459253465, 'min': 0.228, '25%': 0.661, '50%': 0.771, '75%': 0.862, 'max': 0.985}, 'Generosity': {'count': 2282.0, 'unique': nan, 'top': nan, 'freq': nan, 'mean': 9.772129710780206e-05, 'std': 0.16138760312630687, 'min': -0.34, '25%': -0.112, '50%': -0.022, '75%': 0.09375, 'max': 0.7}, 'Perceptions of corruption': {'count': 2238.0, 'unique': nan, 'top': nan, 'freq': nan, 'mean': 0.7439709562109026, 'std': 0.1848654805936834, 'min': 0.035, '25%': 0.687, '50%': 0.7985, '75%': 0.86775, 'max': 0.983}, 'Positive affect': {'count': 2339.0, 'unique': nan, 'top': nan, 'freq': nan, 'mean': 0.6518820008550662, 'std': 0.10623970474397627, 'min': 0.179, '25%': 0.572, '50%': 0.663, '75%': 0.737, 'max': 0.884}, 'Negative affect': {'count': 2347.0, 'unique': nan, 'top': nan, 'freq': nan, 'mean': 0.27315083084789094, 'std': 0.08713107245795021, 'min': 0.083, '25%': 0.209, '50%': 0.262, '75%': 0.326, 'max': 0.705}}

## Correlation Matrix
{'year': {'year': 1.0, 'Life Ladder': 0.04684610051502284, 'Log GDP per capita': 0.0801038042092043, 'Social support': -0.043073662490006374, 'Healthy life expectancy at birth': 0.16802616683445498, 'Freedom to make life choices': 0.23297364128772255, 'Generosity': 0.03086444784813772, 'Perceptions of corruption': -0.08213550694924891, 'Positive affect': 0.013052478449081329, 'Negative affect': 0.2076422697785905}, 'Life Ladder': {'year': 0.04684610051502284, 'Life Ladder': 1.0, 'Log GDP per capita': 0.7835562687553224, 'Social support': 0.7227383546061082, 'Healthy life expectancy at birth': 0.7149267857617213, 'Freedom to make life choices': 0.5382097259777253, 'Generosity': 0.1773984122978725, 'Perceptions of corruption': -0.43048504537012405, 'Positive affect': 0.5152831989958622, 'Negative affect': -0.3524120124832057}, 'Log GDP per capita': {'year': 0.0801038042092043, 'Life Ladder': 0.7835562687553224, 'Log GDP per capita': 1.0, 'Social support': 0.6853285024924187, 'Healthy life expectancy at birth': 0.8193259264445769, 'Freedom to make life choices': 0.36481604533095585, 'Generosity': -0.0007659847139494051, 'Perceptions of corruption': -0.3538925582135235, 'Positive affect': 0.2308681589786361, 'Negative affect': -0.2606891913521718}, 'Social support': {'year': -0.043073662490006374, 'Life Ladder': 0.7227383546061082, 'Log GDP per capita': 0.6853285024924187, 'Social support': 1.0, 'Healthy life expectancy at birth': 0.5977870467057778, 'Freedom to make life choices': 0.40413086354010685, 'Generosity': 0.06523987499766251, 'Perceptions of corruption': -0.22140950297465545, 'Positive affect': 0.42452443789791866, 'Negative affect': -0.45487764009062776}, 'Healthy life expectancy at birth': {'year': 0.16802616683445498, 'Life Ladder': 0.7149267857617213, 'Log GDP per capita': 0.8193259264445769, 'Social support': 0.5977870467057778, 'Healthy life expectancy at birth': 1.0, 'Freedom to make life choices': 0.37574513947224963, 'Generosity': 0.015168207483191342, 'Perceptions of corruption': -0.303129985574044, 'Positive affect': 0.21798223187372157, 'Negative affect': -0.15032954194441223}, 'Freedom to make life choices': {'year': 0.23297364128772255, 'Life Ladder': 0.5382097259777253, 'Log GDP per capita': 0.36481604533095585, 'Social support': 0.40413086354010685, 'Healthy life expectancy at birth': 0.37574513947224963, 'Freedom to make life choices': 1.0, 'Generosity': 0.32139585162490525, 'Perceptions of corruption': -0.46602264599269855, 'Positive affect': 0.5783981600148212, 'Negative affect': -0.27895931560861464}, 'Generosity': {'year': 0.03086444784813772, 'Life Ladder': 0.1773984122978725, 'Log GDP per capita': -0.0007659847139494051, 'Social support': 0.06523987499766251, 'Healthy life expectancy at birth': 0.015168207483191342, 'Freedom to make life choices': 0.32139585162490525, 'Generosity': 1.0, 'Perceptions of corruption': -0.2700039823813803, 'Positive affect': 0.3006076315281511, 'Negative affect': -0.07197460755980206}, 'Perceptions of corruption': {'year': -0.08213550694924891, 'Life Ladder': -0.43048504537012405, 'Log GDP per capita': -0.3538925582135235, 'Social support': -0.22140950297465545, 'Healthy life expectancy at birth': -0.303129985574044, 'Freedom to make life choices': -0.46602264599269855, 'Generosity': -0.2700039823813803, 'Perceptions of corruption': 1.0, 'Positive affect': -0.2742083415576299, 'Negative affect': 0.2655554332512859}, 'Positive affect': {'year': 0.013052478449081329, 'Life Ladder': 0.5152831989958622, 'Log GDP per capita': 0.2308681589786361, 'Social support': 0.42452443789791866, 'Healthy life expectancy at birth': 0.21798223187372157, 'Freedom to make life choices': 0.5783981600148212, 'Generosity': 0.3006076315281511, 'Perceptions of corruption': -0.2742083415576299, 'Positive affect': 1.0, 'Negative affect': -0.33445111286959034}, 'Negative affect': {'year': 0.2076422697785905, 'Life Ladder': -0.3524120124832057, 'Log GDP per capita': -0.2606891913521718, 'Social support': -0.45487764009062776, 'Healthy life expectancy at birth': -0.15032954194441223, 'Freedom to make life choices': -0.27895931560861464, 'Generosity': -0.07197460755980206, 'Perceptions of corruption': 0.2655554332512859, 'Positive affect': -0.33445111286959034, 'Negative affect': 1.0}}

## Narrative
### 1. Narrative about the Data

This dataset contains information on various aspects of well-being and socio-economic factors across different countries over a period of years, specifically from 2005 to 2023. The dataset includes a total of 2,363 entries and 11 attributes, primarily focusing on subjective well-being (Life Ladder), economic measures (Log GDP per capita), social relationships (Social support), health metrics (Healthy life expectancy), personal freedoms (Freedom to make life choices), generosity, and perceptions of corruption. 

Notably, there are missing values in several columns, with Log GDP per capita experiencing 28 missing entries, Social support with 13, and Healthy life expectancy at birth with 63, among others. This suggests potential limitations on the completeness of the analysis, inviting careful consideration when interpreting the results.

### 2. Key Insights and Patterns

- **Life Ladder Correlation**: The Life Ladder, a subjective measure of well-being, exhibits a strong positive correlation with Log GDP per capita (0.78), Social support (0.72), and Healthy life expectancy at birth (0.71). This indicates that higher economic success, better social relationships, and improved health outcomes are associated with higher reported well-being among individuals in various countries.

- **Impact of Freedom**: Freedom to make life choices positively correlates with multiple well-being indicators, including Life Ladder (0.54) and Positive affect (0.58), suggesting that granting individuals personal freedoms may enhance their overall life satisfaction and emotional well-being.

- **Negative Affect**: There is a noticeable negative correlation between Negative affect and Life Ladder (-0.35), highlighting that increasing negative emotions tend to coincide with lower measures of happiness. In contrast, Positive affect shows a strong positive correlation with Life Ladder (0.52), emphasizing the impact of positive emotions on perceived well-being.

- **Perceptions of Corruption**: The data reflects a negative relationship between Perceptions of corruption and Life Ladder (-0.43), indicating that countries perceived as more corrupt may have lower levels of reported happiness. This is compounded by a similar negative relationship with Freedom to make life choices (-0.47), suggesting that corruption may also inhibit personal expression and autonomy.

### 3. Recommended Visualizations

1. **Scatter Plot Matrix**: A comprehensive scatter plot matrix would allow for an examination of the correlations between all numerical attributes in the dataset. This visualization would help identify trends and correlations more comprehensively.

2. **Heatmap of the Correlation Matrix**: A heatmap representation of the correlation matrix would visually depict the strength and direction of relationships between variables. This would enable quick identification of strong correlations and highlights areas for further analysis.

3. **Bar Graph of Mean Values**: A bar graph comparing the mean values of key well-being indicators (Life Ladder, Positive affect, Negative affect) by year or country could provide insights into shifts in well-being perception over time or among different countries, providing context to the data.

These visualizations would effectively summarize the data's key insights, making it easier to communicate essential findings and patterns to a broader audience.

## Visualizations
![happiness\scatter_plot.png](happiness\scatter_plot.png)
![happiness\heatmap.png](happiness\heatmap.png)