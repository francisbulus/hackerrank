def jimOrders(orders):
    dict = {}
    for k in range(1,(len(orders)+1)):
        dict[k] = sum(orders[k-1])
    order = sorted(dict, key=dict.get)
    return order