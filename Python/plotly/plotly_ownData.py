import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

import pandas as pd

data = pd.DataFrame({'data_1': [1, 2, 4, 5, 7, 2],
                     'data_2': [4, 3, 1, 13, 7, 6],
                     'time': [1, 2, 3, 4, 5, 6]
                     })

#data = [1, 2, 3]
# fig = px.bar(x=legend, y=data)
fig = px.line(x=data['time'], y=data['data_1'], markers=True)
# fig = px.line(x=data2['b'], y=[data2['a']], markers=True)
fig.add_bar(x=data['time'], y=data['data_2'])
fig.write_html("boring_fig.html")
print(data)

# graph = go.Figure(
#     data=go.Bar(
#         x= [0, 1, 2],
#         y=[42, 50, 80]
#     ),
#     layout = go.Layout(title=go.layout.Title(text="Beispiel"))
# )
# graph.show()

fig = dict({
    "layout": {
        "title": {
            "text": "Beispiel"
        }
    },
    "data": [
        {
            "type": "bar",
            "x": [0, 1, 2],
            "y": [42, 50, 80]
        },
        {
            "type": "bar",
            "x": [0, 1, 2],
            "y": [4,5,9]
        }
    ]
})
# Alternative
# graph_fig = go.Figure(fig)
# graph_fig.show()

pio.show(fig)




