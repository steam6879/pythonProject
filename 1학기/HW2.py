#12221521 임정빈

current = 0             #Default balance

def deposit(d):
    return current + d

def withdraw(w):
    return current - w

def check_balance(c):
    print("Your current balance is ", c, "won")

def error(e):
    print("There is no button like ", e)


while(True):            #Ifinite loop
    key = input("Deposit(d) or withdrawl(w) or balance check(c)? ")

    if key == "q":      #Escape in infinite loop
        break

    elif key == "d":    #Deposit
        d = int(input("How much do you want to deposit? "))
        print("You deposited ", d, "won")
        current = deposit(d)

    elif key == "w":    #Withdrawal
        w = int(input("How much do you want to withdrawal? "))

        if w > current:     #Withdraw more than the current balance
            print("You've withdrawn ", w, "won\nBut you only have ", current, "won")

        else:               #Withdrawal possible
            print("You've withdrawn ", w, "won")
            current = withdraw(w)

    elif key == "c":    #Check the current balance
        check_balance(current)

    else :              #Undefined key entered
        error(key)