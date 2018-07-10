import re
def validate(s):
    flag = 0
    while(True):
        if (len(s)<6 and len(s)>12):
            flag = -1
            reak
        elif not re.search("[a-z]", s):
            flag = -1
            break
        elif not re.search("[A-Z]", s):
            flag = -1
            break
        elif not re.search("[0-9]", s):
            flag = -1
            break
        elif not re.search("[#@$]", s):
            flag = -1
            break
        elif re.search("\s", password):
            flag = -1
            break
        else:
            flag = 0
            print("Valid")
            break
    if flag == -1:
        print("Invalid")

def main():
    s = input()
    validate(s)
if __name__ == "__main__":
    main()