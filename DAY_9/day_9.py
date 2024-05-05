
def add_travel(log, country, visits, cities):
    new_log_dict = {"country": country, "visits": visits, "cities": cities}
    log.append(new_log_dict)


def display_log(log):
    for subdict in log:
        for key, value in subdict.items():
            if key == "cities":
                print(f"{key}: ", end="")
                for index, city in enumerate(value):
                    if index > 0:
                        print(f"\t\t{city}")
                    else:
                        print(f"{city}")
            else:
                print(f"{key}: {value}")
        print()


travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Aachen", "Hamburg"]
    }
]

display_log(travel_log)
country_input = input("Enter country name: ")
visits_input = int(input("Enter number of visits: "))
cities_input = list(input("Enter cities you visited: ").strip().split(", "))
add_travel(travel_log, country_input, visits_input, cities_input)
display_log(travel_log)
