n = 1
highest = 0
while n < 100000:
    concenated_product = ""
    i = 1
    while len(concenated_product) < 9:
        concenated_product += str(n * i)
        # print(concenated_product, i)
        i += 1
    if int(concenated_product) > highest and len(concenated_product) == 9 and set(concenated_product) == set("123456789"):
        highest = int(concenated_product)

    n += 1

print(highest)

