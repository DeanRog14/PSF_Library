from datetime import date
import pandas as pd
import numpy as np

'''
Has any sort of math function that we are use relatively often. 
'''

# Creating function so that we calc the cumulative return of the entire df
def compute_df_cumulative(df):
    return (1 + df.drop('date', axis=1)).cumprod() - 1

# Function so that we calculate the cumulative return of a specific column
def compute_col_cumulative(df, col):
    return (1 + df[col]).cumprod() - 1

# Function so that we can calculate the annualized return
def annualized_return(df, col, date1, date2):
    cumulative_return = compute_col_cumulative(df, col)
    # Dates need to be given in this form date(2023, 2, 15)
    difference = date2 - date1
    days = difference.days
    
    return ((1 + cumulative_return) ** (365 / days)) - 1

# Calculates the rolling returns a time period
def compute_rolling_returns(df, time_period, risk_free_rate):
    returns_col = df.columns[1]
    
    days = time_period * 252

    df = df.copy()
    df.set_index('date', inplace=True)

    returns = df[returns_col]
    # Total rolling returns
    rolling_total = (1 + returns).rolling(days).apply(np.prod, raw=True) - 1

    # Annualized return calculation
    rolling_annualized = (1 + rolling_total) ** (252 / days) - 1

    # Annualized volatility calculation
    rolling_volatility = returns.rolling(days).std() * np.sqrt(252)

    # Cumulative return calculation
    cumulative_return = (1 + returns).cumprod() - 1

    # Rolling cumulative return 
    rolling_cumulative_return = (1 + returns).rolling(days).apply(np.prod, raw=True) - 1

    # Rolling Sharpe Ratio
    rolling_sharpe = (rolling_annualized - risk_free_rate) / rolling_volatility
    
    # Returns the values in a dataframe format for simple plotting and use
    return pd.DataFrame({
        'cumulative_return': cumulative_return,
        'rolling_cumulative_return': rolling_cumulative_return,
        'annualized_return': rolling_annualized,
        'rolling_volatility': rolling_volatility,
        'rolling_sharpe': rolling_sharpe
        
    }).reset_index()

def compute_returns(df, risk_free_rate):
    df = pd.DataFrame(df)
    returns_col = df.columns[1]
    
    df = df.copy()
    df.set_index('date', inplace=True)
    returns = df[returns_col]

    # Total cumulative return
    cumulative_return = (1 + returns).cumprod() - 1
    total_return = cumulative_return.iloc[-1]

    # Annualized return over full period
    n_days = len(returns)
    annualized_return = (1 + total_return) ** (252 / n_days) - 1

    # Annualized volatility over full period
    volatility = returns.std() * np.sqrt(252)

    # Sharpe ratio
    sharpe_ratio = (annualized_return - risk_free_rate) / volatility

    return pd.DataFrame({
        'cumulative_return': cumulative_return,
        'annualized_return': [annualized_return] * len(returns),
        'volatility': [volatility] * len(returns),
        'sharpe_ratio': [sharpe_ratio] * len(returns)
    })

# Calculates the z-score for a specified column
def z_score(df, col):
    return (df[col].iloc[-1] - df[col].mean()) / df[col].std()


### These are mainly used when we want to adjust for plotting

# Adds a percent sign to a value
def to_percent(y, _):
    return f'{y:.0f}%'

# Mutiplies by 100, and adds the percent if the value is still small
def increase_percent(y, _):
    return f'{y * 100:.0f}%'

# Adds a percent sign to a value
def to_ratio(y, _):
    return f'{y:.0f}x'