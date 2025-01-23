class HashTable:

    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_slots()

    def create_slots(self):
        return [[] for i in range(self.size)]

    def insert(self, key, val):
        intended_slot = hash(key) % self.size
        for pair in self.hash_table[intended_slot]:
            if key in pair:
                temp_list = list(pair)
                temp_list.append(val)
                self.hash_table[intended_slot] = [tuple(temp_list)]
                return self.hash_table
        else:
            self.hash_table[intended_slot].append((key,val))
        return self.hash_table

    def delete(self, key):
        intended_slot = hash(key) % self.size
        for pair in self.hash_table[intended_slot]:
            if key in pair:
                self.hash_table[intended_slot].remove(pair)
        return self.hash_table

    def search(self, key):
        intended_slot = hash(key) % self.size
        for pair in self.hash_table[intended_slot]:
            if key in pair:
                return pair

if __name__ == "__main__":
    h = HashTable(10)
    h.insert("banana", 'json.8')
    h.insert("banana", 'json.10')
    h.insert("lmfao", "json.11")
    h.delete("lmfao")
    print(h.search("banana"))
    print(h.hash_table)

