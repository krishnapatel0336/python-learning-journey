#STRINGS{DATATYPE}
#WIRRTENABLE IN SINGLE DOUBBLR OR TRIPPLE CODE
str1='hello'
str2="mission placement"
str3='''python cource'''
print(str1 , str2 , str3 )
#string cocatenation
print(str1+str2)
#length of string
print(len(str2))
#indexing(position starting from zero [whole numbers])
print(str2[2]) #strings are immutable{can't change directly}

#que.1 
str4="saumya"
length=len(str4)
print(length)
print(str4[0])
print(str4[5])


#slicing{part of string}:                         #end index excluded but if lowerremoval is blank then [include} 
#generalcase{[a:b or  :b)}but exeption{[a: ]}     #first blank means it's zero
str="saumyadii"
firsthalf= str[0:6]#saumya
upperremoval= str[ :5]#saumy
lowerremoval= str[2: ]#umyadii
print(firsthalf)
print(upperremoval)
print(lowerremoval)

#CONCEPT OF NEGATIVE INDEXING                       #START WITH (-n,-1]

#que 2:      middle 3 and last 2 characters
#M-1
str1="green"
middle3= str1[1:4]
print(middle3)   
last2= str1[3: ]
print(last2)
#M-2[general]
str2= input("Enter value: ")
mid= len(str2)//2 #'//' is devide with removal of remender
output1= str2[mid-1:mid+2]
print(output1)
output2= str2[-2:]
print(output2)


#common strings methods  [.upper .lower .title .find(sub) .replace(old,new) .capitalizer]
str="saumya singh"
print(str.upper())
print(str.lower())
print(str.capitalize())
print(str.title())
print(str.find("my"))#to find index number
print(str.replace("singh" , "_1singh"))
print(str.count("s"))#find occurance

#formatted strings use "f" to use variables in "string" with help of {}
name= "saumya singh"
age =21
print(f"my name is {name} and i am {age} years old.")

#ESCAPE SEQUENCES
#\n new line    #\t tab space   #\\backslash    #\' single quote    #\" double quote
print("hello world")
print("hello\nworld")
print("hello\tworld")