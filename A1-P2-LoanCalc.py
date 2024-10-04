
def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    #print name
    print("\nWeekly Loan Calculator\n")

    #input for a (amount borrowed)
    A = float(input("Enter the amount of the loan: "))

    #input for r (interest)
    r = float(input("Enter the interest rate (%): "))

    #input for n (years)
    n = float(input("Enter the number of years: "))

    #math r/5200 = i
    i = (r / 5200)

    #math weekly pay =  (i/1-(1+i) to the power of -52*n) * a
    weekly = (i/(1-(1+i)**(-52*n)))*A

    #print weekly 
    print("\nYour weekly payment will be: ${0:.2f}\n".format(weekly))


    # YOUR CODE ENDS HERE

main()