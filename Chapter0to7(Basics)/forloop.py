   
#"for" list touple or string
#for list
food=["cake", "mango","pizza"] 
for item in food:
    print("food love :",item)
#for tuple
DREAMCOMPNIES=("google","microsoft","adoby","aws","tata")
for eachitem in DREAMCOMPNIES:
    print(eachitem)

#range in for loop
#range(start(0), stop, jump{step}(1))

for newitem in range(1,20,3):
    print(newitem)

#practice que 8
for i in range(2,21,2):
    print("table of two", i)
   
#break/loop breakdown
for n in range(1,5):
    if n==6:
        break
#continue/bump  that value
    elif n==2:
        continue
    print(n)
#pass/loop can't be blank so do no write code than use pass
for a in range(1,9):
    pass
  

#q8 is done in class{print even}
#q9 print 1-50 and saumya singh in place of 5 multiplyers 
for num in range(1,50):
    if num%5==0:
        print("saumya singh")
    else:
        print(num)
#q10 
for n in range(1,11):
    sq=n**2
    print(sq)
#q11(done in class{multiplication table})
#q12(print1-10 and skip 7)
for x in range(1,10):
    if x==7:
        continue
    print(x)
    

