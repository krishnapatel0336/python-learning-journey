#WITH (no need to close file if you use with)

try:

    with open("report.txt","r") as Report:
        Data=Report.read()
        print("FIle Date", Data)

    # reading files
    # 1: read line method
    # READLINE is sequnceal func so after last line you will get empty data only
    with open("Saumya1singh", "r") as f:
        l1= f.readline()
        l2= f.readline()
        l3= f.readline()
        print(l1)
        print(l2)
        print(l3)
    # READLINES FUNCTION:provide all line in form of list

except FileExistsError:
    print("not exist")
    

