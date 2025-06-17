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