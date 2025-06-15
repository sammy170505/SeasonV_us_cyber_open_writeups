# Crypto – bezoutbezoutbezout

**Category:** Crypto  
**Challenge:** bezoutbezoutbezout  
**Flag Format:** SVUSCG{...}

---

## Challenge

We were given three files:

- `gcds.txt`: a list of integers.
- `nums.txt`: a second list of integers.
- `bezoutbezoutbezout.py`: a partial Python script that contains the following:

    ```python
    for i in range(len(gcds)):
        d = gcds[i]
        a, b = magic_select(d, nums)
        s, t = magic_bezout(a, b)
        assert(d + s + t == ord(flag[i]))
    ```

The goal was to recover the full flag using the given data.

---

## Solution

1. **Understood what the script was doing:**
    - For each flag character, select two numbers `a` and `b` from `nums` such that `gcd(a, b) == d`, where `d` comes from `gcds`.
    - Compute Bézout coefficients `s` and `t` such that `s*a + t*b = d`.
    - Calculate `d + s + t` and convert it to a character with `chr()`.

2. **Wrote a script that:**
    - Loops over all pairs `(a, b)` from `nums` where `gcd(a, b) == d`.
    - Uses a recursive extended Euclidean algorithm to get `(s, t)`.

3. **Tried basic brute-force at first:**
    - The default `(s, t)` from the extended GCD only gives one solution, and in many cases `d + s + t` was not a printable ASCII character.
    - That's why brute-force failed, it didn’t explore the full solution space of Bézout's identity.

4. **Used the general Bézout solution:**
    - Tried many `(s, t)` variations using:
      ```
      s' = s + k * (b / d)
      t' = t - k * (a / d)
      ```
    - Looped over values of `k` from `-100` to `100`.

5. **Filtered for valid characters:**
    - Only accepted results where `d + s + t` was between 32 and 126 (printable ASCII).

6. **Handled missing cases:**
    - If no valid character was found, added a `?` for that index.

7. **Ran the script and printed the flag:**
    - Recovered most of the flag successfully.
    - The remaining characters could be guessed based on known spacing and format.

---