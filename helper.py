def state_list(df):
    state_list = df['STATE'].unique().tolist()
    state_list.sort()
    return state_list

def type():
    type = ['GSDP','NSDP','PER CAPITA NSDP']
    return type
   
def get_dataframe(df,state, column_name):
    # Filter the dataframe to only include the rows for the specified state
    state_df = df[df['STATE'] == state]
    state_df = state_df[df.VALUE != 0]
    # Return a new dataframe with only the "YEAR" and specified column
    return state_df[['YEAR', column_name]]

def get_state(df, state):
    state_df = df[df['STATE'] == state]
    state_df = state_df[df.VALUE != 0]
    return state_df

def industry_type():
    indu = ['VALUE ADDED AGRI','VALUE ADDED BANK','VALUE ADDED CONC','VALUE ADDED INDUSTRY','VALUE ADDED MANU', 'VALUE ADDED SERVICE']
    return indu

def year(df):
    year  = df['YEAR'].unique().tolist
    return year


def pop_year(pop_df):
    year = pop_df['year'].unique().tolist
    return year

def get_pop(pop_df, state):
    state_df = pop_df[pop_df['state'] == state]
    state_df = state_df[state_df['value'] != 0]
    return state_df

def pop_state(pop_df):
    state_list = pop_df['state'].unique().tolist()
    state_list.sort()
    return state_list

def pop_type():
    pop = ['State-Wise Total Population', 'Decadal Growth Rate of Population', 'Literacy Rate']
    return pop