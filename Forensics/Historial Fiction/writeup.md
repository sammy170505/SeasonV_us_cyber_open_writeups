# Chrome History Forensics - Find the Book ISBN

**Category:** Forensics  
**Challenge:** Chrome History / Book ISBN  
**Flag Format:** SVUSCG{ISBN}

---

## Challenge

We were given a Chrome browser history database and told an administrator looked at a cybersecurity paperback book online. The flag is the ISBN of that specific paperback edition.

---

## Solution

1. **Extracted the 7z archive:**
    ```bash
    7z x Google.7z
    ```

2. **Opened the Chrome History database** (`History` file) using **DB Browser for SQLite**.

3. **Browsed the `urls` table:**
    - Clicked on the **Browse Data** tab.
    - Selected the `urls` table from the dropdown.

4. **Filtered and searched for relevant entries:**
    - Searched for keywords like `amazon`.
    - Located a URL/title corresponding to a paperback cybersecurity book.

5. **Extracted the ISBN:**
    - The ISBN for the paperback edition was visible in the Amazon URL or by opening the link and checking the book details.

6. **Submitted the flag in the correct format:**
    ```
    SVUSCG{ISBN_NUMBER}
    ```

---

