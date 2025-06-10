## CTF Forensics Challenge: Extracting the Flag from `EndOfTheLine.wav`

### Challenge Type

Forensics

---

### Steps to Retrieve the Flag

#### 1. Reverse the audio

```sh
sox EndOfTheLine.wav reversed.wav reverse
ffplay reversed.wav
```

#### 6. Retrieve the Flag

Send the reverse audio through morse code decoder.

```sh
SVBRG{...}
```

