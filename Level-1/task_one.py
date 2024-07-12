
basket = []


def add_to_basket(item: dict) -> list:
    """ Takes an item from a dictionary and it to a list. """
    basket.append(item)
    return


def generate_receipt(basket: list) -> str:
    """ Outputs the items in the basket, their prices and the total price. """
    total_price = 0
    answer = ""
    if len(basket) == 0:
        return "Basket is empty"
    else:
        for i in basket:
            total_price += i["price"]
            answer += (f'{i["name"]} - £{i["price"]:.2f}\n')
        answer += f"Total: £{total_price:.2f}"
    return answer


if __name__ == "__main__":
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
