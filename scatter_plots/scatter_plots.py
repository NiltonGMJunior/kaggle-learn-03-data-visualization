# Import main libraries.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
print('Setup complete.')

# Loads the candy dataset in a data frame.
candy_filepath = "../data-for-datavis/candy.csv"
candy_data = pd.read_csv(candy_filepath, index_col='id')

# Visualize the head of the dataset.
print(candy_data.head())

# Generates a scatter plot that shows the relation between the ammount of sugar and consumer preference.
plt.figure(figsize=(16,9))
sns.scatterplot(x='sugarpercent', y='winpercent', data=candy_data)
plt.title('Consumer preference with sugar content')
plt.xlabel('Sugar percentual')
plt.ylabel('Consumer rating')
plt.savefig('scatter_plot_sugar_consumer.png')

# Generates a scatter plot with regression line that shows the relation between the ammount of sugar and consumer preference.
plt.figure(figsize=(16,9))
sns.regplot(x='sugarpercent', y='winpercent', data=candy_data)
plt.title('Consumer preference with sugar content')
plt.xlabel('Sugar percentual')
plt.ylabel('Consumer rating')
plt.savefig('reg_plot_sugar_consumer.png')

# Generates a scatter plot that shows the relation between price and consumer preference for chocolate or non-chocolate candy.
plt.figure(figsize=(16,9))
sns.scatterplot(x='pricepercent', y='winpercent', hue='chocolate', data=candy_data)
plt.title('Consumer preference with price')
plt.xlabel('Price percentual')
plt.ylabel('Consumer rating')
plt.savefig('scatter_plot_price_consumer.png')

# Generates a scatter plot with regression lines that shows the relation between price and consumer preference for chocolate or non-chocolate candy.
plt.figure(figsize=(16,9))
sns.lmplot(x='pricepercent', y='winpercent', hue='chocolate', data=candy_data)
plt.title('Consumer preference with price')
plt.xlabel('Price percentual')
plt.ylabel('Consumer rating')
plt.savefig('lm_plot_price_consumer.png')

# Generates a swarm plot that shows the relation between consumer preference for chocolate or non-chocolate candy.
plt.figure(figsize=(16,9))
sns.swarmplot(x='chocolate', y='winpercent', data=candy_data)
plt.title('Consumer preference for chocolate/non-chocolate candy')
plt.ylabel('Consumer rating')
plt.savefig('swarmplot_consumer_chocolate.png')