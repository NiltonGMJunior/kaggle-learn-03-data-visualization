# Imports main libraries for the script
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
print("Setup complete.")

# Sets the path to the dataset and creates the data frame
museum_path = "../data-for-datavis/museum_visitors.csv"
museum_data = pd.read_csv(museum_path, index_col="Date", parse_dates=True)

# Prints the last five rows of the dataset
print(museum_data.tail())

# Each row gives the number of visitors in each museum in a month

# Prints the number of visitors the Chinese American Museum received in July 2018
ca_musesum_jul18 = museum_data['Chinese American Museum']['2018-07-01']
print("Visitors in the Chinese American Museum on July 2018: {}".format(ca_musesum_jul18))

# Prints the difference in the number of visitors in October 2018 for the Avila Adobe and Firehouse Museum
avila_oct18 = museum_data['Avila Adobe']['2018-10-01'] - \
    museum_data['Firehouse Museum']['2018-10-01']
print("Difference in the number of visitors of the Avila Adobe and Firehouse Museum in October 2018: {}".format(avila_oct18))

# Generates a 14in x 6in figure with the number of visitors over time for each museum
plt.figure(figsize=(14, 6))
sns.lineplot(data=museum_data)
plt.savefig('line_plot_all.png')

# Generates a 14in x 6in figure with the number of visitors over time for the Avila Adobe
plt.figure(figsize=(14, 6))
sns.lineplot(data=museum_data['Avila Adobe'], label='Avila Adobe')
plt.savefig('line_plot_avila_adobe.png')

