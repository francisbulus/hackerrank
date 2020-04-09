def max_toys(prices, k):
    prices.sort()
    purchase_count = 0
    total_so_far = 0
​
    for toy_price in prices:
        total_so_far += toy_price
        if k >= total_so_far:
            purchase_count += 1
        else:
            return purchase_count