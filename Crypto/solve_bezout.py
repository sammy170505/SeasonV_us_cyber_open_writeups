from math import gcd

with open('gcds.txt') as f:
    gcds = eval(f.read())
with open('nums.txt') as f:
    nums = eval(f.read())

def extended_gcd(a, b):
    if b == 0:
        return (1, 0)
    else:
        q, r = divmod(a, b)
        s, t = extended_gcd(b, r)
        return (t, s - q * t)

flag = ''
for idx, d in enumerate(gcds):
    found = False
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j:
                continue
            a, b = nums[i], nums[j]
            if gcd(a, b) == d:
                s, t = extended_gcd(a, b)
                # Try multiple k values
                for k in range(-100, 101):
                    s_ = s + k * (b // d)
                    t_ = t - k * (a // d)
                    val = d + s_ + t_
                    if 32 <= val <= 126:
                        print(f"Position {idx} (d={d}): '{chr(val)}' from a={a}, b={b}, s={s_}, t={t_}, k={k}")
                        flag += chr(val)
                        found = True
                        break
                if found:
                    break
        if found:
            break
    if not found:
        print(f"No printable candidates for position {idx} (d={d})")
        flag += '?'

print("Flag so far:", flag)
