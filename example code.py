price=int(input("enter total price:"))
person=int(input("enter the number of persons:"))
vat =float(input("enter the vat amount:"))
total_payablecharge =price/person+vat
print(f"the total payable fee is:{total_payablecharge}")