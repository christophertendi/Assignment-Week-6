prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

stock = 5

for x,y in prices.items():
    print(x)
    print("price:",y)
    print("stock", stock)

total = 0
for item in prices:
    total +- stock * prices [item]
print("total price:", total)
