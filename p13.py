import pandas as pd
#create a first Datafram
df1=pd.DataFrame({'Name':['Tommy','Fury'],'age':[20,21]},index=[1,2])
#create second Datafram
df2=pd.DataFrame({'Name':['Jake','Paul'],'age':[22,3]},index=[3,4])
print(pd.concat([df1,df2])) 
#
