import plotly.graph_objects as go
import plotly.io
import pandas as pd
import plotly.offline as offline
import chart_studio.plotly as py
import os

if not os.path.exists("images"):
    os.mkdir("images")

df = pd.read_csv("D:\\north\\result.csv")
data1=go.Ohlc(x=df['date'],
                open=df['open'],
                high=df['high'],
                low=df['low'],
                close=df['close'])
fig = go.Figure(data=go.Ohlc(x=df['date'],
                    open=df['open'],
                    high=df['high'],
                    low=df['low'],
                    close=df['close']))
#fig.write_image("images/fig1.png")
fig.show()
url = py.plot(fig, filename='stacked-bar')
print(url)
fig.write_html("images/fig1.html")
