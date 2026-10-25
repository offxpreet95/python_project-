#question 1
balance = 10000
attempt = 0
pin = 1234

while attempt <= 2:
    user_pin = int(input("enter pin : "))
    if pin == user_pin:
        print("login successful")
        print("given option: 1)balance 2)deposite 3)withdraw 4)exit")
        while True:
            given_option = int(input("select option : "))
            if given_option == 1:
               print("balance :", balance)
            elif given_option == 2:
              d_a = int(input("enter deposite amount : "))
              balance += d_a
              print("balance : ",balance)
              print("thnakyou for your service")
            elif given_option == 3:
              w_a = int(input("enter withdraw amount : "))
              if w_a > balance:
                 print("insufficient amount")
              elif w_a < balance:
                 balance -= w_a
                 print("balance : ",balance)
                 print("thnakyou for your service")
            elif given_option == 4:
              print("exit")
              print("thnakyou for your service")
              break
            else:
              print("invalid option")
    elif pin != user_pin:
        attempt +=1
        if attempt <=2:  
          print("incorrect pin, try again")
        else: 
          print("card block")

#question 2
students = {"Aman": [85, 90, 78], "Riya": [92, 88, 95], "Zoya": [70, 65, 80]}
for name,marks in students.items():
    avg=sum(marks)/len(marks)
    print(name,round(avg,2))
for name,marks in students.items():
    avg=sum(marks)/len(marks)
    if avg >=85:
        grade="A"
    elif avg>=70:
        grade="B"
    elif avg>=50:
        grade="C"
    else:
        grade="F"
    print(name,round(avg,2),grade)  
topper=""
highest=0
for name,marks in students.items():
    avg=sum(marks)/len(marks)
    if avg>highest:
        highest=avg 
        topper= name
print("topper : ",topper) 
while True:
    print("1.add student")
    print("2.view all") 
    print("3.show topper")
    print("4.exit")
    ch=int(input("enter choice = "))
    if ch==1:
        Name = input("enter name : ")
        if Name in students:
            print("name already exist")
            continue
        marks=[]
        for i in range(3):
            while True:
                mark=int(input("enter marks : "))
                if mark >=0 and mark <=100:
                    marks.append(mark)
                    break
                else:
                    print("Invalid mark, try again.")
        students[Name]=marks
        print("added succussfully")
    if ch == 2:
        for name,marks in students.items():
            avg=sum(marks)/len(marks)
            if avg >=85:
                grade="A"
            elif avg>+70:
                grade="B"
            elif avg>=50:
                grade="C"
            else:
                grade="F"
            print(name,round(avg,2),grade)
    if ch==3:
        topper=""
        highest=0
        for name,marks in students.items():
            avg=sum(marks)/len(marks)
            if avg>highest:
                highest=avg 
                topper= name
        print("Topper : ",topper)
    if ch==4:
        print("Goodbye!")
        break