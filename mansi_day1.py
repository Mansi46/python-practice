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

#---------------------------------------
#checking number is even or odd
num=54
if num%2==0:
  print("number is even")
else:
  print("number is odd")

#greater number
a=49
b=35
if a>b:
  print("number is greater")
else:
print("number is smaller")

#check number is negative, positive or zero
num=79
if num>0:
  print ("positive number")
elif num<0:
   print("negative number")
else:
  print("zero")

#grade system(nested if-else)
marks=86
if marks>=90:
        print("Grade A")
  elif marks>=75:
    if marks>=85:
      print("Grade A")
    else:
      print("Grade B")
elif marks>=50:
   print("Grade C")
else:
print("Fail")

#login system
username=input("Enter username:")
password=input("Enter password:")
if username=="admin":
  if password=="1234":
    print("login successful")
 else:
  print("wrong password")
else:
  print("invalid username")

#----------------------------
#loops
#while loop (till the condition will True the code will repeat)
#syntax
while condition:
  statement

#Print 1 to 5
i=1
while i<=5:
  print(i)
  i=i+1

#print 1 to 10
i=1
while i<=10:
  print(i)
  i=i+1

#reverse counting 1 to 10
i=10
while i>=1:
  print(i)
  i=i-1

#print even and odd numbers 1 to 20
i=1
while i<=20:
  if i%2==0:
    print(i, "number is even")
else:
 print(i, "number is odd")
i=i+1
#Print only odd numbers 21 to 50
i=21
while i<=50:
  if i%2==1:
    print(i, "number is odd")
    i=i+1

#table of 5
i=1
while i<=10:
  print(5*i)
i=i+1
# in format
i=1
while i<=10:
  print(5x","=", 5*i)
i=i+1

#table of 7
i=1
while i<=10:
  print("7x",i,"=", 7*i)
i=i+1

#table of 9 in reverse order
i=10
while i>=1:
  print("9x",i,"=", 9*i)
i=i-1

#print table 1 to 5
i=1
while i<=10:
  print("1x",i,"=", 1*i)
  print("2x",i,"=", 2*i)
  print("3x",i,"=", 3*i)
  print("4x",i,"=", 4*i)
  print("5x",i,"=", 5*i)
i=i+1

#take input from user and print table 2 to 10
n=int(input("enter table:"))
i=1
while i<=10:
  print(n,"x",i,"=", n*i)
i=i+1  



#----------------------------------
#for loop("when we know the how many times the loop will run")
#syntax
for i in range(start, end):
  statement

#print 1 to 5
for i in range(1, 6):
  print(i)

#print reverse (5 to 1)
for i in range(5, 0, -1):
  print(i)

#print table of 6
for i in range (1, 11):
  print("6x",i,"=", 6*i)

#print 1 to 10
for i in range(1, 11):
     print(i)

#print even number 1 to 10 from for loop
for i in range(1, 11):
  if i%2==0:
   print (i)




















































































   







           
           























 






































  






