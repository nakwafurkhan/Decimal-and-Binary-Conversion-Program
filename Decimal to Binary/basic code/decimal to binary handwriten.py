while True:
    x = input("decimal(D) or binary(B) or exit: ")

    if x == "exit":
        print("Program closed. Bye!")
        break

    elif x == "d" or x == "D":
        while True:
            print("Decimal number")
            a = input("enter number or exit: ")
            if a == "exit":
                break
            else:
                a=int(a)
                c = ""
                while a>0:
                    remender = a%2
                    c = str(remender)+c
                    a = a//2
                print(c)    
    
        
    elif x == "b" or x == "B":
        while True:
            print("Binary number")
            b = input("enter number or exit: ")
            if b == "exit":
                break       
            else:
                b1 = b[:: -1]
                power = 0
                d_number = 0
                for i in b1:
                    d_number = d_number + (int(i)*(2** power))
                    power += 1
        
                print(d_number)
              


        

    else:
        print("Invalid input. Please enter 'D', 'B', or 'exit'.")
