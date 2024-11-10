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


def drop_cols_with_proportion_na(df: pd.DataFrame, proportion: float = 0.9) -> pd.DataFrame:
    """
    Drop any columns in the dataframe that are some proportion or more of NA values
    Parameters:
        df - dataframe to drop columns from
        proportion - minimum proportion (between 0 and 1) of NA values in a column for that column to be dropped
    Returns:
        updated DataFrame
    """
    drop_cols = []
    # collect all columns that have >= proportion NA values
    for col in df.columns:
        proportion_na = df[col].isna().mean()
        if proportion_na >= proportion:
            drop_cols.append(col)
    # drop columns
    df = df.drop(columns=drop_cols)
    return df


def tidy_informational(df, og_country_column="Reference area", og_year_column="TIME_PERIOD", drop_columns=None):

    # drop unneeded columns
    if drop_columns is None:
        drop_columns = ["STRUCTURE", "STRUCTURE_ID", "STRUCTURE_NAME", "ACTION", "REF_AREA", "FREQ", "MEASURE", "UNIT_MEASURE", "FINANCING_SCHEME", "FINANCING_SCHEME_REV", "FUNCTION",
                        "MODE_PROVISION", "PROVIDER", "FACTOR_PROVISION", "ASSET_TYPE", "PRICE_BASE", "Time period", "Observation value", "Base period", "CURRENCY", "UNIT_MULT", "Decimals"]
    df = df.drop(columns=drop_columns)
    # rename unclear columns
    df = df.rename(columns={og_year_column: "year",
                   og_country_column: "country"})

    # drop all rows not in desried time frame
    df = df[(df["year"] < 2019) & (df["year"] > 2000)]

    # rename columns to be lowercase and replace spaces with underscores
    all_columns = list(df.columns)
    lower_columns = []
    for column in all_columns:
        lower_columns.append(column.lower().replace(" ", "_"))
    rename_dict = dict(zip(all_columns, lower_columns))
    df = df.rename(columns=rename_dict)

    # drop columns with at least 90% NA values
    df = drop_cols_with_proportion_na(df, 0.9)

    # drop columns with that have the not applicable in them
    not_app_columns = df.columns[(df == "Not applicable").all()]
    df = df.drop(columns=not_app_columns)

    # drop columns with that have the not application in them
    not_application_columns = df.columns[(df == "Not application").all()]
    df = df.drop(columns=not_application_columns)

    # checking that function successfully changed column names
    assert "country" in df.columns, "no country column found, orginal dataframe columns named differently than expected"
    assert "year" in df.columns, "no year column found, orginal dataframe columns named differently than expected"

    return df


def tidy_numerical(df, new_data_col_name):

    return df


def tidy(
        df: pd.DataFrame, df_title: str, new_data_col_name: str,
        og_country_column: str = "Reference area", og_year_column: str = "TIME_PERIOD", drop_columns: list[str] = None) -> pd.DataFrame:

    df = tidy_informational(df, og_country_column,
                            og_year_column, drop_columns=drop_columns)
    df.to_csv(f'informational_datasets/{df_title}', index=False)
    df = tidy_numerical(df, new_data_col_name)
    df.to_csv(f'cleaned_datasets/{df_title}')


# read in file from orginal_datasets folder
# for testing
if __name__ == "__main__":
    df = pd.read_csv(
        "original_datasets/unfiltered_set_healthcare_capita_outcomes.csv")
    df = tidy(df)
    df.to_csv("testing_datasets/testing.csv", index=False)
    print(df.columns)
