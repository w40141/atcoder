k = int(input())
bin_k = bin(k)
k_2 = bin_k.replace("1", "2")
print(k_2[2:])
