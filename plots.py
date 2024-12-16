import pandas as pd
import plotly.graph_objects as go

# Load the dataset
file_path = 'C:\\Users\\vinay\\Downloads\\archive\\cleaned_dataset\\metadata.csv'  # Update with your file's path
df = pd.read_csv(file_path)

# Clean and convert data
df['Re'] = pd.to_numeric(df['Re'], errors='coerce')
df['Rct'] = pd.to_numeric(df['Rct'], errors='coerce')
df_cleaned = df.dropna(subset=['Re', 'Rct'], how='all')
df_cleaned_sorted = df_cleaned.sort_values(by='test_id')

# Create Plotly graph
fig = go.Figure()

# Add Re line plot
fig.add_trace(go.Scatter(x=df_cleaned_sorted['test_id'],
                         y=df_cleaned_sorted['Re'],
                         mode='lines+markers',
                         name='Re (Electrolyte Resistance)',
                         line=dict(color='blue')))

# Add Rct line plot
fig.add_trace(go.Scatter(x=df_cleaned_sorted['test_id'],
                         y=df_cleaned_sorted['Rct'],
                         mode='lines+markers',
                         name='Rct (Charge Transfer Resistance)',
                         line=dict(color='red')))

# Update layout
fig.update_layout(title='Battery Impedance Parameters Over Aging Cycles',
                  xaxis_title='Test ID (Proxy for Battery Aging Cycles)',
                  yaxis_title='Resistance (Ohms)',
                  template='plotly')

# Show the plot
import plotly.offline as pyo
pyo.init_notebook_mode(connected=True)
pyo.plot(fig, filename='battery_impedance_plot.html', auto_open=True)

