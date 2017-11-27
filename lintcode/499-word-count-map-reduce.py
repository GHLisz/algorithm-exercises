class WordCount:
    # @param {str} line a text, for example "Bye Bye see you next"
    def mapper(self, _, line):
        # Write your code here
        # Please use 'yield key, value'
        words = line.split()
        for idx, word in enumerate(words):
            yield word, 1

    # @param key is from mapper
    # @param values is a set of value with the same key
    def reducer(self, key, values):
        # Write your code here
        # Please use 'yield key, value'
        sum_ = 0
        for val in values:
            sum_ += val
        yield key, sum_
