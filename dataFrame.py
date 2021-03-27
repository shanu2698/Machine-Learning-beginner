import pandas as pd
from time import sleep as sl


dataset=pd.read_csv("sampledata.csv")
print("xxxxxxxxxxxxxxxxxxx  printing dataset       xxxxxxxxxxxxxxxxxxxxx")
sl(2)
print(dataset)


mydf= pd.DataFrame(dataset)
sl(2)
print("xxxxxxxxxxxxxxxxxxx   printing data frame   xxxxxxxxxxxxxxxxxxxxx")
sl(2)
print(mydf)

print("xxxxxxxxxxxxxxxxxxx            info         xxxxxxxxxxxxxxxxxxxx ")
print(mydf.info())
