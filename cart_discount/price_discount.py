def main():

    print(discount([10, 4, 20]))  # Expect this to print 4
    # what other lists might this function be called with?


def discount(item_prices):
    """
    Accepts an array of item prices and returns the discount earned.
    Discounts are only earned when there are three or more prices, in which
    case the discount is the price of the cheapest item.

    Args:
        item_prices (list): List of numerical prices.

    Returns:
        int: The discount earned.
    """
    return sorted(item_prices)[0] if len(item_prices) > 2 else 0


if __name__ == '__main__':
    main()
