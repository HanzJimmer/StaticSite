import unittest

from textnode import TextNode, TextType, text_node_to_html


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
        
class TestTxtToHtml(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.PLAIN_TEXT)
        html_node = text_node_to_html(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This will be bold", TextType.BOLD_TEXT)
        html_node = text_node_to_html(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This will be bold")

    def test_italic(self):
        node = TextNode("This will be italic", TextType.ITALIC_TEXT)
        html_node = text_node_to_html(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This will be italic")

    def test_code(self):
        node = TextNode("This will be code", TextType.CODE_TEXT)
        html_node = text_node_to_html(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This will be code")

    def test_link(self):
        node = TextNode("This will be link", TextType.LINK, "www.google.com")
        html_node = text_node_to_html(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This will be link")
        self.assertEqual(html_node.props, {"href": "www.google.com"})

    def test_image(self):
        node = TextNode("This will be image", TextType.IMAGE, "www.google.com")
        html_node = text_node_to_html(node) 
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"alt": "This will be image", "src": "www.google.com"})

if __name__ == "__main__":
    unittest.main()