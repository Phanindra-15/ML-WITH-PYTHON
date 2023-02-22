def twin_primes(x,y):
   tp = []
   for i in range(x,y+1):
       if is_prime(i) and is_prime(i+2):
           tp.append((i,i+2))
           
           return tp
print(twin_primes(10,70))
