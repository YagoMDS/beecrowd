import math 

def main():
    a, b, c = input().split()

    a = float(a)
    b = float(b)
    c = float(c)
    
    delta = (b*b) - (4*a*(c))
    
    if delta > 0 and a != 0:
        raizdelta = math.sqrt(delta)
        if raizdelta > 0:
            x1 = (-b + (raizdelta)) / (2*a)
            x2 = (-b - (raizdelta)) / (2*a)
            print(f'R1 = {x1:.5f}')
            print(f'R2 = {x2:.5f}')
    else:
        print("Impossivel calcular")

main()