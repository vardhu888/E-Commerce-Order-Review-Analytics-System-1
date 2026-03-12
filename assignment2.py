import math

# Product Catalog (Dictionary with Tuple values)
product_catalog = {
    "E101": ("Laptop", 65000.0, 8),
    "E102": ("Smartphone", 30000.0, 12),
    "E103": ("Smartwatch", 8000.0, 20),
    "E104": ("Headphones", 2500.0, 25)
}

orders = []

# Function 1: Display Product Catalog
def display_catalog():
    print("\n----- Product Catalog -----")
    for pid, details in product_catalog.items():
        name, price, stock = details
        print(f"{pid} | {name} | Price: ₹{price} | Stock: {stock}")


# Function 2: Place Order
def place_order():
    try:
        pid = input("Enter Product ID: ")

        if pid not in product_catalog:
            raise KeyError("Invalid Product ID")

        quantity = int(input("Enter Quantity: "))

        if quantity <= 0:
            raise ValueError("Quantity must be positive")

        name, price, stock = product_catalog[pid]

        if quantity > stock:
            print("Error: Quantity exceeds available stock.")
            return

        order_total = price * quantity

        # Discount
        if order_total > 10000:
            discount = order_total * 0.10
        else:
            discount = 0

        final_bill = math.ceil((order_total - discount) * 100) / 100

        print("Final Bill Amount: ₹", final_bill)

        rating = int(input("Provide rating (1-5): "))

        if rating < 1 or rating > 5:
            raise ValueError("Rating must be between 1 and 5")

        # Update stock
        product_catalog[pid] = (name, price, stock - quantity)

        # Store order
        order = {
            "Product ID": pid,
            "Quantity": quantity,
            "Bill Amount": final_bill,
            "Rating": rating
        }

        orders.append(order)

        print("Order placed successfully!")

    except ValueError as ve:
        print("Value Error:", ve)

    except KeyError as ke:
        print("Key Error:", ke)

    except Exception as e:
        print("Unexpected Error:", e)


# Function 3: Analytics Summary
def analytics_summary():

    if len(orders) < 3:
        print("At least 3 orders required for analytics.")
        return

    print("\n----- Analytics Summary -----")

    # Total Revenue
    total_revenue = sum(order["Bill Amount"] for order in orders)
    print("Total Revenue: ₹", total_revenue)

    # Frequency calculation
    freq = {}
    ratings = {}

    for order in orders:
        pid = order["Product ID"]

        freq[pid] = freq.get(pid, 0) + 1

        if pid not in ratings:
            ratings[pid] = []

        ratings[pid].append(order["Rating"])

    # Most frequently ordered
    most_freq = max(freq, key=freq.get)
    print("Most Frequently Ordered Product:", most_freq)

    # Average ratings
    avg_ratings = {}
    for pid in ratings:
        avg_ratings[pid] = sum(ratings[pid]) / len(ratings[pid])

    highest_rated = max(avg_ratings, key=avg_ratings.get)

    print("Highest Rated Product:", highest_rated)

    print("\nAverage Rating per Product:")
    for pid, avg in avg_ratings.items():
        print(pid, ":", round(avg, 2))

    print("\nRemaining Stock:")
    for pid, details in product_catalog.items():
        print(pid, "-", details[0], "| Stock:", details[2])


# Function 4: Save Report
def save_report():

    if not orders:
        print("No orders to save.")
        return

    try:
        with open("orders_report.txt", "a") as file:
            for order in orders:
                file.write(f"{order['Product ID']}, {order['Quantity']}, {order['Bill Amount']}, {order['Rating']}\n")

        print("Order report saved to orders_report.txt")

    except Exception as e:
        print("File Error:", e)


# Menu Driven Program
while True:

    print("\n------ E-Commerce Order & Review Analytics System ------")
    print("1. Display Product Catalog")
    print("2. Place Order")
    print("3. View Analytics Summary")
    print("4. Save Order Report to File")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_catalog()

    elif choice == "2":
        place_order()

    elif choice == "3":
        analytics_summary()

    elif choice == "4":
        save_report()

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")
