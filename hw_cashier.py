def calculate_change(bill, paid):
    if paid < bill:
        return bill - paid
    else:
        return paid - bill


bill = float(input("How much is the bill: "))
paid = float(input("How much did the customer pay: "))

if paid < bill:
    print("Customer needs to pay $", calculate_change(bill, paid), "more.")
else:
    print("Your change is $", calculate_change(bill, paid))