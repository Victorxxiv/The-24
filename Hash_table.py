class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        for kv in self.table[index]:
            if kv[0] == key:
                kv[1] = value
                return
            self.table[index].append([key, value])

    def get(self, key):
        index = self.hash_function(key)
        for kv in self.table[index]:
            if kv[0] == key:
                return kv[1]
        return None

    def delete(self, key):
        index = self.hash_function(key)
        for i, kv in enumerate(self.table[index]):
            if kv[0] == key:
                del self.table[index][i]
                return


# Example
ht = HashTable()
ht.insert("name", "Ragnar")
print(ht.get("name"))
ht.delete("name")
print(ht.get("name"))
