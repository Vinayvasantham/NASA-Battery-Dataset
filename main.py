import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Step 1: Load the dataset
try:
    df = pd.read_csv("C:\\Users\\vinay\\Downloads\\archive\\cleaned_dataset\\metadata.csv")
except FileNotFoundError:
    print("Error: File not found. Please check the file path.")
    exit()
except pd.errors.EmptyDataError:
    print("Error: The file is empty. Please provide a valid dataset.")
    exit()

# Step 2: Inspect the dataset
if df.empty:
    print("Error: The dataset is empty. Ensure the file contains data.")
    exit()
print(df.head())  # View the first few rows

# Step 3: Filter relevant columns (assume columns are named accordingly)
columns_of_interest = ['Cycle', 'Battery_impedance', 'Re', 'Rct']
missing_columns = [col for col in columns_of_interest if col not in df.columns]
if missing_columns:
    print(f"Error: Missing columns in the dataset: {missing_columns}")
    exit()

# Drop rows with missing values in the relevant columns
data = df[columns_of_interest].dropna()
if data.empty:
    print("Error: No valid data available after dropping rows with missing values.")
    exit()

# Step 4: Plot Battery Impedance over Cycles
fig1 = px.line(data, x='Cycle', y='Battery_impedance',
               title='Battery Impedance vs Cycles',
               labels={'Cycle': 'Charge/Discharge Cycle', 'Battery_impedance': 'Impedance (Ohms)'});
fig1.update_traces(line=dict(color='green'))
fig1.show()

# Step 5: Plot Re and Rct over Cycles
fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=data['Cycle'], y=data['Re'], mode='lines', name='Re (Electrolyte Resistance)', line=dict(color='blue')))
fig2.add_trace(go.Scatter(x=data['Cycle'], y=data['Rct'], mode='lines', name='Rct (Charge Transfer Resistance)', line=dict(color='red')))

fig2.update_layout(title='Re and Rct vs Cycles',
                   xaxis_title='Charge/Discharge Cycle',
                   yaxis_title='Resistance (Ohms)',
                   legend_title='Parameters')
fig2.show()
