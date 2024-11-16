import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize=(12, 7))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
    res1 = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    year = range(df["Year"][0], 2050)
    plt.plot(year, res1.intercept + res1.slope*year, color="red")

    # Create second line of best fit
    df2 = df[df["Year"] >= 2000]
    res2 = linregress(df2["Year"], df2["CSIRO Adjusted Sea Level"])
    y = range(2000, 2051)
    plt.plot(y, res2.intercept + res2.slope*y, color = "green")

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

if __name__ == "__main__":
    draw_plot()
