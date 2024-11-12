"""
This file is for cleaning, tidying, and analyzing the data. Here is where datasets
will be imported from original_datasets, then fixed up and saved into cleaned_datasets.
Here is where everyone will be writing code for their individual datasets.
"""

import pandas as pd
from analysis import analyze
from tidy import tidy


# ==================================================================================
# CALLING FUNCTIONS - comment out functions inside run() that you don't want to run
# ==================================================================================

def run():
    medical_tech_availability()
    healthcare_expenditure_worldbank()
    life_expectancy_worldbank()
    ICU_beds()
    health_expenditure_as_percent_of_gdb()

# =============================================
# FUNCTION DEFINITIONS - no need to comment out
# =============================================

def medical_tech_availability():
    read_file = "original_datasets/medical_tech_availability.csv"
    df = pd.read_csv(read_file)
    # most of these are duplicate short-version columns
    unnecessary_cols = [
        'STRUCTURE', 'STRUCTURE_ID', 'STRUCTURE_NAME', 'ACTION', 'MEASURE', 'UNIT_MEASURE',
        'STATISTICAL_OPERATION', 'OWNERSHIP_TYPE', 'HEALTH_FUNCTION', 'CARE_TYPE',
        'HEALTH_CARE_PROVIDER', 'Time period', 'Observation value', 'DECIMALS', 'Decimals',
        'OBS_STATUS', 'OBS_STATUS2', 'OBS_STATUS3', 'UNIT_MULT', 'REF_YEAR_PRICE'
    ]
    data_cols_rename_dict = {
        'OBS_VALUE': 'med_tech_availability_p_mil_ppl'
    }
    df_title = "medical_tech_availability"
    df = tidy(df, df_title,
              data_cols_rename_dict, drop_columns=unnecessary_cols)
    analyze(df, df_title)
    print("Dataframe:", df, sep="\n")


def healthcare_expenditure_worldbank():
    df = pd.read_csv("original_datasets/health_expenditure.csv")
    df = df.rename(columns=df.iloc[3]).iloc[4:]
    #drop columns not needed and only years from 2000 to 2019
    columns_to_keep = ['Country Name', 'Country Code'] + \
                  [col for col in df.columns if isinstance(col, float) and col >= 2000.0 and col<=2019]
    df_filtered = df[columns_to_keep]
    
    #change the orientation of the dataframe and add years as observations instead of variables
    df_long = pd.melt(df_filtered, 
                  id_vars=['Country Name', 'Country Code'], 
                  var_name='Year', 
                  value_name='Value')
    
    # convert 'year' column from float to integer
    df_long['Year'] = df_long['Year'].astype(int)
    # change column names
    df_long.columns = ['country', 'code', 'year', 'expenditure_per_capita']
    
   # analyze(df, df_title)
    print("Dataframe:", df, sep="\n")


def life_expectancy_worldbank():
    df = pd.read_csv("original_datasets/life_expectancy.csv")
    df = df.rename(columns=df.iloc[3]).iloc[4:]
    #drop columns not needed and only years from 2000 to 2019
    columns_to_keep = ['Country Name', 'Country Code'] + \
                   [col for col in df.columns if isinstance(col, float) and col >= 2000.0 and col<=2019]
    df_filtered = df[columns_to_keep]
    
    #change the orientation of the dataframe and add years as observations instead of variables
    df_long = pd.melt(df_filtered, 
                  id_vars=['Country Name', 'Country Code'], 
                  var_name='Year', 
                  value_name='Value')
    
    # convert 'year' column from float to integer
    df_long['Year'] = df_long['Year'].astype(int)
    # change column names
    df_long.columns = ['country', 'code', 'year', 'life_expectancy']
    df_title = 'life_expectancy'
    analyze(df, df_title)
    print("Dataframe:", df, sep="\n")
    

def ICU_beds():
    read_file = "original_datasets/ICU_beds.csv"
    df = pd.read_csv(read_file)
    # most of these are duplicate short-version columns
    unnecessary_cols = [
        'STRUCTURE', 'STRUCTURE_ID', 'STRUCTURE_NAME', 'ACTION', 'MEASURE', 'UNIT_MEASURE',
        'STATISTICAL_OPERATION', 'OWNERSHIP_TYPE', 'HEALTH_FUNCTION', 'CARE_TYPE', 'MEDICAL_TECH',
        'HEALTH_CARE_PROVIDER', 'Observation value', 'DECIMALS', 'Decimals',
        'OBS_STATUS', 'OBS_STATUS2', 'OBS_STATUS3', 'UNIT_MULT', 'REF_YEAR_PRICE'
    ]
    data_cols_rename_dict = {
        'OBS_VALUE': 'available_adult_ICU_beds'
    }
    df_title = "ICU_Beds_and_Use"
    df = tidy(df, df_title,
              data_cols_rename_dict, drop_columns=unnecessary_cols)
    analyze(df, df_title)
    print("Dataframe:", df, sep="\n")


def health_expenditure_as_percent_of_gdb():
    read_file = "original_datasets/health_expenditure_as_percent_gdp.csv"
    # cols 40 and 41 are NA for the first large chunk --> pandas must be told their type to not mix up types while reading in df in chunks to save memory
    df = pd.read_csv(read_file, dtype={40:object, 41:object})
    # most of these are duplicate short-version columns
    unnecessary_cols = [
        'STRUCTURE', 'STRUCTURE_ID', 'STRUCTURE_NAME', 'ACTION', 'MEASURE', 'UNIT_MEASURE', 'FREQ',
        'FINANCING_SCHEME', 'PRICE_BASE', 'CURRENCY', 'BASE_PER', 'FUNCTION', 'MODE_PROVISION',
        'FACTOR_PROVISION', 'ASSET_TYPE', 'Time period', 'Observation value', 'DECIMALS',
        'Decimals', 'OBS_STATUS', 'OBS_STATUS2', 'OBS_STATUS3', 'Unit multiplier', 'MODE_PROVISION'
    ]
    data_cols_rename_dict = {
        'OBS_VALUE': 'health_expenditure_as_percent_gdp'
    }
    df_title = "health_expenditure_as_percent_gdp"
    country_col = "Reference area"
    
    # drop unnecessary countries to limit size of df


    print("\n\ncolumns:\n", df.columns, "\n\n\n")
    df = tidy(df, df_title, data_cols_rename_dict, og_country_column=country_col,
              og_year_column="TIME_PERIOD", drop_columns=unnecessary_cols)
    analyze(df, df_title)
    print("Dataframe:", df, sep="\n")


# RUNNING MAIN PROGRAM
if __name__ == "__main__":
    run()    
