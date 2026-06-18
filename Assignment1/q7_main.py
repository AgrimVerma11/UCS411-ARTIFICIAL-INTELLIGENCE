import interest

p = float(input("Enter principal amount: "))
r = float(input("Enter interest rate: "))
t = float(input("Enter time (years): "))

print("Compound interest =", interest.compound_interest(p, r, t))
