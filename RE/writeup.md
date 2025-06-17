# Reverse Engineering – CTF Cafe

**Category:** Reverse Engineering  
**Challenge:** CTF Cafe  
**Flag Format:** SVBGR{...}

---

## Challenge

We were given a 64-bit ELF binary named `ctf_cafe`, which when executed presented a restaurant-themed menu interface

The hint stated:  
> "We pride ourselves in our secret sauce, which is exclusive or something along those lines."

This pointed toward an XOR-based obfuscation hiding the flag.

---


## Solution

1. **Initial Exploration:**
   - The binary was **not stripped**, so we used `nm` to inspect its symbols:
     ```bash
     nm ./ctf_cafe | grep -iE "flag|secret|order|menu"
     ```
     Revealed useful symbols like:
     - `menu_items`
     - `order_total`
     - `place_order`
     - `secret_sauce` ← suspicious global symbol

2. **Interactive Behavior:**
   - Ran the program and explored the menu.
   - No obvious flag output or hidden options even after ordering every item.

3. **Static and Memory Analysis with GDB:**
   - Opened the binary in `gdb` and inspected `secret_sauce`:
     ```bash
     x/64bx 0x4030c0
     ```
     Recovered a 40-byte array followed by 8 bytes that resembled an XOR key:
     ```python
     encrypted_flag = [0xc8, 0x84, 0x85, 0x1d, ..., 0x00]
     xor_key = [0x9b, 0xd2, 0xc7, 0x5a, 0x49, 0xc4, 0xef, 0xeb]
     ```

4. **Decryption with Python:**
   - Recognized this as a repeating-key XOR cipher.
   - Wrote a script to XOR each byte of the encrypted flag with the corresponding byte from the key (modulo key length):
     ```python
     def xor_decrypt(data, key):
         return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])
     ```

5. **Recovered the Flag:**
   - Successfully decrypted the flag:
     ```bash
     SVBGR{...}
     ```

---