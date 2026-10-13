def greet(name):
    return f"Hello, {name}!"

print(greet('Tobi'))
    

def item_cost(price, quantity):
    return price * quantity

def delivered_cost(price, quantity, delivery):
    subtotal = item_cost(price, quantity)
    return subtotal + delivery

