import seaborn as sns
import matplotlib.pyplot as plt

# Load the tips dataset
tips = sns.load_dataset('tips')

# Create a scatterplot
sns.scatterplot(x='total_bill', y='tip', data=tips)
plt.show()
