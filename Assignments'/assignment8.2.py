#practice4
#login
def login(username,password):
    print(f" name={username}, pass={password}")
login("saumya1singh",1234)
#practice5
score=100 #globle keyword
def check_score():
    score=50
    print(f"inside func:{score}")
print(f"outside the func:(before call):{score}")
check_score()
print(f"outside the func:(after call):{score}")
#practice6
count=10
def update_count():
    global count
    count=25
    print(f"in func:{count}")
print(f"out before call:{count}")
update_count()
print(f"out after call:{count}")
