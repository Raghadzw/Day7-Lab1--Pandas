import pandas as pd

lst = [1 ,2 , 3]

x = pd.Series(lst) #creat Series

x = pd.Series(lst , index=[11,12,13] ) #change the index

print(x[0:2])#print first and second elements

lst2 = [2 , 3]
y =pd.Series(lst2)

x = x.append(y)
print(x)

x =x.drop_duplicates()
print(x)

Student = {"Name" : ["Sara" , "Noor"] ,
           "ID" : ["111111", "222222"]}
Student1 = pd.DataFrame(Student , columns= ["Name" , "ID"])
print(Student1)
edu = pd.read_csv("C:/Users/ragha/AppData/Roaming/Microsoft/Windows/Network Shortcuts/edu.csv")
#What is the difference between loc and slicing?
#loc us the lables,but slicing use the index
