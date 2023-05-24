import string


#Type of pass, and validation test.
def pass_type():
    try:
        type = int(input("Select the type of pass that you want: \n 1- (ABCDEFGHIJKLMNOPQRSTUVWXYZ) \n 2- (abcdefghijklmnopqrstuvwxyz) \n 3- (12345678910)"))
    except ValueError:
        print("Invalid answer type, use a number between 1 and 3")


#Password Length Check.        
while True:
    try:
        num = int(input("Put the password length: "))
    except ValueError:
        print("Invalid password length, please put a number \n")
        continue

