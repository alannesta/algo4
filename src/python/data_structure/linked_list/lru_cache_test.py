import unittest
from data_structure.linked_list.lru_cache import lru, lru_ordered_dict, lru_custom_deque, lru_final_evolution


class Test(unittest.TestCase):
    def setUp(self):
        self.lru = lru(5)
        self.lru_od = lru_ordered_dict(5)
        self.lru_custom = lru_custom_deque(5)
        self.lru_fe = lru_final_evolution(5)

    def test_lru_api(self):
        self.lru.set('kaka', 'lala')
        self.lru.set('gaga', 'kaka')
        self.lru.set('kaka', 'haha')
        self.lru.set('lala', 'lala')
        self.lru.set('haha', 'jaja')
        self.lru.set('fafa', 'aaaa')

        assert (self.lru.get('kaka') == 'haha')

        self.lru.set('new_key', 'new_val')  # add a new key to the cache

        assert (self.lru.get('gaga') is None)

        assert (self.lru.cache[0] == 'new_key')

        self.lru.get('kaka')

        assert (self.lru.cache[0] == 'kaka')
        assert (self.lru.cache[4] == 'lala')
        assert (len(self.lru.cache) == 5)

    def test_lru_od_api(self):
        self.lru_od.set('kaka', 'lala')
        self.lru_od.set('gaga', 'kaka')
        self.lru_od.set('kaka', 'haha')
        self.lru_od.set('lala', 'lala')
        self.lru_od.set('haha', 'jaja')
        self.lru_od.set('fafa', 'aaaa')

        assert (self.lru_od.get('kaka') == 'haha')

        self.lru_od.set('new_key', 'new_val')  # add a new key to the cache

        assert (self.lru_od.get('gaga') is None)

        self.lru_od.get('lala')
        self.lru_od.set('new_key2', 'new_val')
        assert (self.lru_od.get('haha') is None)

        print(self.lru_od.cache)

    def test_lru_custom(self):
        self.lru_custom.set('kaka', 'lala')
        self.lru_custom.set('gaga', 'kaka')
        self.lru_custom.set('kaka', 'haha')
        self.lru_custom.set('lala', 'lala')
        self.lru_custom.set('haha', 'jaja')
        self.lru_custom.set('fafa', 'aaaa')

        assert (self.lru_custom.get('kaka') == 'haha')

        self.lru_custom.set('new_key', 'new_val')  # add a new key to the cache

        assert (self.lru_custom.get('gaga') is None)

        assert (self.lru_custom.cache.get(0) == 'new_key')

        self.lru_custom.get('kaka')

        assert (self.lru_custom.cache.get(0) == 'kaka')
        assert (self.lru_custom.cache.get(4) == 'lala')
        assert (self.lru_custom.cache.size == 5)


    def test_lru_final_evolution(self):
        self.lru_fe.set('kaka', 'lala')
        self.lru_fe.set('gaga', 'kaka')
        self.lru_fe.set('kaka', 'haha')
        self.lru_fe.set('lala', 'lala')
        self.lru_fe.set('haha', 'jaja')
        self.lru_fe.set('fafa', 'aaaa')

        assert (self.lru_fe.get('kaka') == 'haha')

        self.lru_fe.set('new_key', 'new_val')  # add a new key to the cache

        assert (self.lru_fe.get('gaga') is None)

        assert (self.lru_fe.cache.get(0) == ('new_key', 'new_val'))

        self.lru_fe.get('kaka')

        assert (self.lru_fe.cache.get(0) == ('kaka', 'haha'))
        assert (self.lru_fe.cache.get(4) == ('lala', 'lala'))
        assert (self.lru_fe.cache.size == 5)
