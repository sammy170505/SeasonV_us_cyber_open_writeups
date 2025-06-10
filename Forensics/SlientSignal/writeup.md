
# SilentSignal.pcap - Forensics Challenge Writeup

## Challenge Description

We were provided with a PCAP file named `SilentSignal.pcap` and no additional context. The objective was to identify and extract a flag from the capture file. The expected flag format was either `SVBGR{...}` or `SVBRG{...}`.

---

## Tools Used

- Wireshark
- TShark
- Bash
- Python

---

## Methodology

### 1. Initial Inspection

The file was opened in Wireshark. All packets were ICMP Echo Requests (type 8) targeting `8.8.8.8`. Each packet had:

- No response (Echo Reply) packets
- No meaningful payload
- Identical ID and sequence numbers

This ruled out traditional payload-based exfiltration or steganography. The structure suggested a covert channel using metadata.

### 2. Hypothesis: Timing Channel

The data might be encoded using time intervals between successive ICMP packets — a covert timing channel.

### 3. Timestamp Extraction

Extracted the relative timestamps of ICMP Echo Request packets using:

```
tshark -r SilentSignal.pcap -Y "icmp.type == 8" -T fields -e frame.time_relative > times.txt
```

### 4. Delta Calculation

Using a simple script, computed the differences between consecutive timestamps:

```python
intervals = [round(timestamps[i] - timestamps[i-1]) for i in range(1, len(timestamps))]
```

### 5. ASCII Decoding

Interpreted each interval as an ASCII character using:

```python
''.join([chr(i) for i in intervals])
```

This yielded the following string:

```
SVBRG{...}
```

---
