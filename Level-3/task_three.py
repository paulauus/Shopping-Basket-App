def generate_invoice(receipt_string: str) -> str:
    """ Calculates the """
    # Split the lines
    lines = receipt_string.strip().split("\n")
    total_price = 0
    items = []

    # Process each line in the receipt
    for line in lines:
        if line.startswith("Total:"):
            total_price = float(line.strip().split('£')[1])
        else:
            # Split the line to extract item name and price
            item_name, item_price_str = line.split(" - £")
            item_price = float(item_price_str)
            # Calculate VAT-adjusted price
            item_VAT_price = item_price * 0.8
            items.append(f"{item_name} - £{item_VAT_price:.2f}")

    # Calculate VAT
    vat = total_price - sum(float(line.split(' - £')[1]) for line in items)

    if total_price == 0:
        answer = "VAT RECEIPT\n\nTotal: £0.00\nVAT: £0.00\nTotal inc VAT: £0.00"
    else:
    # Format the output invoice
        answer = "VAT RECEIPT\n\n"
        answer += "\n".join(items) + "\n\n"
        answer += f"Total: £{(total_price * 0.8):.2f}\n"
        answer += f"VAT: £{vat:.2f}\n"
        answer += f"Total inc VAT: £{total_price:.2f}"

    return answer



if __name__ == "__main__":
    receipt_string = """Bread x 2 - £3.60
Milk x 1 - £0.80
Butter x 1 - £1.20
Total: £5.60"""
    print(generate_invoice(receipt_string))
