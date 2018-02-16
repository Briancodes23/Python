import pandas as pd

# Joining operation with Pandas
# Removed HPI list from set
df1 = pd.DataFrame({"Low_Tier_HPI": [50,45,67,34], "ENG_GBP": [50,45,45,67]},
                   index = [2001, 2002, 2003, 2004])

df2 = pd.DataFrame({"HPI":[70,80,90,60],"Int_rate": [2,1,2,3],"ENG_GBP": [50,45,45,67]},
                   index = [2001,2003,2005,2007])

# joining the datasets df1 & df2
joined = df1.join(df2)
print joined