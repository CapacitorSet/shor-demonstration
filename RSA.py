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

# Transforms a string into a sequence of values not greater than 8
def serialize(plaintext):
    words = []
    for byte in bytes(plaintext, 'UTF-8'):
        words.extend([byte & 7, (byte >> 3) & 7, byte >> 6])
    return words

def deserialize(words):
    plaintext = []
    # Trick to read N words at a time. https://stackoverflow.com/a/16789817
    it = iter(words)
    for word in it:
        plaintext.append(word + (next(it) << 3) + (next(it) << 6))
    return plaintext

def generate_keypair(p, q):
    n = p * q
    d = 7
    e = 3

    return ((e, n), (d, n))

def encrypt(msg_plaintext, pubkey):
    e, n = pubkey
    # We encrypt one byte at a time, so as not to exceed N=pq as long as we
    # don't pick an absurdly tiny value
    msg_serialized = serialize(msg_plaintext)
    msg_ciphertext = [pow(c, e, n) for c in msg_serialized]
    return bytes(msg_ciphertext)

def decrypt(msg_ciphertext, privkey):
    d, n = privkey
    msg_serialized = [(pow(c, d, n)) for c in msg_ciphertext]
    msg_plaintext = [chr(c) for c in deserialize(msg_serialized)]
    return ''.join(msg_plaintext)