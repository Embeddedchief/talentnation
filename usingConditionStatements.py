#to check if budget is greater than cost
def can_afford(budget, cost):
    if budget >= cost:
        return f'{budget} is enough to cover {cost}'


print(can_afford(5000, 4500))


#to check if the value given is same as value expected
def matches_expected(actual, expected):
    if actual == expected:
        return f"Value given is correct"

print(matches_expected(1000,1000))


#checking if budget is enough to cover a cost
def funding_status(budget, cost):
    if budget >= cost:
        return 'enough'
    else:
        return 'Not enough'

print(funding_status(100, 150))