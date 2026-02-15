import pandas as pd
import numpy as np
data={
    "name" : ["anjali","yenika","tanishka","aastha","gargi","aysha","anmol","bhasha","yogita","nini"],
    "branch" : ["cseds","cseds","cse","cseds","cse","csit","it","ece","mechanical","ece"],
    "rollnumber" : [4534,3653,2453,7890,3245,2355,1245,3255,5346,6785],
    "tvshow" : ["shinchan","nobita","pikachu","barbie","ben10","marvel","doremon","haddimerabadi","nan","nan"]
}
data2 = {
    "name": ["anjali","yenika","tanishka","aastha","gargi","aysha","anmol","bhasha","yogita","nini"],
    "city": ["Delhi","Mumbai","Kolkata","Chennai","Bangalore","Hyderabad","Pune","Jaipur","Lucknow","Patna"],
    "year_of_birth": [2001,2000,2002,2001,2000,2003,2002,2001,2000,2003]
}
#importing csv or worksheet
data3=pd.read_csv(r"C:\Users\ajha4\OneDrive\Documents\flood_data.csv")
df3=pd.DataFrame(data3)
pd.set_option("display.max_columns", None)   # Show all columns
pd.set_option("display.max_rows", None)      # Show all rows 
pd.set_option("display.width", 1000)         # adjust width
pd.set_option("display.max_colwidth", None)  # full column content
print(df3)
df2=pd.DataFrame(data2)
df2["name"]=df2["name"]+"akgec"
print(data)
print(len(data["name"]))
print(len(data["branch"]))
print(len(data["rollnumber"]))
print(len(data["tvshow"]))
df=pd.DataFrame(data)
P=df.iloc[:11,:4]#rows,column[starting:ending,starting:ending]
print(P)
df=pd.DataFrame(data)
df1=df.loc[0:3,["name","branch"]]
print(df1)
#only column-->df[["col1","col2"]]
#rows+column-->df.loc[row,["col1","col2"]]
#position based-->df.iloc[row_index,column_index]
A=df["name"]
print(A)
df.drop("name",axis=1)
#if u actually want to delete use inplace=True and dont give it a name ie G or something otherwise none will be printed
#for temprory dont write inplace cuz its automatically false
print(df)
#axis=0-->is for rows
#axis=1-->is for column
#J=df.drop(columns=["branch"])
#print(J)
R=df.shape
print(R)
info=df.info()
print(info)
describe=df.describe()
print(describe)
# for mean of one column:
print(df["rollnumber"].mean())
#for max of one columns:
max=df["rollnumber"].max()
print(max)
#broadcasting
df["rollnumber"]=df["rollnumber"]+1000
print(df)
df["name"]=df["name"]+"akgec"
print(df)
#renaming column
#for renaming df.rename(columns={"originalname":"tobechangedinto"},inplace=true)
df.rename(columns={"rollnumber":"salary"},inplace=True)
print(df)
unique=df["branch"].unique()
print(unique)
count=df["branch"].value_counts()
print(count)
df["payment"]=df["salary"].apply(
    lambda i: "high payment" if i>4000
    else "low payment" if i<3000
    else "medium payment"
)
print(df)
null=df.isnull().sum
print(null)
#for droping null value as we have 0 null value then there is nothing to drop
#if u want to drop any one null value then use df.dropna(how="any")
#if u want to drop any column having null value then use df.dropna(how="all")
df.dropna(how="all")
print(df)
def intelligence(row):
    if row["salary"]>3000 and row["salary"]<4000:
        return "good"
    elif row["salary"]>1000 and row["salary"]<3000:
        return "keep trying"
    else:
        return "excellence"
df["intelligence"]=df.apply(intelligence,axis=1)
print(df)
#if we have any null value we can just replace it with 0(noob)
df=df.fillna(0)
print(df)
#now we can also replace it with the mean of the data or we can use max or min anything we want
#df["in which column's null value we want to fill the mean"].fillna(df["the column of which we want the mean value"].mean,inplace=True)
df["salary"].fillna(df["salary"].median(),inplace=True)
print(df)
#even we can use forward value and backward value to replace the nan value just by using (method="bfill"or"ffill")
df["salary"].fillna(method="bfill")
print(df)
#we can use df["edited column"]=df["original column"].replace("original value","to be replaced value") or just use inplace=True
df["name"].replace("niniakgec","monikaakgec",inplace=True)
print(df)
duplicate=df[df.duplicated("branch",keep="last")]
print(duplicate)
#and for droping duplicate value we can just use df.drop_duplicates("branch")
"""joins-->we have left right outer inner merge
left-->if A and B is df then the the data which are not same as B in A will be printed ie no B
right-->data in B which is not equal to A will printed ie no A
outer-->will print all
inner-->only those which is similar in A and B
merge more defined differentiate between same and different"""
concat=pd.concat([df,df2])
print(concat)#to merge
concat1=pd.concat([df,df1],axis=1)
merge=pd.merge(df,df2,on="name")
print(merge)
