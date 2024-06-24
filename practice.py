#Q1. Write a program to print the following using while loop
#a. First 10 Even numbers
'''for i in range(1,21):
	if i%2==0 :
		print(i)'''
'''x=1
y=21
while x<y:
	if x%2==0:
		print(x)
	x+=1'''



#b. First 10 Odd numbers
'''for x in range (1,21):
	if x%2 != 0:
		print(x)'''

'''x=1
	y=21
	while(x<y):
		if x%2!=0:
			print(x)
		x+=1'''	
 
#c. First 10 Natural numbers
'''for x in range (1,11):
	print(x)'''

'''x=1
y=11
while(x<y):
	print(x)
	x+=1'''

#d. First 10 Whole numbers
'''for x in range (0,10):
	print(x)'''

'''x=0
y=9
while(x<=y):
	print(x)
	x+=1'''

#Q2. Write a program to print first 10 integers and their squares using while loop.
'''for x in range (1,11):
	print(x**2)'''

'''x=1
y=10
while(x<=y):
	print(x**2)
	x+=1'''

#Q3. Write for loop statement to print the following series
#10, 20, 30............300
'''for x in range (10,301,10):
	print(x,end=" ")'''

'''x=10
y=300
while(x<=y):
	print(x)
	x+=10'''

#Q4. Write a while loop statement to print the following series 105, 98, 91........7.
'''for x in range (105,7,-7):
	print(x)'''

'''x=105
y=7
while(y<=x):
	print(x)
	x+=-7'''

#Q5. Write a program to print first 10 natural number in reverse order using while loop.
'''for x in range(10,0,-1):
	print(x)'''

#Q6. Write a program to print sum of first 10 Natural numbers.
'''x=0
for i in range(1,11):
	x=x+i
print(x)'''

'''x=1
y=10
z=0
while(x<=y):
	z=z+x
	x+=1
print(z)'''
	


#Q7. Write a program to print sum of first 10 Even numbers.
'''x=0
for i in range(1,20):
	if i%2==0:
		x=x+i
print(x)'''

'''x=1
y=20
z=0
while(x<=y):
	if x%2==0:
		z=z+x
		x+=1
print(z)'''



#Q8. Write a program to print table of a number entered from the user.
'''x=int(input("enter the table:-"))
for i in range(1,11):
	print(x*i)'''

'''x=int(input("entre the number:-"))
a=1
b=10
while(a<=b):
	print(x*a)
	a+=1'''


#Q10. Write a program to check whether a number is prime or not using while loop.
'''x=int(input("entre the number:-"))
for i in x:
	if x%2==0:
		print("even",i)
	else:
		print("not even",i)'''

'''x=int(input("entre the number:- "))
y=0
while x>y:
	y=y+1
	if y%2==0:
		print("even number",y)
	else:
		print("not even number",y)'''


#Q11. Write a program to find the sum of the digits of a number.
'''y=0
x =str(input("write the text:-"))
for i in x :
	y=y+1
print(y)'''


'''x="anshu"
y=0
z=len(x)
while(y<z):
	print(y[x])
	y+=1'''

#Q12 Write a program to find the product of the digits of a number.
'''x=int(input("enter the number:- "))
y=1
for i in x:'''
	


#Q13. Write a program to reverse the number 
'''for i in range(100,1,-1):
	print(i)'''

'''x=100
y=1
while(y<x):
	print(x)
	x+=-1'''

#Q14. Write a program to display the number names of the digits of a number entered by user, 
'''x=str(input("enter the number:- "))
y=len(x)
for i in range (y) :
	print(x[i],i)'''

    

'''x=1234'''





#Q15 Write a program to print the Fibonacci series tillin terms (Accept n from user) using while loop.

#Q16. Write a program to print the factorial of a number accepted from user
#Q17. Write a program to check whether a number is Armstrong or not. (Armstrong number is a number that is 
#equal to the sum of cubes of its digits for example: 153 = 1^3 + 5^3 + 3^3.) D

#Q18. Write a program to add first n terms of the following series using a for loop
#1/1! + 1/2 + 1/3 + ... + 1/n!

#Q19 Write a program to enter the numbers till the user wants and at the end it should display the 
#sum of all the numbers entered.

#Q20. Write a program to enter the numbers till the user enter ZERO and at the end it should display the
#count of positive and negative numbers entered

#Q21. Write a program to find the HCF of two numbers entered from the user.

#Q22. Write a program to convert Decimal to Binary.

#Q23. Write a program to convert Binary to Decimal.

#Q24. Write a program to check whether a number is palindrome or not

# Q25. Write a python program to sum the sequence: 1+1/1!+1/2! + 1/3! + 1/n!

#Q26. Write a program to accept 10 numbers from the user and display it's average 

#Q27. Write a program to accept 10 numbers from the user and display the largest & smallest number number.



#Q28. Write a program to display sum of odd numbers and even numbers separately that fall between two numbers accepted from the user. (including both numbers) using while loop.


#Q29. Write a program to display all the numbers which are divisible by 13 but not by 3 between 100 and 500. (exclusive both numbers)
#Q30. Write a program to print the following series till n terms.
#2,22, 222, 2222___n terms

#Q31. Write a program to print the following series till n terms.
#14 9 16 25 n terms.



#Q32. Write a program to find the sum of the following series(accept values of x and n from user)
#1 + x/1! + x²/2! + ..........x"/n!



#Q33. Write a program to find the sum of following series:
#x + x2/2 + .....x"/n

#Q34. Write a program to find the sum of following series
#1+8+27.............n terms

#Q35. Write a program to find the sum of following series:
#1+2+6+24+120..n terms


#Q36. Write a program to find the sum of following series:
#S=1+4-916-25+36 n terms



#Q37. Write a Program to print all the characters in the string 'PYTHON' using while loop.

#Q38. Write a program to print only odd numbers from the given list using while loop. L = [23, 45, 32, 25, 46, 33, 71, 90]
#Q39. Write a program to print all the factors of a number using for loop.

#Q40. Write a python program to get the following output
'''1--49
2--48
3--47
48--2
49--1'''





#doubt questions:- 
#que ,11,12





















'''1 Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t'''

'''x= Restart
print(x.replace())'''
#2Write a Python program to change a given string to a newly string where the first and last chars have been exchanged.
#x=str(input("write the string:-"))
x= "you are beautiful"
print(x.replace("you","i"))
print(x.replace ("beautiful","honest"))



#3Write a Python program to remove characters that have odd index values in a given string.
X = "Databases"
y=0
while y<len(x):
	if y%2==1:
	y+=1
	continue
print(x)


#4Write a Python program to check whether a string starts with specified characters.
#5Tab Tak aap log ye question solve kro

#new question


#1.  print the hello world 10 times with the help of While loop
'''for i in range(1,11):
	print("hello world")'''

'''x=1
y=10
while x<=y:
	print("hello world")
	x+=1'''


#2.  find the all Number from 50 to 100 that is divisibe of 7 and 9. 
'''for i in range (50,100):
	if i%7==0 and i%9==0 :
		print(i)'''

'''x=50
y=100
while(x<=y):
	if x%7==0 and  x%9==0:
		print(x)
	x+=1'''
#3.  Count the all Number form 30 to 80 that is divisible of 6 and 8
'''y=0
for i in range(30,80):
	if i%6==0 and i%8==0:
		y=y+1
print(y)'''

'''x=30
y=80
z=0
while(x<y):
	if x%6==0 and x%8==0:
		z=z+1
	x+=1
print(z)'''


#4.  Write a python program to count the all even Number from 20 to 40.
'''x=0
for i in range(20,41):
	if i%2==0:
		x=x+1
print(x)'''

'''x=20
y=40
z=0
while(x<=y):
	if x%2==0:
		z=z+1
	x+=1
print(z)'''


#5.  Write a python program to sum the total value from 10 to 20 ?
'''x=0
for i in range(10,21):
	x=x+i
print(x)'''


'''x=10
y=20
z=0
while(x<=y):
	z=z+x
	x+=1
print(z)'''


#6.  write a python program to count the all even and Odd Number from 10 ot 35
'''x=0
for i in range(10,36):
	x=x+1
print(x)'''

'''x=10
y=35
z=0
while(x<=y):
	z=z+1
	x+=1
print(z)'''
    

#7.  write a python Program to show the factorial of Any number according to the help of user input
#8.  find the Average of the first 10 Number with the help of while loop
'''x=0
for i in range(1,11):
	x=x+i
print(x/10)'''

'''x=1
y=10
z=0
while(x<=y):
	z=z+x
	x+=1
print(z/10)'''


#9.  Reverse the Number from 80 to 50 with help of for  and while Loop

'''for i in range(80,49,-1):
	print(i,end=" ")'''

'''x=80
y=50
while(y<=x):
	print(x,end=" ")
	x-=1'''


#10. print your name of alphabet with the help of while loop
'''x="anshu"
y=len(x)
for i in range (y):
	print(x[i])'''

'''x="anshu"
y=len(x)
z=0
while(z<y):
	print(x[z])
	z+=1'''

#11. print the reverse name with the help of while loop.







#12. write a python program to show the square root from 1 to 15
'''for i in range(1,16):
	print(i**2)'''


'''x=1
y=15
while(x<=y):
	print(x**2)
	x+=1'''

#13. wrtie a python program to show the number between 100 to 150 that is divisible of 5 and 9 and 3
'''for i in range(100,151):
	if i%3==0 and i%5==0 and i%9==0:
		print(i)'''

'''x=100
y=150
while(x<=y):
	if x%3==0 and x%5==0 and x%9==0:
		print(x)
	x+=1'''


#14  x = "I want to become a data scientist" find the length of the x without space ?
'''x="I want to become a data scientist"
print(len(x)-x.count(" "))'''


#15  write a python program to print the All odd Number from 1 to 30.
'''for i in range(1,31):
	if i%2!=0:
		print(i)'''

'''x=1
y=30
while(x<=y):
	if x%2!=0:
		print(x)
	x+=1'''


#16  Write a python Program to print the Number from 1 to 10 and skip the Number 5,4 and 3 .
'''for x in range(1,11):
	if x==3 or x==4 or x==5:
		continue
	print(x)'''

'''x=1
y=10
while(x<=y):
	if x==3 or x==4 or x==5 :
		continue
    print(x)
    x+=1'''



#17  write a python program to check the Numeber is divisible of 12 and 10
'''x=int(input("write the number:-"))
if x%12==0 and x%10==0:
	print("yes divisible ")
else:
	print("not divisible")'''


#18  Write a python program to wether a number is divisible by 2 and 3 both.
'''x=int(input("write the number:-"))
if x%2==0 and x%3==0:
	print("yes divisible ")
else:
	print("not divisible")'''


#19  x = "Himachal Pradesh" extract the text given Below
x="Himachal Pradesh"
#20. chal
print(x[4:8])
#21. desh
print(x[12:16])
#22. ma
print(x[2:4])
#23. him
print(x[0:3])
#24. reverse the Text
print(x[-1::-1])
#25. print the all text and step size should be 3
print(x[0:-1:3])
#26. join the first and last text
print(x[0:17:15])
#27. count "t" how many times repeated
print(x.count("t"))
#28. find the index of the space
print(x.find(" "))
#29. convert into a list x = "Jammu and Kashmir"
x = "Jammu and Kashmir"
print(x.split(" "))

#31.  print the value whose name start with a
x = ["apple","air","onion","tiger","egg","ball","bus"]
'''for i in x:
	if i.startswith("a"):
		print(i)'''

#32.  print the name whose name end with e
'''for i in x:
	if i.endswith("e"):
		print(i)'''

#33.  print the name whose length is less than 5
'''for i in x:
	if len(i)<5:
		print(i)'''
#34.  print the name whose name startwith alphabet sound

#35.  Remove air  from the list
'''for i in x:
	if i=="air":
		continue
	print(i,end=",")'''

#36.  convert the list in to string without any seperators
print("que:-36=",' '.join(x))

#37.  insert the value "tanishka" at the place of ball
y=(' '.join(x))
print("que:-37=",y.replace("ball","tanishka"))

#38.  Python program to interchange first and last elements in a list
y=(' '.join(x))
print("que:-37=",y.replace("apple","bus"))

#39.  Python program to swap two elements in a list
#40. Reverse the list
y=''.join(x)
print("que:40=",x[-1::-1])
#41. find the 2nd maximum Number in python
#42. x = [12,45,10,[56,89,[10,100,200,[500,400]]]]
 #   100
  #  400
   # 10
    #89
#43.write a python program to check the amount after the discount 
#if amount is greater than 3000 than give 30% discount x>3000 = 30% dis
#if amount is greater than 2000 than give 15% discount x>2000 = 15% dis
#if amount is less equal to than2000  give 5% discount x<2000 = 5%  dis
'''x=int(input("write the amount:- "))
if x>3000:
	print(x-(x*30/100))
elif x>2000:
	print(x-(x*15/100))
else:
	print(x-(x*5/100))'''



#44.Write a Python program that checks whether a given letter is a vowel or a consonant.
'''x=str(input("write the letter:-"))
for i in x:
	if x== "a"or "e"or"i"or"o"or"u" :
		print("vowal")
	else:
		print("consonant")
	'''

#45print the back counting from 50 to 1 in while loop
'''x=50
y=1
while x>=y:
	print(x)
	x-=1'''

#question:-- 16(continue in while koop),29

x=int(input("write the amount:- "))
if x>6000:
	print(x-(x*40/100))
elif x>4000:
	print(x-(x*30/100))
else:
	print(x-(x*20/100))










