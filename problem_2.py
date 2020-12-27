date = int(input("Enter date: "))
print("Yo entered - ",date)
if date > 0 and date < 2022:
    if date % 100 == 0:
        print("It is the  ", date // 100, "st century ", sep="")
    else:
        print("It is the  ",date//100+1, "st century ", sep = "")

else:
    print("This date is invalid")