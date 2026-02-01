#Dictionary BASICS
#no indexing only keys(unordered)(mutable)  #keys can be replicate but it accept only recent value

TEACHER={
    "name":"SAUMYA SINGH",
    "city": "SULTANPUR",
    "age": 25,
    "rollno.": 23
}
print(type(TEACHER))
print(TEACHER["name"])
TEACHER["age"]= 27  #update dictionary
TEACHER["favfood"]= "gulabjamun" #add new key
TEACHER.pop("favfood")
print(TEACHER.keys())
print(TEACHER)

#practice1
#marks dict with 3 sub and add one by one
marks= {}
marks["maths"]= 93
marks["chmistry"]= 93
marks["computer sci."]= 59
print(marks)

