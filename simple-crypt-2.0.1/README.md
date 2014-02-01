simple-crypt
============

Simple, secure encryption and decryption for Python 2.7 and 3 (now on
[pypi](http://pypi.python.org/pypi/simple-crypt)).

This provides two functions, which encrypt and decrypt data, delegating all
the hard work to the [pycrypto](https://www.dlitz.net/software/pycrypto)
library (which must also be installed).

Examples
--------

The two calls:

```python
from simplecrypt import encrypt, decrypt

ciphertext = encrypt(password, 'my secret')
plaintext = decrypt(password, ciphertext)
```

A simple Python 3 program:

```python
from binascii import hexlify
from getpass import getpass
from sys import stdin

from simplecrypt import encrypt, decrypt

# read the password from the user (without displaying it)
password = getpass("password: ")

# read the (single line) plaintext we will encrypt
print("message: ")
message = stdin.readline()

# encrypt the plaintext.  we explicitly convert to bytes first (optional)
ciphertext = encrypt(password, message.encode('utf8'))

# the ciphertext plaintext is bytes, so we display it as a hex string
print("ciphertext: %s" % hexlify(ciphertext))

# now decrypt the plaintext (using the same salt and password)
plaintext = decrypt(password, ciphertext)

# the decrypted plaintext is bytes, but we can convert it back to a string
print("plaintext: %s" % plaintext)
print("plaintext as string: %s" % plaintext.decode('utf8'))
```

Which, when run, produces something like the following (the actual encrypted
message will be different each time, as a random IV is used for each message):

```
password: ******

message:
hello world
ciphertext: b'736300005d14f6bb1c9692c2e09322b6bf11c5c7dea73f3b9047b1d26a50c05925e2237096d313a34a5e93becd587781738b1213129537b3f1b2724dd224acdc'
plaintext: b'hello world\n'
plaintext as string: hello world
```

Also, it's perhaps worth noting that the overhead (the extra length of the
encrypted data, compared to the message) is constant.  It looks a lot here,
because the message is very small, but for most practical uses should not be
an issue.

Algorithms
----------

The algorithms used follow the recommendations at
http://www.daemonology.net/blog/2009-06-11-cryptographic-right-answers.html,
as far as I can tell:

* The password is expanded to two 256 bit keys using PBKDF2 with a 128 bit
  random salt, SHA256, and 10,000 iterations.

* AES256 CTR mode is used to encrypt the data with one key.  The first 64 bits
  of the salt are used as a message nonce (of half the block size); the
  incremental part of the counter uses the remaining 64 bits (see section B.2
  of http://csrc.nist.gov/publications/nistpubs/800-38a/sp800-38a.pdf).

* An encrypted messages starts with a 4 byte header ("sc" in ASCII followed
  by two zero bytes).

* An SHA256 HMAC (of header, salt, and encrypted message) is calculated using
  the other key.

* The final message consists of the header, salt, encrypted data, and HMAC,
  concatenated in that order.

* On decryption, the header is checked and the HMAC validated before
  decryption.

The [entire implementation is here](https://github.com/andrewcooke/simple-crypt/blob/master/src/simplecrypt/__init__.py).

Discussion and criticism of the design can be found on
[HN](http://news.ycombinator.com/item?id=4962983)
([also](https://news.ycombinator.com/item?id=6194102)),
[codereview.stackexchange](http://codereview.stackexchange.com/questions/19910/simple-crypto-library-in-python-correct-and-secure)
and
[crypto.stackexchange](http://crypto.stackexchange.com/questions/5843/future-proof-versioning-and-validation).
Grateful thanks to all commentators (particularly marshray); mistakes remain
mine.

Latest News
-----------

Release 2.0 should be fully compatible with 1.0 on Python 3 (same API and
identical results).  However, thanks to [d10n](https://github.com/d10n) it now
also supports Python 2.7 (tested with Python 2.7.5, 3.0.1 and 3.3.2).

I (Andrew Cooke) am not sure Python 2.7 support is such a good idea.  You should
really use something like [keyczar](http://www.keyczar.org/).  But there seems
to be a demand for this, so better the devil you know...

Warnings
--------

1. The whole idea of encrypting with a password is not so smart these days.
   If you think you need to do this, try reading about Google's
   [keyczar](http://www.keyczar.org/) which instead uses a keystore
   (unfortunately, at the time of writing, keyczar does not support Python 3,
   as far as I can tell, but that should change soon).

2. When you call these routines the password is stored in memory as a Python
   string.  This means that malicious code running on the same machine might
   be able to read the password (or even that the password could be written to
   swap space on disk).  One way to reduce the risk is to have the crypto part
   of your code run as a separate process that exists for a limited time.

(c) 2012 Andrew Cooke, andrew@acooke.org;
2013 [d10n](https://github.com/d10n), david@bitinvert.com.
Released into the public domain for any use, but with absolutely no warranty.
