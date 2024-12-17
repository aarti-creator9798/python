import pandas as pd
import plotly.graph_objects as go


data = pd.read_csv('path_to_your_downloaded_file.csv')


data = data.dropna(subset=['Battery_impedance', 'Re', 'Rct'])



data['Cycle'] = range(1, len(data) + 1)

# Create a figure
fig = go.Figure()

# Add Battery Impedance plot
fig.add_trace(go.Scatter(x=data['Cycle'], y=data['Battery_impedance'],
                         mode='lines+markers', name='Battery Impedance (Ohms)',
                         line=dict(color='blue')))

# Add Estimated Electrolyte Resistance plot
fig.add_trace(go.Scatter(x=data['Cycle'], y=data['Re'],
                         mode='lines+markers', name='Estimated Electrolyte Resistance (Ohms)',
                         line=dict(color='green')))

# Add Estimated Charge Transfer Resistance plot
fig.add_trace(go.Scatter(x=data['Cycle'], y=data['Rct'],
                         mode='lines+markers', name='Estimated Charge Transfer Resistance (Ohms)',
                         line=dict(color='red')))

# Update layout
fig.update_layout(title='Battery Parameters vs. Cycle Number',
                  xaxis_title='Cycle Number',
                  yaxis_title='Resistance (Ohms)',
                  legend_title='Parameters',
                  template='plotly_white')

# Show the figure
fig.show()
