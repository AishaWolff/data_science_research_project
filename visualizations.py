#for generating visualilzations
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


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

death_by_country_over_time()
hospital_stay_length_by_med_tech_avalibility_over_time()
plt.show()
