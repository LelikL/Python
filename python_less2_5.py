prices = [57.08, 46.51, 97, 51, 1.76, 20, 25.08, 76, 23.34, 98.90,
	          70.01, 63, 39, 90.47, 29, 24, 42, 59.11, 45.78, 48.29,
	          8.53, 67, 95, 5.62, 11, 18.34, 13, 64.80, 78, 93, 88.08]

#-------------------------- A -------------------------------------------
print(f"{'-' * 35} A {'-' * 35} \n")
for price in prices:
	price_rub, price_kop = str(f"{price:.2f}").split(".")
	print(f"{price_rub} руб {int(price_kop):02d} коп, ", end=" ")

#-------------------------- B -------------------------------------------
print(f"\n\n{'-' * 35} B {'-' * 35} \n")

print(f" id prices = {id(prices)}")
prices.sort()
print(f" prices_ sort = {prices} \n")
print(f" id prices_sort = {id(prices)}")

#-------------------------- C -------------------------------------------
print(f"\n\n{'-' * 35} C {'-' * 35} \n")

print(f" id prices = {id(prices)}")
prices.sort(reverse=1)
prices_2 = prices.copy()
print(f" id prices_2 = {id(prices_2)}")
#prices_2.sort(prices_2, reverse=1)
print(prices_2)

#-------------------------- D -------------------------------------------
print(f"\n\n{'-' * 35} D {'-' * 35} \n")
prices5_max = sorted(prices[:5])
print(prices5_max)

