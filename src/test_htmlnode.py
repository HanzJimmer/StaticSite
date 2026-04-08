import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test1(self):
        print(HTMLNode("h1", "This should be a header"))

    def test2(self):
        print(HTMLNode("p", "this is the paragraph test"))
    
    def test3(self):
        print(HTMLNode("a", "This is the link test", None, {"href": "zombocom"}))
              
    def test4(self):
        node2 = HTMLNode("p", "this is the paragraph test")
        node3 = HTMLNode("a", "This is the link test", None, {"href": "zombocom"})
        node1 = HTMLNode("h1", "This should be a header with children", [node2, node3])
        print(node1)

if __name__ == "__main__":
    unittest.main()