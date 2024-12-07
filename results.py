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
    mean_col_value = rank[column].mean()
    sd_col = rank[column].std()
    print(mean_col_value)
    print(sd_col)
    rank = rank[['code',column]]
    print(rank)

#quality of care rankings 
hos_stay = rank_column('hospital_stay_length',True)

med_ava = rank_column("med_tech_availability_p_mil_ppl",False)

life_exp = rank_column('life_expectancy',False)

nono_death = rank_column("avoidable_deaths",True)


#expenditure rankings 
gdp_exp = rank_column("health_expenditure_as_percent_gdp",False)

capita_exp = rank_column('expenditure_per_capita',False)