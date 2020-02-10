class HashedSeq(list):
    __slots__ = 'hashvalue'

    def __init__(self, tup, hash=hash):
        self[:] = tup
        self.hashvalue = hash(tup)

    def __hash__(self):
        return self.hashvalue

    def __contains__(self, key):
        return key in self
    
    def make_key(self, key, len=len):
        return HashedSeq(key)
    
    def get_key(self):
        pass