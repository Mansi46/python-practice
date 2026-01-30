print("Hello GitHub")
print("My first Python program")

#---------------
#Variables
name="Mansi"
age=19
is_student=True
height=5.2

print(name)
print(age)
print(is_student)
print(height)

#-----------------
#Data Types
print(type(name))
print(type(age))
print(type(is_student))
print(type(height))

#----------------
#Operators
a=10
b=3

print("Addition", a + b)
print("Subtract", a - b)
print("Multiplication", a * b)
print("Divide", a / b)
print("Modulus", a % b)

#------------------------
#User Input (basic)
user_name=input("Enter your name:")
print("Welcome", user_name)

#--------------------
#Practice
#Even/odd
num=26
if num%2==0:
  print("number is even")
else:
  print("number is odd")

#Pass/fail
marks=47
if marks>=35:
  print("passs")
else:
  print("fail")

#Positive/negative
num=int(input("Enter a number:"))
if num>0:
  print("Positive")
elif num<0:
  print("Negative")
else:
  print("zero")

#Grade calculator
marks=int(input("Enter marks"))
if marks>=90:
  print("Grade A")
elif marks>=75:
  print("Grade B")
elif marks>=50:
  print("Grade C")
elif marks>=45:
  print ("pass")
else:
  print("fail")

#Eligible for scholarship (and)
marks=int(input("Enter marks"))
attendance=int(input("Enter attendance"))
if marks>=80 and attendance>=75:
  print("Eligible for scholarship")
else:
  print("Not eligible")

#Allowed to enter exam (or)
id_card=int(input("enter id"))
admit_card=int(input("enter admit"))
if id_card==1 or admit_card==1:
  print("allowed")
else:
  print("not allowed")

#Login system(not)
password=input("enter passsword:")
if not password:
  print("not allowed")
else:
  print("alloweed")

#-----------------------
#Nested if-else
#Syntax
if condition1:
  if condition2:
    statement
  else:
    statement
else:
   statement


#Vote eligibility + nationality
age=int(input("Enter age"))
if age>=18:
  nationality=input("Enter nationality")
if nationality=="Indian":
  print("Eligible to vote")
else:
  print("Only Indian citizens can vote")
else:
  print("Not eligible due to age")

#number cheeck
num=int(input("Enter number:"))
if num>0:
  if num%2==0:
  print("Positive even number")
  else:
  print("Positive odd number")
else:
  print("Number is zero or negative")

#take input from user if number is positive than divide by 3
num=int(input("enter number"))
if num>0:
  if num%3==0:
    print("number is positive & divisible by 3")
 else:
    print("positive but not divisible by 3")
else:
    print("number is zero or negative")

#nested if-else + operator
age=int(input("Enter your age:"))
has_id=int(input("Enter your id:"))
if age>=18:
  if has_id==1:
   print("allowed to enter")
 else:
  print("id required")
else:
  print("not allowed due to age")

#take a marks input from user
marks=int(input("enter marks:"))
if marks>=40:
  if marks>=90:
    print("Grade A")
else:
    if marks>=60:
      print("Grade B")
    else:
      print("Grade C")
    else:
      print("fail")

#take input from user of salary and experience
salary=int(input("enter salary:"))
experience=int(input("enter experience:"))
if salary>=20000:
  if experience>=2:
    print("eligible for promotion")
else:
  print("experience not sufficient")
else:
 print("salary criteria not met")
   







           
           























 






































  



