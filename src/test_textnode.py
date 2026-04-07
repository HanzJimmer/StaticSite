import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def test_noteq(self):
        node = TextNode("italic", TextType.ITALIC_TEXT)
        node2 = TextNode("url", TextType.LINK, "www.google.com")
        self.assertNotEqual(node, node2)

    def test_almosteq(self):
        node = TextNode("This is one text", TextType.PLAIN_TEXT)
        node2 = TextNode("this is another text", TextType.PLAIN_TEXT)
        self.assertNotEqual(node, node2)
        

if __name__ == "__main__":
    unittest.main()