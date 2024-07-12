basket = []

#####
#
# COPY YOUR CODE FROM LEVEL 1 BELOW
#
#####


def add_to_basket(item: dict) -> list:
    """ Takes an item from a dictionary and it to a list. """
    basket.append(item)
    return basket


def generate_receipt(basket: list) -> str:
    """ Outputs the items in the basket, their prices and the total price. """
    total_price = 0
    answer = ""
    if len(basket) == 0:
        return "Basket is empty"

    # Dictionary to store item counts and total prices
    item_counts = {}
    for item in basket:
        item_name = item['name']
        item_price = item['price']

        # Use a tuple as key to differentiate items with same name but different price
        item_key = (item_name, item_price)
        if item_key in item_counts:
            item_counts[item_key]['quantity'] += 1
            item_counts[item_key]['total_price'] += item_price
        else:
            item_counts[item_key] = {'quantity': 1, 'total_price': item_price}

        total_price += item_price

    for (item_name, item_price), info in item_counts.items():
        quantity = info['quantity']
        total_price_for_item = info['total_price']
        if total_price_for_item == 0:
            answer += f'{item_name} x {quantity} - Free\n'
        else:
            answer += f'{item_name} x {quantity} - £{total_price_for_item:.2f}\n'

    answer += f"Total: £{total_price:.2f}"
    return answer

#####
#
# COPY YOUR CODE FROM LEVEL 1 ABOVE
#
#####


if __name__ == "__main__":
    add_to_basket({
        "name": "Bread",
        "price": 1.80
    })
    add_to_basket({
        "name": "Bread",
        "price": 1.80
    })
    add_to_basket({
        "name": "Milk",
        "price": 0.80
    })
    add_to_basket({
        "name": "Butter",
        "price": 1.20
    })
    print(generate_receipt(basket))
