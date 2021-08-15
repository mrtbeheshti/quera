import math as m
angle=float(input())
angle_rad=m.radians(angle)
print(m.gcd(m.ceil((angle**(float(5)/3))+m.tan(angle_rad)),m.floor(m.pi**(2+(m.atan(m.sin(angle_rad)**2))))))  