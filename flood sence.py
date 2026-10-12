import pandas as pd
import plotly.express as px

df = pd.read_csv("global air pollution dataset.csv")

print(df.head())
print(df.columns)

country_aqi = (
    df.groupby("Country")["AQI Value"]
    .mean()
    .reset_index()
    .sort_values(by="AQI Value", ascending=False)
)

fig = px.bar(
    country_aqi.head(15),
    x="Country",
    y="AQI Value",
    title="Top 15 Countries with Highest Air Quality Index (AQI)",
    labels={
        "AQI Value": "Average AQI",
        "Country": "Country"
    }
)
fig.show()


aqi_category = df["AQI Category"].value_counts().reset_index()
aqi_category.columns = ["AQI category", "Count"]
print(aqi_category.head())
fig = px.pie(
    aqi_category,
    names="AQI category",
    values="Count",
    title="Distribution of AQI categories ",
    hole=0.3
)
fig.show()


fig = px.histogram(
    df,
    x="AQI Value",
    title="AQI Distribution",
    nbins=30
)

fig.show()


fig = px.scatter(
    df, 
    x = "PM2.5 AQI Value",
    y = "AQI Value",
    color = "AQI Category",
    hover_name = "City",
    hover_data = ["Country"],
    title = "PM2.5 and AQI"
)
fig.show()

corr = df[
    [
        "AQI Value",
        "CO AQI Value",
        "Ozone AQI Value",
        "NO2 AQI Value",
        "PM2.5 AQI Value"
    ]
].corr()

fig = px.imshow(
    corr,
    text_auto=True,
    title="AQI and Pollutant Correlation"
)

fig.show()

fig = px.scatter_3d(
    df,
    x="CO AQI Value",
    y="NO2 AQI Value",
    z="PM2.5 AQI Value",
    color="AQI Category",
    hover_name="City",
    title="3D Air Pollution Visualization"
)

fig.show()