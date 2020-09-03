import pandas as pd


def remove_duplicates(df):
    df=df.drop([128,133,129,132,130,131])
    return df
            
    pass
   


def impute_male_and_female_population(df):
    male_null_list= df[df['Male'].isnull()].index.tolist()
    for i in male_null_list:
        df['Male'][i]= df['Population'][i]-df['Female'][i]
    
    female_null_list = df[df['Female'].isnull()].index.tolist()
    for i in female_null_list:
        df['Female'][i]= df['Population'][i]-df['Male'][i]
    return df
    pass


def impute_male_and_female_literacy_rate(df):
    mallit_null_list = df[df['Male_Literacy_Rate'].isnull()].index.tolist()
    for i in mallit_null_list:
        df['Male_Literacy_Rate'][i]= round(((df['Male_Literate'][i]/df['Male'][i])*100),2)
        
    femallit_null_list = df[df['Female_Literacy_Rate'].isnull()].index.tolist()
    for i in femallit_null_list:
        df['Female_Literacy_Rate'][i]= round(((df['Female_Literate'][i]/df['Female'][i])*100),2)
    return df
    pass


def transform_state_names(df):
    state_list= df.iloc[:,2].values
    for id,val in enumerate(state_list):
        if(val=='JAMMU & KASHMIR'):
            df['State name'][id]= 'JAMMU AND KASHMIR'
        if(val=='PUDUCHERRY'):
            df['State name'][id]= 'PONDICHERRY'
        if(val== 'ANDAMAN & NICOBAR ISLANDS'):
            df['State name'][id]= 'ANDAMAN AND NICOBAR ISLANDS'
        if(val== 'DAMAN & DIU'):
            df['State name'][id]= 'DAMAN AND DIU'
        if(val== 'ODISHA'):
            df['State name'][id]= 'ORISSA'
        else:
            continue
    return df
    pass


def classify_population_into_tier(df):
    df['tier'] = ""
    
    pop_list = df.iloc[:,4].values
    for id,val in enumerate(pop_list):
        if(val>=100000):
            df['tier'][id]= 'Tier-1'
        elif(val>=50000 and val<=99999):
            df['tier'][id]= 'Tier-2'
        elif(val>=20000 and val<=49999):
            df['tier'][id]= 'Tier-3'
        elif(val>=10000 and val<=19999):
            df['tier'][id]= 'Tier-4'
        elif(val>=5000 and val<=9999):
            df['tier'][id]= 'Tier-5'
        else:
            df['tier'][id]= 'Tier-6'
    return df
    pass
if __name__ == "__main__":
    df = pd.read_csv('india_census_2011_sample_1.csv')

    q1_df = remove_duplicates(df.copy())
    print(df.shape[0] - q1_df.shape[0])

    q2_df = impute_male_and_female_population(q1_df.copy())
    print(q2_df["Male"].values.tolist())
    print(q2_df["Female"].values.tolist())

    q3_df = impute_male_and_female_literacy_rate(q2_df.copy())
    print(q3_df["Male_Literacy_Rate"].values.tolist())
    print(q3_df["Female_Literacy_Rate"].values.tolist())

    q4_df = transform_state_names(q3_df.copy())
    print(q4_df["State name"].values.tolist())

    q5_df = classify_population_into_tier(q4_df.copy())
    print(q5_df["tier"].values.tolist())