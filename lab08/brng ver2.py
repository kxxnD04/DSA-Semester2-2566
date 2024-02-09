"""holy shito"""
import json as jonathan
def gcd(num1, num2):
    """use recursive function and modulo to calculate gcd"""
    if num1 > num2:
        num1, num2 = num2, num1
    if num1 == 0:
        return num2
    return gcd(num1, num2%num1)

def calcualte_field(start, jump, amount, field, lcm):
    """try to make it less"""
    batch = []
    out = 0
    for j in range(amount):
        current = field[(start + (j * jump))%256]
        if current == field[start] and j != 0:
            break
        batch.append(current)
    out += sum(batch) * ((amount*jump) // lcm)
    batch = []
    for k in range(((amount*jump) % lcm)//jump):
        current = field[(start + (k * jump))%256]
        batch.append(current)
    out += sum(batch)
    return out

def gotsum(field, amounts, spatium):
    """Amazing grace how sweet the sound
    That saved a wretch like me
    I once was lost, but now I'm found
    Was blind but now I see"""
    most = 0
    leastcm = abs(spatium * 256)//gcd(spatium, 256)
    field = dict(enumerate(field))
    for i in range(256):
        now = calcualte_field(i, spatium, amounts, field, leastcm)
        most = max(now, most)
    print(int(most))

gotsum(jonathan.loads(input()), int(input()), int(input()))