ground_shipping_premium = 125.00

def calculate_ground(weight):
    if weight <= 2:
        cost_ground = weight * 1.5 + 20
    elif weight <= 6:
        cost_ground = weight * 3.00 + 20
    elif weight <= 10:
        cost_ground = weight * 4.00 + 20
    else:
        cost_ground = weight * 4.75 + 20

    return cost_ground


def calculate_drone(weight):
    if weight <= 2:
        cost_drone = weight * 4.50
    elif weight <= 6:
        cost_drone = weight * 9.00
    elif weight <= 10:
        cost_drone = weight * 12.00
    else:
        cost_drone = weight * 14.25

    return cost_drone


def calculate_cheapest(weight):
    if calculate_drone(weight) < calculate_ground(weight) and calculate_drone(weight) < ground_shipping_premium:
        print(f"Cheapest cost is with drone shipping. Cost is ${calculate_drone(weight)}")
    elif calculate_ground(weight) < calculate_drone(weight) and calculate_ground(weight) < ground_shipping_premium:
        print(f"Cheapest cost is with ground shipping. Cost is ${calculate_ground(weight)}")
    else:
        print(f"Cheapest cost is with ground shipping premium. Cost is ${ground_shipping_premium}")


