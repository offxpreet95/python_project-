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