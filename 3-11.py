def calculate_change(payment, cost):
    change=payment-cost

    fiftythounsand=50000
    tenthousand=10000
    fivethousand=5000
    onethousand=1000

    fiftythounsandcount=change//fiftythounsand
    change=change%fiftythounsand

    tenthousandcount=change//tenthousand
    change=change%tenthousand

    fivethousandcount=change//fivethousand
    change=change%fivethousand

    onethousandcount=change//onethousand

    print("50000원 지폐:%d장"%(fiftythounsandcount))
    print("10000원 지폐:%d장" % (tenthousandcount))
    print("5000원 지폐:%d장" % (fivethousandcount))
    print("1000원 지폐:%d장" % (onethousandcount))


calculate_change(100000,33000)
print()
calculate_change(500000,378000)







