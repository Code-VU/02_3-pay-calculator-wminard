def calculatePay():
    # Implement your solution in between the two comment blocks
    print("calculating pay")
    # This first line is provided for you
    hours = input("Enter Hours: ")
    rate = input("Enter rate of pay in US dollars per hour: ")

    # pay calculation
    # casting both hours and rate to floats in case user inputs decimals for either
    pay = float(hours) * float(rate) 

    # print results of inputs
    print(pay)

    # end assignment


## If you want to test locally before you try to sync
## Open your terminal and run > python payCalculator.py

#Ignore this for now. 
if __name__ == "__main__":
    calculatePay()
