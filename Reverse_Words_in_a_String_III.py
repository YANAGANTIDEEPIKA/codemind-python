s=input()
n=s.split(" ")
rs=[word[::-1] for word in n]
ns=" ".join(rs)
print(ns)