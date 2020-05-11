import unittest
from data_structure.linked_list.lru_cache import lru, lru_ordered_dict


class Test(unittest.TestCase):
    def setUp(self):
        self.lru = lru(5)
        self.lru_od = lru_ordered_dict(5)

    def test_lru_api(self):
        self.lru.set('kaka', 'lala')
        self.lru.set('gaga', 'kaka')
        self.lru.set('kaka', 'haha')
        self.lru.set('lala', 'lala')
        self.lru.set('haha', 'jaja')
        self.lru.set('fafa', 'aaaa')

        assert (self.lru.get('kaka') == 'haha')

        self.lru.set('new_key', 'new_val')  # add a new key to the cache

        assert(self.lru.get('gaga') is None)

        assert(self.lru.cache[0] == 'new_key')

        self.lru.get('kaka')

        assert(self.lru.cache[0] == 'kaka')
        assert(self.lru.cache[4] == 'lala')
        assert(len(self.lru.cache) == 5)

    def test_lru_od_api(self):
        self.lru_od.set('kaka', 'lala')
        self.lru_od.set('gaga', 'kaka')
        self.lru_od.set('kaka', 'haha')
        self.lru_od.set('lala', 'lala')
        self.lru_od.set('haha', 'jaja')
        self.lru_od.set('fafa', 'aaaa')

        assert (self.lru_od.get('kaka') == 'haha')

        self.lru_od.set('new_key', 'new_val')  # add a new key to the cache

        assert(self.lru_od.get('gaga') is None)

        self.lru_od.get('lala')
        self.lru_od.set('new_key2', 'new_val')
        assert(self.lru_od.get('haha') is None)


        print(self.lru_od.cache)
