def is_prime(i):
    if i < 2:
        return False
    for d in range(2, int(i ** 0.5) + 1):
        if i % d == 0:
            return False
    return True
    
    
def all_digits_odd(i):
    return all(int(digit) % 2 != 0 for digit in str(i))
    

def odd_dig_primes(n): # P.O.D.P (pure ood digit prime)
    
    liste = []
    
    
    for i in range (2, n):
        if is_prime(i) and all_digits_odd(i):
            liste.append(i)
            
    nombre_de_podp_en_dessous_de_n = len(liste) 
    
    if liste and liste[-1] < n:
        plus_grand_podp_inferieur = liste[-1]
    else:
        plus_grand_podp_inferieur = list[-1] if liste[-1] >= n else liste[-2]
        
    i = n + 1
    while True:
        if is_prime(i) and all_digits_odd(i):
            plus_petit_podp_superieur = i
            break
        i += 1
        
    
    return [nombre_de_podp_en_dessous_de_n, plus_grand_podp_inferieur, plus_petit_podp_superieur]
    
             
    pass 