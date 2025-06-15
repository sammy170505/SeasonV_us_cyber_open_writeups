# Gotta Go Low – RSA Low Exponent Attack

**Category:** Crypto  
**Challenge:** Gotta Go Low  
**Flag Format:** SVBGR{...} or SVBRG{...}

---

## Challenge

We were given a Python script that uses RSA encryption with:

- A low public exponent `e = 3`
- A 1024-bit modulus `n`
- A short message: the flag
- No padding used during encryption

We were also provided with the public key and the ciphertext in `output.txt`.

---

## Solution

1. **Identified low-exponent vulnerability:**
   - The public exponent `e = 3` was very small.
   - The message was a short flag like `SVBGR{...}`.
   - Because the message is short, its cube (`m^3`) is smaller than `n`.

2. **Recognized that:**
   - If `m^3 < n`, then encryption does not wrap modulo `n`, so:
     ```
     c = m^3
     ```

3. **Recovered `m` using cube root:**
   - Used `sympy.integer_nthroot(c, 3)` to compute the integer cube root.

4. **Decoded the result:**
   - Converted the cube root value back to bytes.
   - Decoded the bytes to get the plaintext flag.
