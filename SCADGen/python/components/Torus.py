from __future__ import absolute_import

import xml.etree.ElementTree as ET
from .Component import Component

class Torus(Component):

    def __init__(self, xml_elem):
        """
        Gets the major and minor axes dimensions
        for the Torus from its line in the XML file.
        The contents of this line are acessed through
        the xml.etree.ElementTree.Element object, xml_elem.
        """
        self.major = xml_elem.get("major") 
        self.minor = xml_elem.get("minor")

    def __str__(self):
        """
        Returns a string containing the SCAD code
        for instantiating this Torus object.
        """
        return "Torus({0!s}, {1!s});".format(self.major, self.minor)
