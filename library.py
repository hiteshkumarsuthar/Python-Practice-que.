import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Sales": [10000, 15000, 12000, 18000, 22000]
})

sns.barplot(data=df, x="Month", y="Sales", color="steelblue")

plt.title("Monthly Sales")
plt.show()


import matplotlib.pyplot as plt

x = [2, 4, 6, 8]
y = [15, 20, 25, 30]

plt.plot(x, y)
plt.xlabel("-axis")
plt.ylabel("Y-axis")
plt.title("Simple Line Graph")
plt.show()
