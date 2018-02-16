import pandas as pd

# importing three data frames with multiple lists in the dictionary
df1 = pd.DataFrame({"HPI":[70,80,90,60], "Int_rate": [2,1,2,3], "ENG_GBP": [50,45,45,67]},
                   index = [2001, 2002, 2003, 2004])

df2 = pd.DataFrame({"HPI":[70,80,90,60],"Int_rate": [2,1,2,3],"ENG_GBP": [50,45,45,67]},
                   index = [2005,2006,2007,2008])

# Now merging both data frames above
merge = pd.merge(df1,df2, on = "HPI")
print(merge)


