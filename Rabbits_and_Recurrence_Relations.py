a = 1
j = 1
k = 3

f1 = 1*j                     # 1
f2 = 1*a                     # 2
f3 = f2*a + (f1 * k*j)       # 4
f4 = f3*a + (f2 * k*j)       # 7
f5 = f4*a + (f3 * k*j)       # 19   

print(f5)


n = 5
k = 3

fn = f(n-1) + f(n-3) * k