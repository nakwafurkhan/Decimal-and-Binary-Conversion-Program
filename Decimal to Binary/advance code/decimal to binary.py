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
                a = int(a)
                is_negative = a < 0  # Check if the number is negative
                a = abs(a)  # Work with the absolute value of the number
                c = ""
                while a > 0:
                    remainder = a % 2
                    c = str(remainder) + c
                    a = a // 2
                if c == "":
                    c = "0"
                if is_negative:
                    c = "-" + c  # Add a negative sign if the original number was negative
                print(c)

    elif x == "b" or x == "B":
        while True:
            print("Binary number")
            b = input("enter number or exit: ")
            if b == "exit":
                break
            else:
                is_negative = b[0] == '-'  # Check if the binary number is negative
                if is_negative:
                    b = b[1:]  # Remove the negative sign for calculation

                b1 = b[::-1]
                power = 0
                d_number = 0
                for i in b1:
                    d_number = d_number + (int(i) * (2 ** power))
                    power += 1

                if is_negative:
                    d_number = -d_number  # Restore the negative sign

                print(d_number)

    else:
        print("Invalid input. Please enter 'D', 'B', or 'exit'.")
