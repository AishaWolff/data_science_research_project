#for generating visualilzations
import seaborn as sns
import pandas as pd 
import matplotlib.pyplot as plt

def med_tech_availability_corr_with_expenditure():
    df = pd.read_csv('cleaned_datasets/inner_merged.csv')
    # get average over all years by country
    correlation_data = df.groupby('code').apply(
        lambda x: x['med_tech_availability_p_mil_ppl'].corr(x['expenditure_per_capita'])
    ).reset_index(name='correlation')

    plt.figure(figsize=(10, 6))
    plt.title("Correlation between Med Tech Availability and Expenditure per Capita by Country")
    sns.barplot(data=correlation_data, y='code', x='correlation', palette='viridis')
    plt.show()


if __name__ == "__main__":
    med_tech_availability_corr_with_expenditure()
