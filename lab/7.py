#Enter the following details of a student at run time: - Name, Roll number and marks secured for Mathematics Examination out of 100. Write a python script to display student details as shown:
#Name:
#Roll Number:
#Marks:
#Grade Point:
#Remark:

name=input("ENTER UR NAME : ")
roll=input('ENTER UR ROLL NO : ')
marks=int(input("ENTER UR MARKS : "))
print("UR NAME IS : ",name)
print("UR ROLL NO IS : ",roll)
print("UR MARKS : ",marks)
if marks>=90:
    print("GRADE POINT : 10")
    print("REMARK : EXCELLENT")
elif marks>=80:
    print("GRADE POINT : 9")
    print("REMARK : VERY GOOD")
elif marks>=70:
    print("GRADE POINT : 8")
    print("REMARK : GOOD")
elif marks>=60:
    print("GRADE POINT : 7")
    print("REMARK : AVERAGE")
elif marks>=50:
    print("GRADE POINT : 6")
    print("REMARK : PASS")
