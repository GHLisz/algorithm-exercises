class Tower:
    """
    @param: i: An integer from 0 to 2
    """

    def __init__(self, i):
        # create three towers
        self.disks = []

    """
    @param: d: An integer
    @return: nothing
    """

    def add(self, d):
        # Add a disk into this tower
        if len(self.disks) > 0 and self.disks[-1] <= d:
            print "Error placing disk %s" % d
        else:
            self.disks.append(d)

    """
    @param: t: a tower
    @return: nothing
    """

    def move_top_to(self, t):
        # Move the top disk of this tower to the top of t.
        t.add(self.disks.pop())

    """
    @param: n: An integer
    @param: destination: a tower
    @param: buffer: a tower
    @return: nothing
    """

    def move_disks(self, n, destination, buffer):
        # Move n Disks from this tower to destination by buffer tower
        if n > 0:
            self.move_disks(n - 1, buffer, destination)
            self.move_top_to(destination)
            buffer.move_disks(n - 1, destination, self)

    """
    @return: Disks
    """

    def get_disks(self):
        # write your code here
        return self.disks


"""
Your Tower object will be instantiated and called as such:
towers = [Tower(0), Tower(1), Tower(2)]
for i in xrange(n - 1, -1, -1): towers[0].add(i)
towers[0].move_disks(n, towers[2], towers[1])
print towers[0], towers[1], towers[2]
"""
