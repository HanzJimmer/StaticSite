# import unittest

# from htmlnode import HTMLNode, LeafNode, ParentNode

# class TestHTMLNode(unittest.TestCase):
#     def test_h1_HTMLNode(self):
#         node = HTMLNode("h1", "This should be a header")
#         self.assertEqual(str(node), "Current Node:\ntag = h1\nvalue = This should be a header\nchildren = None\nprops = ")
    
#     def test_link_HTMLNode(self):
#         node = HTMLNode("a", "This is the link test", None, {"href": "zombocom"})
#         self.assertEqual(str(node), 'Current Node:\ntag = a\nvalue = This is the link test\nchildren = None\nprops =  href="zombocom"')
              
#     def test_header_with_children(self):
#         node2 = HTMLNode("p", "this is the paragraph test")
#         node3 = HTMLNode("a", "This is the link test", None, {"href": "zombocom"})
#         node1 = HTMLNode("h1", "This should be a header with children", [node2, node3])
#         self.assertEqual(str(node1), 'Current Node:\ntag = h1\nvalue = This should be a header with children\nchildren = [Current Node:\ntag = p\nvalue = this is the paragraph test\nchildren = None\nprops = , Current Node:\ntag = a\nvalue = This is the link test\nchildren = None\nprops =  href="zombocom"]\nprops = ')

# class TestLeafNode(unittest.TestCase):
#     def test_leaf_to_html_link(self):
#         node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
#         self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

#     def test_leaf_to_html_p(self):
#         node = LeafNode("p", "Hello, world!")
#         self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

#     def test_leaf_to_html_no_tag(self):
#         node = LeafNode(None, "Raw Text")
#         self.assertEqual(node.to_html(), "Raw Text")

#     def test_leaf_to_html_no_value(self):
#         node = LeafNode("p", None)
#         with self.assertRaises(ValueError):
#             print(node.to_html())

# class TestParentNode(unittest.TestCase):
#     def test_to_html_with_children(self):
#         child_node = LeafNode("span", "child")
#         parent_node = ParentNode("div", [child_node])
#         self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

#     def test_to_html_with_grandchildren(self):
#         grandchild_node = LeafNode("b", "grandchild")
#         child_node = ParentNode("span", [grandchild_node])
#         parent_node = ParentNode("div", [child_node])
#         self.assertEqual(
#             parent_node.to_html(),
#             "<div><span><b>grandchild</b></span></div>",
#         )

#     def test_to_html_missing_tag(self):
#         child_node = LeafNode("p", "paragraph")
#         parent_node = ParentNode(None, [child_node])
#         with self.assertRaises(ValueError):
#             print(parent_node.to_html())

#     def test_to_html_missing_children(self):
#         parent_node = ParentNode("h1", [])
#         with self.assertRaises(ValueError):
#             print(parent_node.to_html())

#     def test_to_html_with_multiple_children(self):
#         child1_node = LeafNode("b", "child1")
#         child2_node = LeafNode("span", "child2")
#         parent_node = ParentNode("div", [child1_node, child2_node])
#         self.assertEqual(
#             parent_node.to_html(),
#             "<div><b>child1</b><span>child2</span></div>",
#         )
    
#     def test_to_html_link_child(self):
#         child_node = LeafNode("a", "child", {"href": "www.google.com"})
#         parent_node = ParentNode("div", [child_node])
#         self.assertEqual(parent_node.to_html(), '<div><a href="www.google.com">child</a></div>') 

# if __name__ == "__main__":
#     unittest.main()