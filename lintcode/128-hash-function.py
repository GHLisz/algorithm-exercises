class Solution:
    """
    @param key: A String you should hash
    @param HASH_SIZE: An integer
    @return an integer
    """
    def hashCode(self, key, HASH_SIZE):
        # write your code here
        accum = 0
        for i in key:
            accum = (accum*33 + ord(i)) % HASH_SIZE
        return accum
