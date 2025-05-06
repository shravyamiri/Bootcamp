def calculate_discount(price, is_member):
    # Members receive a 10% discount as part of loyalty program
    if is_member:
        return price * 0.9
    return price
