import pandas as pd

lolle = pd.Series([1,3,5,"lol"])
print(lolle)
lolle.index = ["a","b","A","B"]
print(lolle)
print(lolle["A"])
print(lolle.loc["A"])
#Ripetizione DataFrame

dfWow = pd.DataFrame({
    "randomNumbers" : [3,30,300,1,10,100],
    "letters" : ["w","i","j","a","bb","CCC"]
}, index=["a","B","c","D","E","f"])
print(dfWow)

print(dfWow["randomNumbers"])
#Ripasso .loc e .iloc
print(dfWow.loc["B",["randomNumbers","letters"]])
print(dfWow.iloc[1:5,0])
print(dfWow[(dfWow["randomNumbers"] <= 150) & (dfWow["randomNumbers"] >= 10)])

print(dfWow.iloc[:,0].mean())
print(dfWow["randomNumbers"].median())
print(f"Moda della prima colonna : {dfWow.loc[:,"randomNumbers"].mode()}")
#Correlazione e covarianza
data = {
    'X': [4,20,100],
    'Y': [5,10,80]
}
df = pd.DataFrame(data)
print(f"Covatianza fra due array: {df['X'].cov(df['Y'])}")
print(f"Correlazione fra due array: {df["X"].corr(df['Y'])}")