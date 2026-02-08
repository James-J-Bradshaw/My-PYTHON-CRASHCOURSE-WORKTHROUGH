print("Give me two numbers, and I will attempt to divide them.")
print("enter 'q' to quit")
while True:
    first_num = input("\nFirst number: ")
    if first_num == "q":
        break
    second_num = input("\nSecond number: ")
    if second_num == "q":
        break
    try:
        answer = int(first_num) / int(second_num)
    except ZeroDivisionError:
        print("You cannot divide by 0.")
    except ValueError:
        print("you cannot divide letters.")
    else: print(answer)