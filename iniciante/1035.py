import math 

def main():

    a = float(input())
    b = float(input())
    c = float(input())
    
    delta = (b*b) - (4*a*(c))
    raizdelta = math.sqrt(delta)

    if raizdelta >= 0 and a > 00:
        x1 = (-b + (raizdelta)) / (2*a)
        x2 = (-b - (raizdelta)) / (2*a)
        print(delta)
        print(x1)
        print(x2)
    else:
        print("Impossível calcular")

    


main()