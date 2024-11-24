#for generating visualilzations
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


# ==================================================================================
# CALLING FUNCTIONS - comment out functions inside run() that you don't want to run
# ==================================================================================

def run():
    med_tech_availability_corr_with_expenditure()
    health_expenditure_p_capita_vs_health_expenditure_as_perc_gdp()
    death_by_country_over_time()
    hospital_stay_length_by_med_tech_avalibility_over_time()
    analyze_weird_expenditure_correlations()


# =============================================
# FUNCTION DEFINITIONS - no need to comment out
# =============================================


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

def health_expenditure_p_capita_vs_health_expenditure_as_perc_gdp():
    df = pd.read_csv('cleaned_datasets/inner_merged.csv')
    correlation_data = df.groupby('code').apply(
        lambda x: x['health_expenditure_as_percent_gdp'].corr(x['expenditure_per_capita'])
    ).reset_index(name='correlation')

    plt.figure(figsize=(10, 6))
    plt.title("Correlation between Expenditure as percent of gdb and Expenditure per Capita by Country")
    sns.barplot(data=correlation_data, y='code', x='correlation', palette='viridis')
    plt.show()

def analyze_weird_expenditure_correlations():
    df = pd.read_csv('cleaned_datasets/inner_merged.csv')
    correlation_data = df.groupby('code').apply(
        lambda x: x['health_expenditure_as_percent_gdp'].corr(x['expenditure_per_capita'])
    ).reset_index(name='correlation')
    weird_countries = correlation_data[correlation_data['correlation'] < 0]['code'].to_list()
    df_subset = df[df['code'].isin(weird_countries)]
    
    plt.rc('figure', figsize=(15, 8))
    fig, (ax1, ax2) = plt.subplots(ncols=2, sharey=False)
    sns.lineplot(data=df_subset, x='year', y='health_expenditure_as_percent_gdp', hue='code',palette='viridis', ax=ax1)
    sns.lineplot(data=df_subset, x='year', y='expenditure_per_capita', hue='code', palette='viridis', ax=ax2)
    plt.show()

#avoidable deaths by country per year
def death_by_country_over_time():
    df = pd.read_csv("cleaned_datasets/inner_merged.csv")
    fig = sns.lineplot(hue = "code",y = "avoidable_deaths",x = "year", palette = "viridis", data = df)
    sns.move_legend(fig, "upper left", bbox_to_anchor=(1, 1))
    plt.show()

#hospital stay length by med tech avalibity
def hospital_stay_length_by_med_tech_avalibility_over_time():
    df = pd.read_csv("cleaned_datasets/inner_merged.csv")
    fig = sns.clustermap(hue = "code",y = "hospital_stay_length", x = "med_tech_availability_p_mil_ppl", palette = "viridis", data =df)
    plt.xticks(range(0,7000,500))
    sns.move_legend(fig, "upper left", bbox_to_anchor=(1, 1))
    plt.show()


# RUNNING MAIN PROGRAM
if __name__ == "__main__":
    run()