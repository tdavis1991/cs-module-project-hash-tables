class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None



class LinkedList:
    def __init__(self):
        self.head = None
        self.items = 0
        
    def find(self, key):
        current_node = self.head

        while current_node is not None:
            # Compare the current node with what we are looking for
            if current_node.key == key:
                return current_node.value
            current_node = current_node.next

        return None

    def insert_at_head(self, node):
        self.items += 1
        # Link the node to the current HEAD
        node.next = self.head
        # Set head pointer to new node
        self.head = node

    def delete(self, key):
        self.items -= 1
        # Handle the case where the node to delete is the HEAD
        if key == self.head.key:
            self.head = self.head.next
            return self.head
    
        prev = None
        curr = self.head

        while curr is not None:
            # loop until we find the right key
            if curr.key == key:
                # found it!
                prev.next = curr.next
                return curr.value
                
            # move the pointers over
            prev = curr    
            curr = curr.next
    



# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity=MIN_CAPACITY):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.number_of_items = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.storage / self.number_of_items



    def fnv1(self, key, seed=0):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        FNV_prime = 1099511628211
        offset_basis = 14695981039346656037

        hash = offset_basis + seed
        for char in key:
            hash = hash * FNV_prime
            hash = hash ^ ord(char)
        return hash


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381
        for x in key:
            hash = (( hash << 5) + hash) + ord(x)
        return hash & 0xFFFFFFFF


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        self.number_of_items += 1
        new_node = HashTableEntry(key, value)

        index = self.hash_index(key)
        if self.storage[index] == None:
            self.storage[index] = LinkedList()
            self.storage[index].head = new_node

        self.storage[index].insert_at_head(new_node)


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)

        if self.storage[index] == None:
            return None
        
        return self.storage[index].delete(key)


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        #hash key to find index value should be at
        index = self.hash_index(key)
        

        #if None:
        if self.storage[index] == None:
            #return None
            return None
        #if the index is a linked list run find method associated with LL class
        
        return self.storage[index].find(key)
            #if found
                #return value
            #if not found return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        new_value_array = []
        self.capacity = new_capacity
        
        



new_hash = HashTable()
new_hash.put('mustang', '420hp')
print(new_hash.get('mustang'))


