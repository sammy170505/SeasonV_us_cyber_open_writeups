# Redactables - Forensics CTF Writeup

**Category:** Forensics  
**Challenge Name:** Redactables  
**Hash Given:** 05f6b8c32740c785e07432d5dbd7cb7e  
**Flag Format:** SVUSCG{This_is_a_Flag}

---

## Challenge Prompt

> My friend redacted this file, but I think they made a mistake. Can you find it?  
> The MD5 hash of the provided file is `05f6b8c32740c785e07432d5dbd7cb7e`.

---

## Initial Inspection

1. **Check file type:**
    ```sh
    file redactable.pdf
    ```
    Output:
    ```sh
    redactable.pdf: PDF document, version 1.7
    ```

2. **Try extracting text or info:**
    ```sh
    pdftotext redactable.pdf output.txt
    ```
    Output:
    ```sh
    Command Line Error: Incorrect password
    ```

3. **The PDF is password protected.**

---

## Password Cracking

### Step 1: Extract PDF hash for John the Ripper

```sh
/usr/share/john/pdf2john.pl redactable.pdf > hash.txt
```
### Step 2: Use John with rockyou wordlist

```bash
john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt
```

Output:
```bash
friends4eva      (redactable.pdf)
```

## Unlock & Analyze PDF

### Step 1: Try extracting text (no flag in text)

```bash
pdftotext -upw friends4eva redactable.pdf output.txt
cat output.txt
```
> NO flag just a black box in the pdf

### Step 2: Extract the image from pdf

```bash
pdfimages -upw friends4eva -all redactable.pdf extracted
```

This produces an image: extracted-000.jpg

### Step 3: View the extracted image

The image contains a swirled/distorted text, starting with SVUSCG.

## Reverse the Image Obfuscation

### Step 1: Open extracted-000.jpg in GIMP 

### Step 2 : Go to:

    Filters > Distorts > Whirl and Pinch...


### Set the whirl to -500 
    
    The text unscrambles to reveal the flag.
