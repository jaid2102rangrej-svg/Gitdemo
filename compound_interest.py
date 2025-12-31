"""amount =  p(1+r/100)**t
ci = amount -p
"""


principal = float(input("enter principal amount"))
rate = float(input("enter rate of interest"))
time = float(input("enter time "))
amount1 = principal * (1+rate/time)**time
amount2 = principal * principal * pow((1+rate/time),time)
print("amount1 is ",amount1)
print("amount2 is ",amount2)

print(round(amount2,2))

ci = amount2 - principal

print("compound interest is",round(ci,2))
