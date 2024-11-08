"""
Tidying:

Steps:
 - drop any years that aren't in the range 2000 to 2019
 - make sure all column names are lowercase and words are separated by underscores rather than spaces
 - Make dataframe have 1 index column (0-n), 1 countries column, 1 years column, 1+ variable column(s)
 - Each country in the country column will appear several times, same with each year in the year column. This is because for each country, we need one row per year.
    - therefore if there are c countries and y years, there will be c*y rows, where each country will be repeated y times and each year will be repeated c times
    
 - Ex:  (although year would be from 2000-2019 instead of 2008-2019)
    Country | Year | some_variable
    ------------------------------
    Albania | 2008 | 23.4
    Albania | 2009 | 26.2
    Andorra | 2008 | 11.1
    Andorra | 2009 | 10.3
"""
import pandas as pd

def tidy (df):
   #drop all rows not in desried time frame 
   df = df[(df["TIME_PERIOD"] < 2019) & (df["TIME_PERIOD"] > 2000)]
   #rename columns to be lowercase
   all_columns = list(df.columns)
   lower_columns = []
   for column in all_columns:
      lower_columns.append(column.lower())
   rename_dict = dict(zip(all_columns,lower_columns))
   df = df.rename(columns = rename_dict)
   



   


    
   return df

#read in file from orginal_datasets folder
df= pd.read_csv("original_datasets/healthcare_quality_and_outcomes.csv")
#print(df.columns)
df = tidy(df)
#print(df.head)
