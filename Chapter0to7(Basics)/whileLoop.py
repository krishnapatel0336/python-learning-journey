# while loop and for loop
#print name 100 time
num=1
while num<=3:
    print ("saumya dii")
    num=num+1
print("out of while loop")

#practice question
#print numbers from 1 to 10 by while loop
i=1
while (i<11):
    print(i)
    i+=1
print("que:1 done")
#print no from 10 to 1 while 
i=10
while (i>=1):
    print(i)
    i-=1
print("que:2 done")


#print even num from 1 to 50 by while loop
n= 1
while (n<=50):
    if(n%2 ==0):
        print(n)
    n=n+1

#print sum of first n numbers
n= int(input("enter number: "))
sum=0
while n>=1:
    sum= sum+n
    n= n-1
print("sum= ",sum)
print("n= ",n)


#print the pattern
# * **  *** ****
n=1
while(n<=4):
    print("*"*n)
    n=n+1
print("out of while, and value of n should be 5. is it 5? check : ",n)
#print n saumya
n=1
name= "saumya"
while n<=5:
    print(f"{n}. {name}")
    n=n+1

#table of number
n=int(input("enter no:", ))
i=1
while i<=10:
    print(f"{n}x{i}={n*i}")
    i=i+1
 