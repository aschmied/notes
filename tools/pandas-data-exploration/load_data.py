import pandas as pd

crime_csvs = [

]

def load_and_reshape_police(filename):
    df = pd.read_csv(filename, usecols=['REF_DATE', 'GEO', 'Statistics', 'VALUE'])
    index = (df["Statistics"] == "Police officers per 100,000 population")
    df = df[index]
    df = df.pivot(index='REF_DATE', columns='GEO', values='VALUE')
    df.index.rename('Year', inplace=True)
    return df

police_dfs = [load_and_reshape_police(f) for f in [
    'data/3510007601_databaseLoadingData_NB.csv',
    'data/3510007601_databaseLoadingData_NL.csv',
    'data/3510007601_databaseLoadingData_NS.csv',
    'data/3510007601_databaseLoadingData_ON.csv',
    'data/3510007601_databaseLoadingData_PE.csv',
    'data/3510007601_databaseLoadingData_QC.csv']]

police = pd.concat(police_dfs, axis=1)

def load_and_reshape_crime(filename):
    df = pd.read_csv(filename, usecols=['REF_DATE', 'GEO', 'Statistics', 'VALUE'])
    index = (df["Statistics"] == "Rate per 100,000 population")
    df = df[index]
    df = df.pivot(index='REF_DATE', columns='GEO', values='VALUE')
    df.rename(columns=lambda name: ' '.join(name.split()[0:-1]), inplace=True)
    df.index.rename('Year', inplace=True)
    return df

crime_dfs = [load_and_reshape_crime(f) for f in [
    'data/3510017701_databaseLoadingData_NB.csv',
    'data/3510017701_databaseLoadingData_NL.csv',
    'data/3510017701_databaseLoadingData_NS.csv',
    'data/3510017701_databaseLoadingData_ON.csv',
    'data/3510017701_databaseLoadingData_PE.csv',
    'data/3510017701_databaseLoadingData_QC.csv'
]]

crime = pd.concat(crime_dfs, axis=1)
