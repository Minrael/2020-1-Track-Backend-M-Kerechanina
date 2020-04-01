class LRUCache():

    def __init__(self, capacity=10):
        self.cache = {}
        self.time_used = []
        self.capacity = capacity

    def get(self, key):
        if key in self.cache:
            self.time_used.remove(key)
            self.time_used.append(key)
            return self.cache[key]
        else:
            self.time_used.append(key)
            return ''

    def set(self, key, value):
        if key in self.cache:
            self.time_used.remove(key)
        else:
            if (len(self.time_used) == self.capacity):
                self.cache.pop(self.time_used[0])
                self.time_used.pop(0)
        self.time_used.append(key)
        self.cache[key] = value

    def del_elem(self, key):
        if key in self.cache:
            self.cache.pop(key)
            self.time_used.remove(key)

def main():
    cache = LRUCache(100)
    cache.set('Jesse', 'Pinkman')
    cache.set('Walter', 'White')
    cache.set('Jesse', 'James')

    print(cache.get('Jesse'))
    cache.del_elem('Walter')
    print(cache.get('Walter'))
    return


if __name__ == "__main__":
    main()


