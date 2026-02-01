file= open("python2.txt", "r")
data= file.read()
print("DATA of the file is: ", data)
#file close iks necessery 
file.close()


# PRACTICE QUESTION
# write a program to read a text from a given file 
# certificate.txt and #find it contains the word live

file= open ("certificate.txt","r")
dataOfFile= file.read()
if "live" in dataOfFile:
    print("yes 'live' word is present in the file")
else:
    print("NO 'live word is not present'")



