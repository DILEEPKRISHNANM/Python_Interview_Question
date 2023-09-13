n = int(input("enter the array limit:"))
a = []
for i in range(n):
    x = int(input("enter the number {}: ".format(i)))
    a.append(x)

max_product = 0  # Initialize max_product with negative infinity
a_index, b_index = 0, 0

for j in range(len(a)):
    for k in range(j + 1, len(a)):
        product = a[j] * a[k]
        if product > max_product:
            max_product = product
            a_index, b_index = j, k

# Print the pair with the highest multiplied result
print("Pair with the highest multiplied result:", a[a_index], a[b_index])
