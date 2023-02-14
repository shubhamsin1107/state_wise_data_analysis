import pandas as pd

def preprocess(df):
    

    df = pd.melt(df, id_vars=['STATE', 'CATEGORY'], value_vars=['1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997',
       '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006',
       '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015',
       '2016', '2017', '2018', '2019', '2020', '2021', '2022'], var_name='YEAR', value_name='VALUE')
    df['VALUE'].fillna(0, inplace=True)
    df['VALUE'] = df['VALUE'].astype(int)
    df = pd.concat([df, pd.get_dummies(df['CATEGORY'])], axis = 1)
    for i in range(len(df)):
        if df.iloc[i,3] != 0:
            if df.iloc[i,4] == 1:
                df.iloc[i,4] = df.iloc[i,3]
            elif df.iloc[i,5] == 1:
                df.iloc[i,5] = df.iloc[i,3]
            elif df.iloc[i,6] == 1:
                df.iloc[i,6] = df.iloc[i,3]
            elif df.iloc[i,7] == 1:
                df.iloc[i,7] = df.iloc[i,3]
            elif df.iloc[i,8] == 1:
                df.iloc[i,8] = df.iloc[i,3]
            elif df.iloc[i,9] == 1:
                df.iloc[i,9] = df.iloc[i,3]
            elif df.iloc[i,10] == 1:
                df.iloc[i,10] = df.iloc[i,3]
            elif df.iloc[i,11] == 1:
                df.iloc[i,11] = df.iloc[i,3]
            elif df.iloc[i,12] == 1:
                df.iloc[i,12] = df.iloc[i,3]
        if df.iloc[i,3] == 0:
            if df.iloc[i,4] == 1:
                df.iloc[i,4] = df.iloc[i,3]
            elif df.iloc[i,5] == 1:
                df.iloc[i,5] = df.iloc[i,3]
            elif df.iloc[i,6] == 1:
                df.iloc[i,6] = df.iloc[i,3]
            elif df.iloc[i,7] == 1:
                df.iloc[i,7] = df.iloc[i,3]
            elif df.iloc[i,8] == 1:
                df.iloc[i,8] = df.iloc[i,3]
            elif df.iloc[i,9] == 1:
                df.iloc[i,9] = df.iloc[i,3]
            elif df.iloc[i,10] == 1:
                df.iloc[i,10] = df.iloc[i,3]
            elif df.iloc[i,11] == 1:
                df.iloc[i,11] = df.iloc[i,3]
            elif df.iloc[i,12] == 1:
                df.iloc[i,12] = df.iloc[i,3]
    
    df = df.groupby(['STATE','YEAR']).sum().reset_index()
    df['YEAR'].astype(int)
    # df['YEAR'] = pd.to_datetime(df['YEAR'], format='%Y')
    return df

def preprocess1(pop_df):
    pop_df = pd.melt(pop_df,id_vars=['state', 'data'], value_vars=['1951','1961','1971','1981','1991','2001','2011'], var_name='year', value_name='value')
    pop_df['value'].fillna(0, inplace=True)
    pop_df = pd.concat([pop_df, pd.get_dummies(pop_df['data'])], axis = 1)
    df = pop_df
    def replace_values(row):
        if row[3] != 0:
            if row[4] == 1:
                row[4] = row[3]
            elif row[5] == 1:
                row[5] = row[3]
            elif row[6] == 1:
                row[6] = row[3]
            elif row[7] == 1:
                row[7] = row[3]
            elif row[8] == 1:
                row[8] = row[3]
            elif row[9] == 1:
                row[9] = row[3]
        else:
            if row[4] == 1:
                row[4] = row[3]
            elif row[5] == 1:
                row[5] = row[3]
            elif row[6] == 1:
                row[6] = row[3]
            elif row[7] == 1:
                row[7] = row[3]
            elif row[8] == 1:
                row[8] = row[3]
            elif row[9] == 1:
                row[9] = row[3]
        return row

    pop_df = df.apply(replace_values, axis=1)
    pop_df = pop_df.groupby(['state','year']).sum().reset_index()
    pop_df['year'].astype(int)
    return pop_df