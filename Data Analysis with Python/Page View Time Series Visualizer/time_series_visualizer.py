import matplotlib.pyplot as plt
from numpy.core.fromnumeric import size
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv")
df = df.set_index('date')
df.index = pd.to_datetime(df.index)

# Clean data
df = df[(df["value"] >= df["value"].quantile(0.025))&(df["value"] <= df["value"].quantile(1-0.025))]

def draw_line_plot():
    # Draw line plot
    fig = plt.figure(figsize=(12, 5))
    plt.plot(df.index, df['value'])
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig
draw_line_plot()


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy().reset_index()
    df_bar['year'] = df_bar['date'].dt.year
    df_bar['month'] = df_bar['date'].dt.month_name()
    df_bar = df_bar.groupby(['year','month'])['value'].mean().reset_index()

    # Draw bar plot
    fig, ax = plt.subplots(1, figsize=(10, 6))
    sns.barplot(data=df_bar, x='year', y='value', hue='month')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],title='Months')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig
draw_bar_plot()


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    df_box["month_num"] = df_box["date"].dt.month
    df_box = df_box.sort_values("month_num")
    fig, axes = plt.subplots(1, 2, figsize = (18,5))

    axes[0] = sns.boxplot(x=df_box["year"], y=df_box["value"], ax = axes[0])
    axes[1] = sns.boxplot(x=df_box["month"], y=df_box["value"], ax = axes[1])

    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
draw_box_plot()