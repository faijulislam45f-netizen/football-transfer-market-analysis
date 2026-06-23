import pandas as pd
import numpy as np
import plotly.express as px

df = pd.read_csv('transfers_history.csv')

# 1. Top 5 Leagues Bar Chart
top_league = df['to_league'].value_counts().head(5).reset_index()
top_league.columns = ['league', 'count']

fig = px.bar(top_league, x='league', y='count', title='Top 5 Leagues By Players Arrivals', color='count', color_continuous_scale='Viridis')
fig.write_image("top_5_leagues_Arrivals.png")

print("Chart saved as 'top_5_leagues_Arrivals.png'")

# 2. Financial Impact Chart
league_spending = df.groupby('to_league')['fee_eur_m'].sum().sort_values(ascending=False).head(5).reset_index()
fig2 = px.bar(league_spending, x='to_league', y='fee_eur_m', title='Total Spending By League In Million Euro', color='fee_eur_m', 
color_continuous_scale='Bluered')

fig2.write_image('league_spending.png')
print("Financial Chart is Saved as 'league_spending.png'")
