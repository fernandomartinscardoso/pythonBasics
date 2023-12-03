# Greatest common divisor algorithm
def gcd(u,v):
    #t=0
    if u < v:
        t=u
    else:
        t=v
    while u%t != 0 or v%t != 0:
        t=t-1
    gcd=t
    return print("GCD of {} and {} is {}".format(u,v,gcd))

gcd(0,26)