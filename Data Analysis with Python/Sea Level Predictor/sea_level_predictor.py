import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots(figsize = (12,7))
    x = df["Year"]
    y = df["CSIRO Adjusted Sea Level"]
    plt.scatter(x, y)

    # Create first line of best fit
    slope, intercept = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])[0:2]
    m = slope
    b = intercept
    x_pred = pd.Series([i for i in range(1880,2051)])
    y_pred = m*x_pred + b
    plt.plot(x_pred, y_pred, "green")

    # Create second line of best fit
    mod_df = df.loc[df["Year"] >=2000]
    slope2, intercept2 = linregress(mod_df["Year"], mod_df["CSIRO Adjusted Sea Level"])[0:2]
    m2 = slope2
    b2 = intercept2
    x_pred2 = pd.Series([i for i in range(2000,2051)])
    y_pred2 = m2*x_pred2 + b2
    plt.plot(x_pred2, y_pred2, "red")
    

    # Add labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    plt.show()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
