import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 

df = pd.read_csv("cleaned_datasets/main_df.csv")

new = df.groupby('code').mean()
new = new.drop(columns = ['year'])
#print (new)

#ranks by a column
def rank_column(column,ascending):
    rank = new.sort_values(column,ascending = ascending)
    rank = rank.reset_index()
    rank['rank'] = rank.index+1
    mean_col_value = rank[column].mean()
    sd_col = rank[column].std()
    rank = rank[['rank','code',column]]
    return rank, mean_col_value, sd_col

#quality of care rankings 
hos_stay, mean_hos_stay, sd_hos_stay = rank_column('hospital_stay_length',True)

med_ava, mean_med_ava, sd_med_ava = rank_column("med_tech_availability_p_mil_ppl",False)

life_exp, mean_life_exp, sd_ife_exp = rank_column('life_expectancy',False)

nono_death, mean_nono_death, sd_nono_death = rank_column("avoidable_deaths",True)

#weighted average 
#life expentacy has a really low standard deviation meaning that it does not mattter much in calucluation of effectiveness of healthcare 
#where as med tech avaibility and avoidable deaths have a really large standard deviation 
#decided how to weight based on standard deviation as a percent of mean
def weight_averages():
    dfs = [hos_stay,med_ava,life_exp,nono_death]
    columns = ['code','rank']
    df_1 = [hos_stay[columns], med_ava[columns]]
    df_2 = [life_exp[columns],nono_death[columns]]
    rank_df_1 = pd.merge(df_1[0],df_1[1], on = "code", suffixes = ['_hospital_stay_length','_med_tech_availability_p_mil_ppl'])
    rank_df_2 = pd.merge(df_2[0],df_2[1], on = "code", suffixes = ['_life_expectancy','_avoidable_deaths'])
    rank_df = pd.merge(rank_df_1,rank_df_2, on = "code")

    multipliers = {'rank_hospital_stay_length':.25,'rank_med_tech_availability_p_mil_ppl':.3125,'rank_life_expectancy':.125,'rank_avoidable_deaths':.3125}
    rank_df['rank_weighted_sum'] = 0
    for column,multiplier in multipliers.items():
        temp = rank_df[column] * multiplier
        rank_df["rank_weighted_sum"] = rank_df["rank_weighted_sum"] + temp

    return rank_df
        


rank_df = weight_averages()
results_df = rank_df.sort_values("rank_weighted_sum",ascending = True)
results_df = results_df[["code","rank_weighted_sum"]]
results_df = results_df.reset_index(drop = True)

print(results_df)









#expenditure rankings 
#draw corellation between quality ranking and gdp ranking, and capita ranking seperately 
gdp_exp, mean_gdp_exp, sd_gdp_exp = rank_column("health_expenditure_as_percent_gdp",False)

capita_exp, mean_capita_exp, sd_capita_exp = rank_column('expenditure_per_capita',False)