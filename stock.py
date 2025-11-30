prices = {"AAPL": 180, "TSLA": 250, "GOOG": 140, "MSFT": 300}

portfolio = {}
total = 0

while True:
    name = input("Enter stock name (or 'done' to finish): ").upper()
    if name == "DONE":
        break
    
    if name not in prices:
        print("Stock not found!")
        continue

    qty = int(input("Enter quantity: "))
    portfolio[name] = qty

for stock, qty in portfolio.items():
    total += prices[stock] * qty

print("Total Investment:", total)
