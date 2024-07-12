def generate_invoice(receipt_string: str) -> str:
    # Split the lines
    lines = receipt_string.strip().split("\n")
    total_price = 0
    new_lines = []

    for line in lines:
        if line.startswith("Total:"):
            total_price = float(line.strip().split('£')[1])
        else:
            line_parts = line.split("£")
            if len(line_parts) == 2:
                item_name = line_parts[0]
                item_price = float(line_parts[1])
                item_VAT_price = item_price / 1.2
                new_lines.append(f"{item_name} - £{item_VAT_price:.2f}")
    return  # return the invoice string


if __name__ == "__main__":
    receipt_string = """Bread x 2 - £3.60
Milk x 1 - £0.80
Butter x 1 - £1.20
Total: £5.60"""
    print(generate_invoice(receipt_string))
