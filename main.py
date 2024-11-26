import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('sales.csv')
df.info()
# df['UnitPrice'].plot(kind='hist')
# df['Country'].value_counts().plot(kind='pie',autopct='%1.1f%%')
# df['Description'].value_counts().plot(kind='barh')
# df['PaymentMethod'].value_counts().plot(kind='pie',autopct='%1.1f%%')
# df['Category'].value_counts().plot(kind='pie',autopct='%1.1f%%')
df['OrderPriority'].value_counts().plot(kind='pie',autopct='%1.1f%%')
plt.show()