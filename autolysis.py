import os
import sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import openai

# Set up the AI Proxy
openai.api_base = "http://aiproxy.sanand.workers.dev/openai/v1/chat/completions"
openai.api_key = os.environ["AIPROXY_TOKEN"]  # Set this environment variable before running

def analyze_csv(file_path):
    """
    Analyze the CSV file and generate key insights.
    """
    try:
        # Handle encoding issue (try 'latin1' encoding if needed)
        df = pd.read_csv(file_path, encoding='latin1')
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return None, None, None

    summary = {
        "shape": df.shape,
        "columns": df.columns.tolist(),
        "missing_values": df.isnull().sum().to_dict(),
        "summary_statistics": df.describe(include='all').to_dict()
    }

    # Numeric columns for correlation matrix
    numeric_df = df.select_dtypes(include=['number'])
    correlation_matrix = numeric_df.corr().to_dict() if numeric_df.shape[1] > 1 else None

    return df, summary, correlation_matrix

def ask_llm(summary, correlation_matrix):
    """
    Interact with the LLM to generate narratives and suggestions.
    """
    prompt = f"""
    Analyze the following dataset summary and correlation matrix:
    Summary: {summary}
    Correlation Matrix: {correlation_matrix}
    
    1. Provide a narrative about the data.
    2. Suggest key insights and patterns.
    3. Recommend 1-3 visualizations to best represent the data.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",  # Use the correct model for AI Proxy
            messages=[ 
                {"role": "system", "content": "You are a data analysis assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error interacting with LLM: {e}")
        return "No narrative generated."

def generate_visualizations(df, suggestions, output_dir):
    """
    Create visualizations based on LLM suggestions and save them in the output directory.
    """
    visualizations = []
    try:
        # Select numeric columns for visualizations
        numeric_df = df.select_dtypes(include=['number'])

        # Generate a scatter plot (always generate)
        if len(numeric_df.columns) >= 2:
            plt.figure(figsize=(5.12, 5.12))  # Set the figure size to approximately 512x512 px
            sns.scatterplot(x=numeric_df.columns[0], y=numeric_df.columns[1], data=numeric_df)
            scatter_path = os.path.join(output_dir, "scatter_plot.png")
            plt.savefig(scatter_path, dpi=100)  # Save with 100 DPI for 512x512 px
            visualizations.append(scatter_path)
            plt.close()

        # Generate a heatmap for correlations (always generate if there are enough numeric columns)
        if numeric_df.shape[1] > 1:
            corr = numeric_df.corr()
            plt.figure(figsize=(5.12, 5.12))  # Set the figure size to approximately 512x512 px
            sns.heatmap(corr, annot=True, cmap='coolwarm')
            heatmap_path = os.path.join(output_dir, "heatmap.png")
            plt.savefig(heatmap_path, dpi=100)  # Save with 100 DPI for 512x512 px
            visualizations.append(heatmap_path)
            plt.close()

    except Exception as e:
        print(f"Error generating visualizations: {e}")

    return visualizations

def generate_readme(summary, correlation_matrix, narratives, visualizations, output_dir):
    """
    Generate a README.md file summarizing the analysis.
    """
    readme_path = os.path.join(output_dir, "README.md")
    with open(readme_path, "w") as f:
        # Add header for the file
        f.write("# Dataset Analysis\n")
        f.write("This README provides an analysis of the dataset provided along with key insights, recommendations, and visualizations.\n\n")
        
        # Summary Section
        f.write("## Summary\n")
        f.write(f"Shape of dataset: {summary['shape']}\n\n")
        f.write("### Columns in the dataset\n")
        f.write(f"{', '.join(summary['columns'])}\n\n")
        
        # Missing Values Section
        f.write("### Missing Values\n")
        f.write("Below is the count of missing values per column:\n")
        for column, missing in summary['missing_values'].items():
            f.write(f"- {column}: {missing} missing values\n")
        f.write("\n")
        
        # Summary Statistics Section
        f.write("### Summary Statistics\n")
        f.write("Here are the summary statistics for numeric columns:\n")
        for column, stats in summary['summary_statistics'].items():
            f.write(f"- {column}: {stats}\n")
        f.write("\n")
        
        # Correlation Matrix Section (if exists)
        if correlation_matrix:
            f.write("## Correlation Matrix\n")
            f.write("This section shows the correlations between numeric variables in the dataset:\n")
            for column, correlations in correlation_matrix.items():
                f.write(f"- {column}:\n")
                for other_column, value in correlations.items():
                    f.write(f"  - {other_column}: {value}\n")
            f.write("\n")
        
        # AI-generated Narrative Section
        f.write("## Narrative\n")
        f.write(f"{narratives}\n\n")

        # Visualizations Section
        f.write("## Visualizations\n")
        f.write("Below are the generated visualizations that help in understanding the relationships in the data:\n")
        for vis in visualizations:
            f.write(f"![{vis}]({vis})\n")
        f.write("\n")
        
    print(f"README file generated at: {readme_path}")


def main():
    """
    Main function to handle CSV analysis, LLM interaction, and output generation.
    """
    if len(sys.argv) != 2:
        print("Usage: python autolysis.py <file_path>")
        return

    file_path = sys.argv[1]
    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist.")
        return

    # Create output directory based on the dataset name
    dataset_name = os.path.basename(file_path).split('.')[0]  # Extract file name without extension
    output_dir = os.path.join(dataset_name)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)  # Create the directory if it doesn't exist

    # Analyze the CSV file
    df, summary, correlation_matrix = analyze_csv(file_path)
    if df is None:
        return

    # Ask the LLM for insights
    narratives = ask_llm(summary, correlation_matrix)

    # Generate visualizations based on LLM suggestions (both scatter plot and heatmap)
    visualizations = generate_visualizations(df, narratives, output_dir)

    # Generate a README file summarizing the analysis
    generate_readme(summary, correlation_matrix, narratives, visualizations, output_dir)

    print(f"Analysis complete. Check {output_dir}/README.md and the generated visualizations.")

if __name__ == "__main__":
    main()
