bill = float(input("total bill amount? "))
service = input("Level of service? "
"(Enter Good, Fair, or Bad) ")
people = int(input("split how many ways "))


def getTip(bill, service, people):
    if service == 'good':
        tip = bill * 0.20
        total = bill + tip
        individual = total / people
    
    elif service == 'fair':
        tip = bill * 0.15
        total = bill + tip
        individual = total / people
    
    elif service =='bad':
        tip = bill * 0.10
        total = bill * tip
        individual = total / people

    fIndividual = "${:,.2f}".format(individual)
    fTip = "${:,.2f}".format(tip)
    fTotal = "${:,.2f}".format(total)
    print(f"Tip amount: {fTip}")
    print(f"Total amount:{fTotal}")
    print(f"Price per person:{fIndividual}")

getTip(bill, service, people)

