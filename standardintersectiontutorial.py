from math import lcm
print("Please ensure that all inputs are integers!!!")
print("a₁x + b₁y = c₁")
a1 = int(input('What is "a₁" ?'))
b1 = int(input('What is "b₁" ?'))
c1 = int(input('What is "c₁" ?'))
print(f"{a1}x + {b1}y = {c1} ...⓵")
print("a₂x + b₂y = c₂")
a2 = int(input('What is "a₂" ?'))
b2 = int(input('What is "b₂" ?'))
c2 = int(input('What is "c₂" ?'))
print(f"{a2}x + {b2}y = {c2} ...⓶")
input("Press the ENTER/RETURN Key to continue")
print("\n\n\n\n\n\n\n")
if a1 != a2:
    print(f"Find the LCM of {a1}x and {a2}x")
    LCM = lcm(a1, a2)
    print(f"The LCM is {LCM}")
    input("Press the ENTER/RETURN Key to continue")
    print("\n\n\n\n\n\n\n")
    print(f"Find how much ⓵ must be multiplied by for {a1}x to turn into {LCM} x")
    multiplier1 = LCM/a1
    print(f"It must be multiplied by {multiplier1}")
    a1 *= multiplier1
    b1 *= multiplier1
    c1*= multiplier1
    print(f"{a1}x + {b1}y = {c1} ...⓵")
    input("Press the ENTER/RETURN Key to continue")
    print("\n\n\n\n\n\n\n")
    print(f"Find how much ⓶ must be multiplied by for {a2}x to turn into {LCM} x")
    multiplier2 = LCM / a2
    print(f"It must be multiplied by {multiplier2}")
    a2 *= multiplier2
    b2 *= multiplier2
    c2 *= multiplier2
    print(f"{a2}x + {b2}y = {c2} ...⓶")
    input("Press the ENTER/RETURN Key to continue")
    print("\n\n\n\n\n\n\n")

print(f"Since {a1}x is equal to {a2}x, subtract ⓶ from ⓵")
b3 = b1-b2
c3 = c1 - c2
print(f"{b3}y = {c3}")
y= c3/b3
print(f"Thus, y = {y}")
input("Press the ENTER/RETURN Key to continue")
print("\n\n\n\n\n\n\n")
print(f"Substitute y = {y} into ⓵")
print(f"{a1}x + {b1}*{y} = {c1}")
print(f"{a1}x = {c1} - {b1*y}")
x = (c1 - (b1*y))/a1
print(f"Thus, x = {x}")
input("Press the ENTER/RETURN Key to continue")
print("\n\n\n\n\n\n\n")
print(f"Therefore, the point of intersection is ({x}, {y})")