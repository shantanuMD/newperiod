from os import system, name

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
period=input("Enter your current period for price : ")
clear()
decision=1
while(decision):
    # clear()
    current=input("Enter Current Price :")
    m=0
    def getSum(n):
        sum = 0
        for digit in str(n):
            sum += int(digit)
        return sum
    m=getSum(current)+1
    #print(m)
     
          print(newperiod+1," : RED")
      else:
          print(newperiod+1,"  : GREEN")
    #input=input("")
    decision+=1
    # decision=input("Do you want to play : Press 1 and 0 to exit \n")
