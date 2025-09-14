#creating a File
HISTORY_FILE="history.txt"

#Function1: Show History
def show_history():
    file = open(HISTORY_FILE,"r")
    lines = file.readlines()
    if len(lines)==0:
        print("history not found")
    else:
        for line in reversed(lines):
            print(line)
    file.close()


#Function2: clearing the history
def clear_history():
    file = open(HISTORY_FILE,"w")
    file.write("\n")
    file.close()
    print("history cleared")

#Function3: save to the history
def save_history(equation,result):
    file = open(HISTORY_FILE,"a")
    file.write(equation+"="+str(result)+"\n")
    file.close()

#Function4: Calculator operations
def calculate(user_input):
    parts=user_input.split()

    if len(parts)!=3:
        print("wrong input, use operation like eg: 8 + 8")
        return

    num1=float(parts[0])
    operator=parts[1]
    num2=float(parts[2])

    if operator=="+":
        result=num1+num2
    elif operator=="-":
        result=num1-num2
    elif operator=="*":
        result=num1*num2
    elif operator=="/":
        if num2==0:
            print("division by zero")
            return
        result=num1/num2
    else:
        print("wrong operator")
        return

    if int(result)==result:
        result=int(result)
    print("result="+str(result))

    save_history(user_input,result)


#main function
def main():
    print("Welcome to calculator program with history")

    while True:
        user_input=input("enter equation like (+, -, *, /) or command: history, clear, exit:\n")
        if user_input=="history":
            show_history()
        elif user_input=="clear":
            clear_history()
        elif user_input=="exit":
            print("Have a nice day, Goodbye")
            break
        else:
            calculate(user_input)

main()



