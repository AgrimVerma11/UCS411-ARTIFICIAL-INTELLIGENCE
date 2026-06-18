def compound_interest(principal, rate, time):
    amount = principal * (1 + rate / 100) ** time
    return amount - principal

p = float(input("Enter principal amount: "))
r = float(input("Enter interest rate: "))
t = float(input("Enter time (years): "))

print("Compound interest =", compound_interest(p, r, t))
