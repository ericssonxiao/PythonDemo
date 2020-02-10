from datetime import datetime
from collections import namedtuple
from hashed_seq import HashedSeq
from doubly_linked_list import DoublyLinkedList
import threading

class LRUCache:
    """ This is LRU Cache.
    """
    lock = threading.RLock()

    def __init__(self, capacity=60, expiration=60):
        self.capacity = capacity
        self.expiration = expiration

    def __hash__(self):
        pass

    def get_cache(self):
        LRUCache.lock.acquire()
        pass
        LRUCache.lock.release()
    
    def set_cache(self):
        LRUCache.lock.acquire()
        pass
        LRUCache.lock.release()

    def del_cache(self):
        LRUCache.lock.acquire()
        pass
        LRUCache.lock.release()

    def cache_info(self):
        LRUCache.lock.acquire()
        pass
        LRUCache.lock.release()

    def cache_clean(self):
        LRUCache.lock.acquire()
        pass
        LRUCache.lock.release()