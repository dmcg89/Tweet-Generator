#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        Running time: O(n^2) Why and under what conditions?  O(n^2) in all cases since it
        iterates entirely every time"""
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        Running time: O(n^2) Why and under what conditions?  Same logic as before"""
        # bucket_values = []
        all_values = []
        # Loop through all buckets
        for bucket in self.buckets:
        # Collect all values in each bucket
            for key, value in bucket.items():
                all_values.append(value)
        return all_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        Running time: O(n) Why and under what conditions?  Loops through all buckets once"""
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        TODO: Running time: O(n) Why and under what conditions?  Loops through all
        buckets once"""
        # Loop through all buckets
        length = 0
        for bucket in self.buckets:
        # Count number of key-value entries in each bucket
            length += bucket.size
        return length

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        Running time: O(1) or O(n) Why and under what conditions?  Depends on where
        the desired key is located.  See find logic"""
        # Find bucket where given key belongs
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # Check if key-value entry exists in bucket
        entry = bucket.find(lambda key_value: key_value[0] == key)
        # Check out the entry that returned -- is it None?
        if entry is None:
            return False
        else: # entry is not none
            return True
        # shorter version
        # return entry is not None

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        Running time: O(1) or O(n) Why and under what conditions?  Same logic as
        above function"""
        # Find bucket where given key belongs
        # bucket = self.buckets[self._bucket_index(key)]
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # Check if key-value entry exists in bucket
        entry = bucket.find(lambda key_value: key_value[0] == key)
        # If found, return value associated with given key
        if entry is not None:   # Found
            return entry[1]    # Get value at index 1
        # Otherwise, raise error to tell user get failed
        else:
            raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        Running time: O(1) or O(l) (l being average length of buckets).
        Why and under what conditions?
        Best case O(1) item is located near head of list.  Otherwise O(l) (find) + O(l) (delete) = O(2*l)
        simplifies to O(l) if item is near tail of list"""
        # Find bucket where given key belongs (first two lines on almost every step)
        index = self._bucket_index(key)  # O(1)
        bucket = self.buckets[index]     # O(1)
        # Check if key-value entry exists in bucket
        entry = bucket.find(lambda key_value: key_value[0] == key)  # O(l) worst case
        # If found, update value associated with given key
        if entry is not None:   # found
            bucket.delete(entry)    # O(l) worst case
        # Otherwise, insert given key-value entry into bucket
        entry = (key, value)    # O(1)
        bucket.append(entry)    # O(1)

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        Running time: Best case O(1) if item is near head of list or O(n)
        if item is near tail of list."""
        # Find bucket where given key belongs
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # Check if key-value entry exists in bucket
        entry = bucket.find(lambda key_value: key_value[0] == key)
        # If found, delete entry associated with given key
        if entry is not None: # found
            bucket.delete(entry)
        # Otherwise, raise error to tell user delete failed
        else:
            raise KeyError('Key not found: {}'.format(key))


def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10), ('I', 2), ('y', 2)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))
    print(ht.values())

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
