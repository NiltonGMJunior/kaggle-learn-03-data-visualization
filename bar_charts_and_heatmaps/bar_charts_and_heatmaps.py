# Importing main libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
print("Setup complete.")

# Loads IGN data in a dataframe
ign_filepath = "../data-for-datavis/ign_scores.csv"
ign_data = pd.read_csv(ign_filepath, index_col='Platform')

# Summarizes the data and print the dataset
print(ign_data.describe())
print(ign_data)

# Generates a bar plot with the average scores for racing games for each platform
plt.figure(figsize=(16, 9))
plt.title('Racing game average scores per platform')
sns.barplot(x=ign_data['Racing'], y=ign_data.index)
plt.xlabel('Rating')
plt.ylabel('Platform')
plt.savefig('bar_plot_racing.png')

# Generate a heatmap of average scores by genre and platform
plt.figure(figsize=(10, 10))
sns.heatmap(data=ign_data, annot=True)
plt.title('Average game score by platform and genre')
plt.xlabel('Genre')
plt.savefig('heatmap.png')
