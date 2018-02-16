import pandas as pd
import matplotlib.pyplot as plt
from marplotlib import style
style.use("fivethirtyeight")

# dataframe to show various activities on the website
df = pd.DataFrame({"Day":[1,2,3,4], "Visitors": [200,100,230,300], "Bounce_rate":[20,45,60,10]})

df.set_index("Day", inplace= True)

# Shows graph of data when running the code
df.plot()
plt.show()





