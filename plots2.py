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

# ------------------ Add Filtering Logic Here ------------------ #
# Remove invalid data points (e.g., very large or negative values)
df_filtered = df_cleaned_sorted[(df_cleaned_sorted['Re'] > 0) & (df_cleaned_sorted['Re'] < 1000)]
df_filtered = df_filtered[(df_filtered['Rct'] > 0) & (df_filtered['Rct'] < 1000)]
# ------------------------------------------------------------- #

# Check the cleaned data ranges (Optional)
print(df_filtered.describe())

# Create Plotly graph
fig_cleaned = go.Figure()

# Add Re line plot
fig_cleaned.add_trace(go.Scatter(x=df_filtered['test_id'],
                                 y=df_filtered['Re'],
                                 mode='lines+markers',
                                 name='Re (Electrolyte Resistance)',
                                 line=dict(color='blue')))

# Add Rct line plot
fig_cleaned.add_trace(go.Scatter(x=df_filtered['test_id'],
                                 y=df_filtered['Rct'],
                                 mode='lines+markers',
                                 name='Rct (Charge Transfer Resistance)',
                                 line=dict(color='red')))

# Update layout
fig_cleaned.update_layout(title='Battery Impedance Parameters Over Aging Cycles (Filtered)',
                          xaxis_title='Test ID (Proxy for Battery Aging Cycles)',
                          yaxis_title='Resistance (Ohms)',
                          template='plotly')

# Show the plot
import plotly.offline as pyo
pyo.init_notebook_mode(connected=True)
pyo.plot(fig_cleaned, filename='battery_impedance_plot_filtered.html', auto_open=True)
