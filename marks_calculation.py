import numpy as np
import pandas as pd

Students=np.array(["Areeb","Affan","Hassan","Ahmed"])
Subject=np.array(["English","Urdu","JS","C+"])
rng=np.random.default_rng(42)
marks=rng.integers(30,100,(4,4))
#print(marks)
df=pd.DataFrame(marks, index=Students, columns=Subject)
#print(df)
# avg of subjects

#print(df)
#print("The average of each subject")
#print(df.mean())
avg_sub=df.mean()
#print("The total of each student")
#print(df.sum(axis=1))
#print("The average of each student")
#print(df.mean(axis=1))
  

#new columns
df["Average"]=df.mean(axis=1)
#print(df["Average"])

df["Grade"] = np.where(df["Average"] >= 80, "A",
                np.where(df["Average"] >= 65, "B",
                np.where(df["Average"] >= 50, "C", "D")))
#print(df["Grade"])

df["Status"] =np.where((df["Grade"] == "A") | (df["Grade"] == "B"),"Pass","Fail")
#print(df["Status"])

#questions
print("Top performing student")
top_performer=df["Average"].sort_values(ascending=False)
print(top_performer.head(1))
print("weakest performing student")
weak_performer=df["Average"].sort_values()
print(weak_performer.head(1))
print("easiest subject : ")
print(avg_sub.sort_values(ascending=False).head(1))

print("hardest subject : ")
print(avg_sub.sort_values().head(1))

print(df)