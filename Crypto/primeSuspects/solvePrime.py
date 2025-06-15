from Crypto.Util.number import * # type: ignore

import base64

# Given values
n = 102064367305175623005003367803963735992210717721719563218760598878897771063019
e = 65537
c = 66538583650087752653364112099322882026083260207958188191147900019851853145222

# Factored from n
p = 305875545128432734240552595430305723491
q = 333679396508538352589365351078683227609

# Compute phi(n)
phi = (p - 1) * (q - 1)

# Compute private key d
d = inverse(e, phi) # type: ignore

# Decrypt the ciphertext
m = pow(c, d, n)
plaintext = long_to_bytes(m) # type: ignore


# Print raw decrypted message
print("Decrypted message:", plaintext)

# Decode base64 with fixed padding
try:
    b64_data = plaintext.decode()
    padding = 4 - (len(b64_data) % 4)
    if padding != 4:
        b64_data += '=' * padding

    decoded = base64.b64decode(b64_data)
    print("Flag:", decoded.decode())
except Exception as err:
    print("Base64 decode error:", err)
