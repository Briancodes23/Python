# importing the required module
import pandas as pd

# defining a data dictionary which will contain various information about my website.
#Bounce_rate: meaning the rate at which users visit and leave the website.
Data_web = {'Day':[1,2,3,4,5,6,7], "Visitors": [1000,700,6000,1000,400,350, 300],'Bounce_Rate':[20,20,23,15,10,34,38]}

# converting the dictionary into a pandas dataframe

# declaring a variable df
df = pd.DataFrame(Data_web)

print(df)

# Slicing
# To print the starting two rows only of the data in the dictionary
print df.head(2))