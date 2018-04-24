class TwoSum:
    """
    @param: number: An integer
    @return: nothing
    """
    def __init__(self):
        self.dic = {}

    def add(self, number):
        # write your code here
        if number in self.dic:
            self.dic[number] += 1
        else:
            self.dic[number] = 1
    """
    @param: value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        # write your code here
        for key in self.dic.keys():
            another = value - key
            if another == key and self.dic[key] > 1:
                return True
            elif another != key and another in self.dic:
                return True
        return False
