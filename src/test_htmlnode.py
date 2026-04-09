import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_h1_HTMLNode(self):
        node = HTMLNode("h1", "This should be a header")
        self.assertEqual(str(node), "Current Node:\ntag = h1\nvalue = This should be a header\nchildren = None\nprops = ")
    
    def test_link_HTMLNode(self):
        node = HTMLNode("a", "This is the link test", None, {"href": "zombocom"})
        self.assertEqual(str(node), 'Current Node:\ntag = a\nvalue = This is the link test\nchildren = None\nprops =  href="zombocom"')
              
    def test_header_with_children(self):
        node2 = HTMLNode("p", "this is the paragraph test")
        node3 = HTMLNode("a", "This is the link test", None, {"href": "zombocom"})
        node1 = HTMLNode("h1", "This should be a header with children", [node2, node3])
        self.assertEqual(str(node1), 'Current Node:\ntag = h1\nvalue = This should be a header with children\nchildren = [Current Node:\ntag = p\nvalue = this is the paragraph test\nchildren = None\nprops = , Current Node:\ntag = a\nvalue = This is the link test\nchildren = None\nprops =  href="zombocom"]\nprops = ')

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_link(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Raw Text")
        self.assertEqual(node.to_html(), "Raw Text")

    def test_leaf_to_html_no_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            print(node.to_html())

if __name__ == "__main__":
    unittest.main()