# FTP Forgotten Password Forensics (IIS Log)

## Challenge
Find how many times the administrator forgot their FTP password, as indicated by failed logins in the IIS log file (`ex250604.log`).

## Approach
1. **Identify failed login attempts:**  
   In IIS FTP logs, failed password attempts are recorded as `PASS` commands returning status `530`.

2. **Handle binary issues:**  
   The log file was being detected as binary by `grep`, leading to incorrect results.  
   To address this, the `strings` utility was used to extract only readable ASCII lines for analysis.

3. **Count the failures:**  
   Run:
   ```bash
   strings ex250604.log | grep "PASS" | grep "530" | wc -l
    ```
4. ## The failure number is the Flag
    SVUSCG{number}