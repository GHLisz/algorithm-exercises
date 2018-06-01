class Solution:
    """
    @param cpdomains: a list cpdomains of count-paired domains
    @return: a list of count-paired domains
    """
    def subdomainVisits(self, cpdomains):
        # Write your code here
        import collections
        ans = collections.Counter()
        for domain in cpdomains:
            count, domain = domain.split()
            count = int(count)
            frags = domain.split('.')
            for i in range(len(frags)):
                ans[".".join(frags[i:])] += count
        return [f"{ct} {dom}" for dom, ct in ans.items()]
