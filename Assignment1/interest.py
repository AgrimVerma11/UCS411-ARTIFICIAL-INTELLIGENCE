def compound_interest(principal, rate, time):
    amount = principal * (1 + rate / 100) ** time
    return amount - principal
