import dash
from dash import html
from django_plotly_dash import DjangoDash

app = DjangoDash('SimpleExample')  # replaces dash.Dash

app.layout = html.Div([
    html.H1("Django Plotly Dash Example"),
])