import pandas_datareader.data as pdr
import datetime

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

end = datetime.date.today()
start = end - datetime.timedelta(days=365*5)

pd_data = pdr.DataReader('SNE', 'iex', start, end)

print(pd_data)
#pd_data.to_csv("data.csv")


plt.plot(pd_data["close"])
plt.savefig("glaph.png")