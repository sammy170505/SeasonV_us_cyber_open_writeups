# Prime Suspects – RSA Decryption

**Category:** Crypto  
**Challenge:** Prime Suspects  
**Flag Format:** SVUSCG{...}

---

## Challenge

We were given a weak RSA encryption setup with the following values:

- `n`: RSA modulus
- `e`: Public exponent (65537)
- `c`: Ciphertext

Our task was to decrypt the message and recover the flag.

---

## Solution

1. **Noticed small RSA modulus `n`:**  
   The modulus was only 78 digits long, which hinted that it might be factorable.

2. **Factored `n` using FactorDB:**
   - Factordb.com quickly returned two 39-digit primes:
     ```
     p = 305875545128432734240552595430305723491
     q = 333679396508538352589365351078683227609
     ```

3. **Used RSA decryption steps:**
   - Calculated phi(n) = (p - 1)(q - 1)
   - Computed the private key `d = inverse(e, phi(n))`
   - Decrypted the ciphertext: `m = c^d mod n`

4. **Converted decrypted integer to bytes:**
   - Got: `b'SVUSCG{...}'`

5. **Decoded the flag:**
   - The decrypted message was already in plaintext.
   - No base64 decoding was necessary.
