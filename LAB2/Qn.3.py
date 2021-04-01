#Price of  house is $1M. if buyer has good credit, they need to put down 10% otherwise
# they need to put down 20% .print down the payment.
price = 1000000
has_good_credit= True

if has_good_credit:
    down_payment= 0.1*price
else:
    down_payment= 0.2*price
print(f"The down payment is:${down_payment}")

