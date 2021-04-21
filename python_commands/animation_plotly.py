import numpy as np
import plotly.graph_objects as go

x = np.random.normal(5, 1, 10000)
xm = np.min(x) - 1
xM = np.max(x) + 1
ym = 0
yM = 1

fig = go.Figure()
fig.add_trace(go.Histogram(x=x, nbinsx=50, histnorm="probability"))
fig.add_trace(go.Histogram(x=x, nbinsx=50, histnorm="probability"))
fig.frames = [
    go.Frame(data=[go.Histogram(x=np.random.normal(0.05 * i + 5, 1, 1000))])
    for i in range(101)
]
fig.layout = go.Layout(
    xaxis=dict(range=[xm, xM], autorange=False, zeroline=False),
    yaxis=dict(range=[ym, yM], autorange=False, zeroline=False),
    title_text="Drifting Distribution",
    hovermode="closest",
    updatemenus=[
        dict(
            type="buttons",
            buttons=[
                dict(label="Play", method="animate", args=[None]),
                {
                    "args": [
                        [None],
                        {
                            "frame": {"duration": 0, "redraw": False},
                            "mode": "immediate",
                            "transition": {"duration": 0},
                        },
                    ],
                    "label": "Pause",
                    "method": "animate",
                },
            ],
        )
    ],
)


# Overlay both histograms
fig.update_layout(barmode="overlay")
# Reduce opacity to see both histograms
fig.update_traces(opacity=0.75)

fig.show()

# Same results but formatted differently:
# fig = go.Figure(
# 	data = [go.Histogram(x=x, nbinsx = 50, histnorm = 'probability'),
# 			go.Histogram(x=x, nbinsx = 50, histnorm = 'probability')],

# 	layout=go.Layout(
# 	        xaxis=dict(range=[xm, xM], autorange=False, zeroline=False),
# 	        yaxis=dict(range=[ym, yM], autorange=False, zeroline=False),
# 	        title_text="Drifting Distribution", hovermode="closest",
# 	        updatemenus=[dict(type="buttons",
# 	                          buttons=[dict(label="Play",
# 	                                        method="animate",
# 	                                        args=[None]),

# 	                          {
# 					                "args": [[None], {"frame": {"duration": 0, "redraw": False},
# 					                                  "mode": "immediate",
# 					                                  "transition": {"duration": 0}}],
# 					                "label": "Pause",
# 					                "method": "animate"
# 					            }


# 	                          ])]),
# 	frames = [go.Frame(
# 		data = [go.Histogram(
# 			x=np.random.normal(.05*i+5,1,1000))])
# 		for i in range(101)]
# 	)
