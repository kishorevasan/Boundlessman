import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("./BIGDAAATA.csv")
counts= df.groupby(['year']).count().majors.tolist()


plt.plot(range(2017, 1993, -1), counts)
plt.show()