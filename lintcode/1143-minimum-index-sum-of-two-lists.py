class Solution:
    """
    @param list1: a list of strings
    @param list2: a list of strings
    @return: the common interest with the least list index sum
    """

    def findRestaurant(self, list1, list2):
        # Write your code here
        dic = {item: 0 for item in (set(list1) & set(list2))}
        for lis in (list1, list2):
            for i, v in enumerate(lis):
                if v in dic:
                    dic[v] += i
        least = min(dic.values())
        return [k for k, v in dic.items() if v == least]
