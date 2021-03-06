from __future__ import absolute_import

from .Binary import Binary

class Intersection(Binary):

    def __init__(self):
        """
        Stores the components for the Intersection
        in member variables self.comp1 self.comp2.
        """
        Binary.__init__(self)
        return

    def __str__(self):
        """
        Returns a string containing the SCAD
        code for implementing an intersection.
        """
        return """intersection() {{
    {0!s}
    {1!s}
}}""".format(self.comp1, self.comp2)
