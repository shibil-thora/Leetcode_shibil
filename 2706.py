prices = [98,54,6,34,66,63,52,39]
money = 3
sum_num = 0
prices.sort()
for i in range(len(prices)):
    try:
        if prices[i] + prices[i + 1] <= money:
            sum_num = prices[i] + prices[i + 1]
            break
    except:
        sum_num = 0

print(money - sum_num)