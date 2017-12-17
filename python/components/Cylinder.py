import xml.etree.ElementTree as ET

class Cylinder:

    def __init__(self, xml_elem):
        """
        Gets radius and height for the cylinder from
        the atrributes from its XML line. These attributes are
        accessed using the xml.etree.ElementTree.Element object, xml_elem.
        """
        self.radius = xml_elem.get("radius")
        self.height = xml_elem.get("height")
        return

    def __str__(self):
        """
        Returns a string containing the SCAD
        code for this cylinder object.
        """
        return "cylinder(h = {0!s}, r = {1!s});".format(self.height, self.radius)
