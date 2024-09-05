import math 

def main():
    a, b, c = input().split()

    a = float(a)
    b = float(b)
    c = float(c)
    
    delta = (b*b) - (4*a*(c))
    
    if delta >=0
    raizdelta = math.sqrt(delta)

    if raizdelta >= 0 and a > 00 or delta <= 0:
        x1 = (-b + (raizdelta)) / (2*a)
        x2 = (-b - (raizdelta)) / (2*a)
        print(delta)
        print(x1)
        print(x2)
    else:
        print("Impossível calcular")

main()