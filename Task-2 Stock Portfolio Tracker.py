# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 135,
    "AMZN": 125,
    "MSFT": 310
}

portfolio = {}

print("Welcome to the Stock Portfolio Tracker")
print("Available stocks:", ", ".join(stock_prices.keys()))

# Input from user
while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not found. Please choose from:", ", ".join(stock_prices.keys()))
        continue
    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
        if quantity < 0:
            print("Quantity must be a positive number.")
            continue
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("Please enter a valid number.")

# Calculate total investment
total_investment = 0
print("\nYour Portfolio:")
for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    total_investment += value
    print(f"{stock}: {qty} shares @ ${stock_prices[stock]} = ${value}")

print(f"\nTotal Investment Value: ${total_investment}")

# Optional: Save to a file
save = input("Do you want to save the result to a file? (yes/no): ").lower()
if save == "yes":
    with open("portfolio_summary.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        file.write("------------------------\n")
        for stock, qty in portfolio.items():
            value = stock_prices[stock] * qty
            file.write(f"{stock}: {qty} shares @ ${stock_prices[stock]} = ${value}\n")
        file.write(f"\nTotal Investment Value: ${total_investment}")
    print("Portfolio saved to 'portfolio_summary.txt'")
