amount = float(input("Enter the purchase amount: "))

if amount >= 5000:
    discount = amount * 0.20
elif amount >= 2000:
    discount = amount * 0.10
elif amount >= 1000:
    discount = amount * 0.05
else:
    discount = 0

print("Discount:", discount)
print("Amount to pay:", amount - discount)
