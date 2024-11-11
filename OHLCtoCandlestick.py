import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots

# Sample OHLCV Data (replace this with your actual DataFrame)
data = {
    'Date': pd.date_range(start='2024-10-01', periods=30, freq='D'),
    'Open': [100 + i for i in range(30)],
    'High': [102 + i for i in range(30)],
    'Low': [98 + i for i in range(30)],
    'Close': [101 + i for i in range(30)],
    'Volume': [1000 + i * 10 for i in range(30)]
}
df = pd.DataFrame(data)

# Ensure that Date column is in datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Create a candlestick figure
fig = make_subplots(rows=2, cols=1, shared_xaxes=True,
                    vertical_spacing=0.2, subplot_titles=('Candlestick Chart', 'Volume'),
                    row_heights=[0.7, 0.3])

# Add candlestick trace
fig.add_trace(go.Candlestick(
    x=df['Date'],
    open=df['Open'],
    high=df['High'],
    low=df['Low'],
    close=df['Close'],
    name='Candlestick'
), row=1, col=1)

# Add volume trace
fig.add_trace(go.Bar(
    x=df['Date'],
    y=df['Volume'],
    name='Volume',
    marker_color='blue',
    opacity=0.5
), row=2, col=1)

# Update layout for better visualization
fig.update_layout(
    title='OHLC Candlestick Chart with Volume',
    xaxis_title='Date',
    yaxis_title='Price',
    yaxis2_title='Volume',
    xaxis_rangeslider_visible=False,
    template='plotly_dark'
)

# Use renderer='browser' if fig.show() didn't work
fig.show(renderer='browser')
