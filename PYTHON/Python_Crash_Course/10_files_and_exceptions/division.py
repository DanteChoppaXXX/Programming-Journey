#!../bin/python3

print("Give me two numbers and I'll divide them.")
print("Enter 'q' to quit the program.")



while True:
    first_number = input("\nEnter first number: ")
    if first_number == 'q':
        break
    second_number = input("\nEnter second number: ")
    if second_number == 'q':
        break
    try:
        answer = float(first_number) / float(second_number)
        print(answer)
    except ZeroDivisionError:
        print("Zero is not divisible")
    