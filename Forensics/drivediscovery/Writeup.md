# Drive Discovery CTF – Full Write-up

## Challenge Description

> **We took an image of a suspicious USB drive - can you investigate it in more detail?  
> We think the user may have tried to cover their tracks.**

**File provided:** `nothinginterestinghere.001`

---

## Step 1: Identify the Image File

Check the file type:
```sh
file nothinginterestinghere.001
```

Result
```sh
DOS/MBR boot sector MS-MBR Windows 7...
```
It’s a disk image (USB drive).

## Step 2: Examine the Partitions

List partitions in the the image:
```sh
fdisk -l nothinginterestinghere.001
```

Result:
```
Disk nothinginterestinghere.001: 10 MiB, 10485760 bytes, 20480 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: gpt
Disk identifier: 57E69F86-3F3B-41EE-8B6E-EC5DFA2FEDBE

Device                       Start   End Sectors Size Type
nothinginterestinghere.001p1   128 16511   16384   8M Microsoft basic data
```

## Step 3: Mount the partitions

```sh
sudo mount -o loop,offset=$((128*512)) nothinginterestinghere.001 /mnt/usb
```
## Step 4: Explore the Filesystem
```sh
ls -l /mnt/usb
```

Output:

```sh
$RECYCLE.BIN/
Pictures/
Recipes/
Secrets/
System Volume Information/
```
## Step 5: Investigate “Secrets”
```sh
ls -l /mnt/usb/Secrets
cat /mnt/usb/Secrets/note\ to\ self.txt
```

Result:
```vbnet
NOTES:
1. Make sure to delete flag.txt before giving this USB drive to anyone.
2. Apparently there's a really secure type of encryption called Base64, I should look into using that.
```
> The note suggests the flag was deleted and references Base64.


## Step 6: File Carving for Deleted Files
Use foremost to recover deleted files:

```sh
foremost -i nothinginterestinghere.001 -o outputdir
```
Review the output:

```sh
outputdir/jpg/00001248.jpg

outputdir/png/00001304.png
```

## Step 7: Analyze Carved Images
Try extracting readable strings from the images:

```sh
strings outputdir/png/00001304.png | grep -E '[A-Za-z0-9+/=]{16,}'
```
No useful results.

## Why Did I Choose `image3.png`?

During my initial sweep of the provided images, I specifically targeted `image3.png` for deeper analysis for several reasons:

- **Suspicious Metadata:**  
  Running `exiftool` and `pngcheck` revealed multiple metadata fields (including custom `tEXt` chunks), an outdated modification date, and a warning about non-standard PNG chunk ordering.
- **Anomalous Structure:**  
  The file size and chunk count were a bit unusual for its apparent dimensions and content. The presence of extra zlib-compressed streams (`zlib` data) embedded beyond normal image data made it a strong candidate for steganography or hidden content.
- **Hints from CTF:**  
  The CTF hinted at flags hidden through non-obvious means. Out of all the files, `image3.png` showed the most classic signs of deliberate manipulation (e.g., hidden chunks, non-standard software used to create it).
- **Process of Elimination:**  
  Other images either quickly revealed nothing of interest or were simple photographs without embedded data.

By combining these clues, I prioritized `image3.png` for advanced forensics (strings, chunk analysis, and zlib decompression), which ultimately led to the successful flag extraction.


## Step 8: Try Steganalysis and Metadata
Check metadata:

```sh
exiftool /mnt/usb/Pictures/image3.png
```

Run zsteg for steganography:

```sh
zsteg /mnt/usb/Pictures/image3.png
```
> No flag found yet.

## Step 9: Look for Embedded/Compressed Data
Extract embedded streams with binwalk:

```sh
binwalk -e /mnt/usb/Pictures/image3.png
```

You get a file like _image3.png.extracted/8A.zlib:

```sh
file _image3.png.extracted/8A.zlib
```
Result:
> zlib compressed data

## Step 10: Try to Decompress the zlib Data
Direct decompression fails, so try skipping bytes (brute force):

```sh
for n in {1..32}; do
  dd if=_image3.png.extracted/8A.zlib of=zlib_skip${n}.bin bs=1 skip=$n status=none
  python3 -c "import zlib; print(zlib.decompress(open('zlib_skip${n}.bin','rb').read()).decode(errors='ignore'))" 2>/dev/null
done
```

> Still nothing conclusive.

## Step 11: Grep for the Flag Pattern
Search all files for the CTF flag format or base64-encoded strings:

```sh
strings nothinginterestinghere.001 | grep -E '[A-Za-z0-9+/=]{16,}'
```
I found: 
```sh
U1ZCUkd7ZDNsMzczZF9uMDdfZjByNjA3NzNuXzI4MzAyOTM4Mn0=
```
> This is a Base64-encoded string.

## Step 12: Decode the Flag
Decode with:

```sh
echo 'U1ZCUkd7ZDNsMzczZF9uMDdfZjByNjA3NzNuXzI4MzAyOTM4Mn0=' | base64 -d
```
Result:
```sh
SVBRG{THE FLAG}
```
