import pandas as pd
df = pd.DataFrame({'hello': ["abc","def","hij","klm","nop"], 'world': [1,2,3,4,5]})
print(df)
df.to_csv('example1.csv',index=False,sep=" ")

