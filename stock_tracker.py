# CodeAlpha - Task 2
# Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "AMZN": 190,
    "MSFT": 420
}

print("================================")
print("     STOCK PORTFOLIO TRACKER")
print("================================")

total_investment = 0

while True:
    print("\nAvailable Stocks:")
    print("AAPL - $180")
    print("TSLA - $250")
    print("GOOG - $150")
    print("AMZN - $190")
    print("MSFT - $420")

    stock_name = input("\nEnter stock name (or type 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("❌ Stock not available. Please choose from the list.")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("❌ Quantity must be greater than 0.")
            continue

        price = stock_prices[stock_name]
        investment = price * quantity

        print("\nStock:", stock_name)
        print("Price per share: $", price)
        print("Quantity:", quantity)
        print("Investment: $", investment)

        total_investment += investment

    except ValueError:
        print("❌ Please enter a valid number for quantity.")

print("\n================================")
print("       PORTFOLIO SUMMARY")
print("================================")
print("Total Investment: $", total_investment)
print("Thank you for using Stock Portfolio Tracker!")