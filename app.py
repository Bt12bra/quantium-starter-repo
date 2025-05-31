from dash import Dash, html

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Quantium Dash App"),
    html.P("Dash environment ready!")
])

if __name__ == "__main__":
    app.run(debug=True)
