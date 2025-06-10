# Echo.jpg Forensics Writeup

## Challenge Type
Forensics — Image Analysis

## File Provided
`Echo.jpg`

## Steps Taken

1. **Verified file type**  
   Used `file Echo.jpg` to confirm it’s a valid JPEG image.

2. **Checked Exif metadata**  
   Ran `exiftool Echo.jpg` to look for hidden data in fields like `UserComment`, `Software`, or GPS tags. Nothing unusual was found.

3. **Searched for appended data**  
   Executed:
   ```sh
   strings Echo.jpg | grep -i 'SVB'
   ```

4. **Flag Found**
    SVBRG{....}
