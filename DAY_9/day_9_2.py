from art import logo


def add_bid_to_log(log, name, price):
    log.append({"name": name, "price": price})


def find_highest_price(log):
    highest_price = 0
    highest_name = ""
    for person in log:
        if person["price"] > highest_price:
            highest_price = person["price"]
            highest_name = person["name"]
    return {"name": highest_name, "price": highest_price}


end_bid = False
while not end_bid:
    print(logo)
    bid_log = []

    add_person = True
    while add_person:
        name_person = input("What is bidder's name: ")
        price_person = int(input("What is bidder's price: "))
        add_bid_to_log(bid_log, name_person, price_person)
        add_person = True if input("Anyone else would you like to bid again? (y/n): ") == "y" else False

    highest = find_highest_price(bid_log)
    print(f"The highest price is {highest["price"]} belonging to {highest['name']}.")
    end_bid = True if input("Would you like to continue? (y/n): ") == "y" else False

print("End of program.")
