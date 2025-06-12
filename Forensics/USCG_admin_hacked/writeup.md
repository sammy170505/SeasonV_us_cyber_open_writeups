# USCG Admin Hacked - Forensics Writeup

## Goal

Identify the malicious startup application set to run when a user logs in.

## Approach

1. **Unzip the registry.7z**
    ```bash
    7z x registry.7z
    ```

2. **Identify user registry hives:**  
   Located `NTUSER.DAT` under `Users/uscgadmin/`.

3. **Extract Run keys:**  
   Used `reglookup` to search for startup entries:
   ```bash
   reglookup NTUSER.DAT | grep -i 'run'
    ```

4. **Finding**
    ```bash
    /Software/Microsoft/Windows/CurrentVersion/Run/ SVUSCG{uf0undme},SZ,C:\Users\uscgadmin\Documents\MSDCSC\msdcsc.exe
    ```
