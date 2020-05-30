from math import sqrt

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return -1

def isprime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        for i in range(1, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
    return True

# Transforms a string into a sequence of values not greater than pq=33
def serialize(plaintext):
    words = []
    for byte in bytes(plaintext, 'UTF-8'):
        words.extend([byte & 0x1f, byte >> 5])
    return words

def deserialize(words):
    plaintext = []
    # Trick to read two words at a time. https://stackoverflow.com/a/16789817
    it = iter(words)
    for word in it:
        plaintext.append(word + (next(it) << 5))
    return plaintext

def generate_keypair():
    p = 11
    q = 3
    n = p * q
    d = 7
    e = 3

    return ((e, n), (d, n))

def encrypt(msg_plaintext, pubkey):
    e, n = pubkey
    msg_serialized = serialize(msg_plaintext)
    msg_ciphertext = [pow(c, e, n) for c in msg_serialized]
    return msg_ciphertext

def decrypt(msg_ciphertext, privkey):
    d, n = privkey
    msg_serialized = [(pow(c, d, n)) for c in msg_ciphertext]
    msg_plaintext = [chr(c) for c in deserialize(msg_serialized)]
    return ''.join(msg_plaintext)