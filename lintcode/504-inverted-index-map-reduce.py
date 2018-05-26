"""
Definition of Document
class Document:
    def __init__(self, id, cotent):
        self.id = id
        self.content = content
"""


class InvertedIndex:

    # @param {Document} value is a document
    def mapper(self, _, value):
        # Write your code here
        # Please use 'yield key, value' here
        id_, content = value.id, value.content
        words = content.split(' ')
        if not words: return
        for word in words:
            yield word, id_

    # @param key is from mapper
    # @param values is a set of value with the same key
    def reducer(self, key, values):
        # Write your code here
        # Please use 'yield key, value' here
        if not key: return
        yield key, sorted(set(values))
