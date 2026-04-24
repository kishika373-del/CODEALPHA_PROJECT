stocks = {"AAPL": 180, "TSLA": 250, "GOOG": 2700}

total = 0

for stock in stocks:
    qty = int(input(f"Enter quantity for {stock}: "))
    total += qty * stocks[stock]

print("Total Investment Value:", total)
