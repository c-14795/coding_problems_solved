# 4 100
# 20 90 40 90
for i in range(int(input())):
    num_houses, budget = input().split(" ")
    budget = int(budget)

    house_prices = sorted([int(price) for price in input().split(" ")])
    total_sum = 0
    cnt = 0
    for each_price in house_prices:
        total_sum = total_sum + each_price
        if budget < total_sum:
            break
        cnt = cnt + 1
    print("Case #{}: {}".format(i + 1, cnt), end='\n')
