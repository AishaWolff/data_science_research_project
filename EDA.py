# Merging the Data

# import pandas as pd

# # load all the necessary datasets
# health_exp = pd.read_csv("cleaned_datasets/healthcare_expenditure_worldbank.csv")
# med_tech = pd.read_csv("cleaned_datasets/medical_tech_availability.csv")
# expenditure_p_gdp = pd.read_csv("cleaned_datasets/filtered_health_expenditure_as_percent_gdp.csv")
# len_stay = pd.read_csv("cleaned_datasets/hospital_stay_length.csv")
# av_mortality = pd.read_csv("cleaned_datasets/avoidable_mortality.csv")
# life_expec = pd.read_csv("cleaned_datasets/life_expectancy.csv")

# # inner mege all the necessary datasets by (country, year)
# inner_merged = health_exp.merge(life_expec, on=['code', 'year'], how='inner') \
#                   .merge(av_mortality, on=['code', 'year'], how='inner') \
#                   .merge(len_stay, on=['code', 'year'], how='inner') \
#                   .merge(expenditure_p_gdp, on=['code', 'year'], how='inner') \
#                  .merge(med_tech, on=['code', 'year'], how='inner')
# inner_merged     


# #aggreagte hospital length stay and med tech availability by mean for each (country, year)
# aggregated = inner_merged.groupby(['code', 'year'], as_index=True).agg({
#     'hospital_stay_length': 'mean',  
#     'med_tech_availability_p_mil_ppl': 'mean',
#     'expenditure_per_capita': 'first' ,       
#     'life_expectancy': 'first' ,
#     'avoidable_deaths': 'first' ,
#     'health_expenditure_as_percent_gdp': 'first' 
# })

# #store the merged dataset in inner_final
# inner_final = aggregated.reset_index()

# #uncomment to turn it into a csv file
# #inner_final.to_csv('cleaned_datasets/inner_merged.csv')
