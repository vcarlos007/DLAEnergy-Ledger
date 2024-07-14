import datetime

class FuelTransaction:
    def __init__(self, date, transaction_type, quantity, price_per_gallon):
        self.date = date
        self.transaction_type = transaction_type
        self.quantity = quantity
        self.price_per_gallon = price_per_gallon
        self.total_price = quantity * price_per_gallon

class JAAFuelLedger:
    def __init__(self):
        self.transactions = []
        self.inventory = 0

    def add_transaction(self, transaction_type, quantity, price_per_gallon):
        date = datetime.datetime.now()
        transaction = FuelTransaction(date, transaction_type, quantity, price_per_gallon)
        self.transactions.append(transaction)

        if transaction_type == 'Received':
            self.inventory += quantity
        elif transaction_type == 'Issued':
            self.inventory -= quantity

        return transaction

    def view_inventory(self):
        print(f"\nCurrent JAA Fuel Inventory: {self.inventory} gallons")

    def generate_report(self, start_date, end_date):
        report_transactions = [t for t in self.transactions if start_date <= t.date <= end_date]
        
        print(f"\nJAA Fuel Report from {start_date.date()} to {end_date.date()}:")
        print("Date\t\tType\tQuantity\tPrice/Gal\tTotal")
        print("-" * 65)
        
        total_received = 0
        total_issued = 0
        for t in report_transactions:
            print(f"{t.date:%Y-%m-%d}\t{t.transaction_type}\t{t.quantity}\t\t${t.price_per_gallon:.2f}\t\t${t.total_price:.2f}")
            if t.transaction_type == 'Received':
                total_received += t.total_price
            else:
                total_issued += t.total_price
        
        print("-" * 65)
        print(f"Total Received: ${total_received:.2f}")
        print(f"Total Issued: ${total_issued:.2f}")

def main():
    ledger = JAAFuelLedger()

    while True:
        print("\nJAA Fuel Ledger")
        print("1. Add Fuel Received")
        print("2. Record Fuel Issued")
        print("3. View Current Inventory")
        print("4. Generate Report")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1' or choice == '2':
            transaction_type = 'Received' if choice == '1' else 'Issued'
            quantity = float(input("Enter quantity in gallons: "))
            price = float(input("Enter price per gallon: $"))
            transaction = ledger.add_transaction(transaction_type, quantity, price)
            print(f"Transaction recorded: {transaction_type} {quantity} gallons of JAA fuel at ${price:.2f}/gallon")

        elif choice == '3':
            ledger.view_inventory()

        elif choice == '4':
            start_date = datetime.datetime.strptime(input("Enter start date (YYYY-MM-DD): "), "%Y-%m-%d")
            end_date = datetime.datetime.strptime(input("Enter end date (YYYY-MM-DD): "), "%Y-%m-%d")
            ledger.generate_report(start_date, end_date)

        elif choice == '5':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()