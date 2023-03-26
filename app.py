import pandas as pd
import plotly.express as px

# Load data
data_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
column_names = ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"]
data = pd.read_csv(data_url, header=None, names=column_names)

# Create a scatter plot
fig = px.scatter(data, x="sepal_length", y="sepal_width", color="class", title="Iris Dataset: Sepal Length vs. Sepal Width")

# Show the plot
fig.show()
