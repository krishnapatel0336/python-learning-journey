#no indexing unordered[unique]{} mutable
food={"paneer", "chole bhature", "sandwitch","golgappe" ,"paneer"}
print(type(food))
food.add("kunafa")
food.remove("paneer")
print(food)

#practice2
#list to set
programminglist=["java", "python", "c++" , "C" ,"java"]
programmingset=set(programminglist)
print(type(programmingset))
print("number of langauges", len(programmingset))
print(programmingset)