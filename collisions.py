# how full does a hash table have to get before a collision happens?
# depends on hashing method. a good method that has good distribution. islow

import hashlib
import random

# generate random keys and put them in hash table until a collision


def hash_function(key):
    return int(hashlib.md5(str(key).encode()).hexdigest()[-8:], 16) & 0xffffffff
    # takes a string returns a number


def how_may_before_collision(buckets, loops):
    for i in range(loops):
        tries = 0
        tried = set()
        while True:
            random_key = random.random()
            index = hash_function(random_key) % buckets

            if index not in tried:
                tried.add(index)
                tries += 1
            else:
                break

        print(f"{buckets} buckets, {tries} hashes before collision. Capacity: {tries / buckets * 100:.1f}% full")


how_may_before_collision(30, 10)
