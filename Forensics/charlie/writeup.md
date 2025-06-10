## CTF Forensics Challenge: Extracting the Flag from `charlie.jpg`

### Challenge Type

Forensics

---

### Steps to Retrieve the Flag

#### 1. Identify Embedded Content

Run `binwalk` to analyze `charlie.jpg` for hidden files:

```bash
binwalk -e charlie.jpg
```

This revealed an embedded ZIP file starting at offset `0x4451BC` containing `flag.txt`.

#### 2. Extract the ZIP from the JPEG

Manually extract the ZIP archive using `dd`:

```bash
dd if=charlie.jpg bs=1 skip=4477372 of=hidden.zip
```

#### 3. Unzip the Extracted Archive

```bash
unzip hidden.zip
```

This yields `flag.txt`.

#### 4. Decode the Contents of `flag.txt`

The file contained a single line with 65,536 characters. Use base64 decoding to extract the embedded file:

```bash
base64 -d flag.txt > output.bin
```

#### 5. Identify and Open the Decoded File

Check the file type:

```bash
file output.bin
```

This revealed it to be a JPEG image. Rename and open it:

```bash
mv output.bin extracted.jpg
xdg-open extracted.jpg
```

#### 6. Retrieve the Flag

The decoded image visibly contained the flag in the format:

```
SVBGR{...}
```

---
