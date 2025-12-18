import numpy as np

Students=np.array(["Areeb","Affan","Hassan","Ahmed"])
Subject=np.array(["English","Urdu","JS","C+"])
marks=np.array([[22,57,70,80],
                [90,70,65,46],
                [78,70,40,50],
                [70,75,65,45]])

avg=np.average(marks,axis=0)
for i in range(0,4):
    print(f"the avgerage marks of {Subject[i]} is {avg[i]}")
print()
print()
sum=np.sum(marks,axis=1)
for i in range(0,4):
    print(f"the sum  of {Students[i]}  is {sum[i]}")
avg_marks=np.average(marks,axis=1)
grades = np.where(avg >= 80, "A",
         np.where(avg >= 65, "B",
         np.where(avg >= 50, "C", "D")))
status = np.where((grades == "A") | (grades == "B"), "Pass", "Fail")
print()

for j in range(0,4):
    print(f"{Students[j]} has {grades[j]} and thier status is {status[j]}")