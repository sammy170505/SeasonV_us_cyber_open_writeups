from Crypto.Util.number import long_to_bytes # type: ignore
from sympy import integer_nthroot

# Given
c = 898564915277349210856325643177982880844269990070750993964886895279898673815668084088711509416748167698104435154155125903563814943672577759197896689419072923530272379905743352154731864706846939063378835946564725599528080721144587149407333

# Step 1: Cube root of ciphertext
m, exact = integer_nthroot(c, 3)  # (value, is_exact)

# Step 2: Convert to bytes and decode
plaintext = long_to_bytes(m)
print("Flag:", plaintext.decode())
