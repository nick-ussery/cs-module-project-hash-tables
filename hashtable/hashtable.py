class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        # establishes an empty list with length desired
        self.data = [None for i in range(capacity)]
        self.size = 0  # number of full slots

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity  # returns max slots

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.size / self.get_num_slots()

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        for char in key:
            hash = (hash * 33) + ord(char)
        return hash

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        # copied from wiki

        hash = 5381
        for x in key:
            hash = ((hash << 5) + hash) + ord(x)
        return hash & 0xFFFFFFFF

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        bucket = self.hash_index(key)

        if self.data[bucket] is None:
            self.data[bucket] = HashTableEntry(key, value)
            self.size += 1

            if self.get_load_factor() > 0.7:
                self.resize(self.capacity * 2)
        else:
            current = self.data[bucket]

            while current.next is not None and current.key != key:
                current = current.next

            # Overwrite existing value
            if current.key == key:
                current.value = value
            else:
                # Key does not exist, so must be added
                current.next = HashTableEntry(key, value)
                self.size += 1

                if self.get_load_factor() > 0.7:
                    self.resize(self.capacity * 2)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        bucket = self.hash_index(key)

        current = self.data[bucket]

        if current is None:
            print('The key was not found.')
        elif current.key == key:
            self.data[bucket] = current.next
            self.size -= 1
        else:
            while current.next is not None and current.next.key != key:
                current = current.next

            if current.next.key == key:
                current.next = current.next.next
                self.size -= 1
            else:
                print('The key was not found.')

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        bucket = self.hash_index(key)

        if self.data[bucket] is not None:
            current = self.data[bucket]

            while current is not None and current.key != key:
                current = current.next

            if current:
                return current.value
            else:
                return None
        else:
            return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        self.capacity = new_capacity  # sets new capacity
        # creates the list with None values
        new_storage = [None for i in range(new_capacity)]

        for linked_list in self.data:
            current = linked_list

            while current is not None:  # need to copy old list to this new list first
                bucket = self.hash_index(current.key)

                if new_storage[bucket] is None:
                    # if the new location is empty(which it should be) puts the next entry into this slot
                    new_storage[bucket] = HashTableEntry(
                        currrent.key, current.value)
                else:
                    # otherwise overrides the slot with the already existing HashTableEntry
                    new_current = new_storage[bucket]

                    while new_current.next is not None:  # cycle to end of list
                        new_current = new_current.next

                    new_current.next = HashTableEntry(
                        current.key, current.value)

                current = current.next

        self.data = new_storage  # sets the list to be the resized enw list


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
