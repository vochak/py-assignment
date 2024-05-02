def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.

    Args:
        price (float): Original price of the item.
        discount_percent (float): Discount percentage (between 0 and 100).

    Returns:
        float: Final price after applying the discount.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Get input from the user
original_price = float(input("Enter the original price: "))
discount_percentage = float(input("Enter the discount percentage: "))

# Calculate the final price
final_price = calculate_discount(original_price, discount_percentage)

# Print the result
if final_price == original_price:
    print(f"No discount applied. Final price: ${final_price:.2f}")
else:
    print(f"Discount applied. Final price: ${final_price:.2f}")
