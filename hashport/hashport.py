#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib


def hashport(text: str) -> int:
    # Use the built-in hashlib to create a sha256 hash
    sha256_hash = hashlib.sha256(text.encode('utf-8')).hexdigest()

    # Convert the hash to an integer
    hash_int = int(sha256_hash, 16)

    # Scale the integer to the desired range (49152 to 65535)
    min_value = 49152
    max_value = 65535
    scaled_int = min_value + (hash_int % (max_value - min_value + 1))

    return scaled_int
