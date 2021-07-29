bill = float(input())
tip = 12
bill_per_person = (bill / 5 ) * (tip / 100 + 1)
print(".2f"%bill_per_person)