import unittest
from textnode import TextNode, TextType
from helpfunctions import *

class TestBlockToHTML(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )





# class TestDelimiterParser(unittest.TestCase):
#     def test_code_delimiter(self):
#         node = TextNode("This is text with a `code block` word", TextType.PLAIN_TEXT)
#         new_nodes = split_nodes_delimiter([node], "`", TextType.CODE_TEXT)
#         self.assertEqual(new_nodes, [
#             TextNode("This is text with a ", TextType.PLAIN_TEXT),
#             TextNode("code block", TextType.CODE_TEXT),
#             TextNode(" word", TextType.PLAIN_TEXT),
#             ]
#         )

#     def test_bold_delimiter(self):
#         node = TextNode("This is text with a **bold block** word", TextType.PLAIN_TEXT)
#         new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
#         self.assertEqual(new_nodes, [
#             TextNode("This is text with a ", TextType.PLAIN_TEXT),
#             TextNode("bold block", TextType.BOLD_TEXT),
#             TextNode(" word", TextType.PLAIN_TEXT),
#             ]
#         )

#     def test_italic_delimiter(self):
#         node = TextNode("This is text with a _italic block_ word", TextType.PLAIN_TEXT)
#         new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC_TEXT)
#         self.assertEqual(new_nodes, [
#             TextNode("This is text with a ", TextType.PLAIN_TEXT),
#             TextNode("italic block", TextType.ITALIC_TEXT),
#             TextNode(" word", TextType.PLAIN_TEXT),
#             ]
#         )

#     def test_delimiter_start(self):
#         node = TextNode("_This starts with an italic_ block of text", TextType.PLAIN_TEXT)
#         new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC_TEXT)
#         self.assertEqual(new_nodes, [
#             TextNode("This starts with an italic", TextType.ITALIC_TEXT),
#             TextNode(" block of text", TextType.PLAIN_TEXT),
#             ]
#         )

#     def test_missing_delmiter(self):
#         node = TextNode("This is **missing a delimiter", TextType.PLAIN_TEXT)
#         with self.assertRaises(Exception):
#             new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)

#     def test_delim_bold_double(self):
#         node = TextNode(
#             "This is text with a **bolded word** and **another**", TextType.PLAIN_TEXT
#         )
#         new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
#         self.assertListEqual(
#             [
#                 TextNode("This is text with a ", TextType.PLAIN_TEXT),
#                 TextNode("bolded word", TextType.BOLD_TEXT),
#                 TextNode(" and ", TextType.PLAIN_TEXT),
#                 TextNode("another", TextType.BOLD_TEXT),
#             ],
#             new_nodes,
#         )

#     def test_delim_bold_ital(self):
#         node = TextNode(
#             "This is text with a **bolded word** and _italic_", TextType.PLAIN_TEXT
#         )
#         new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
#         new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC_TEXT)
#         self.assertListEqual(
#             [
#                 TextNode("This is text with a ", TextType.PLAIN_TEXT),
#                 TextNode("bolded word", TextType.BOLD_TEXT),
#                 TextNode(" and ", TextType.PLAIN_TEXT),
#                 TextNode("italic", TextType.ITALIC_TEXT),
#             ],
#             new_nodes,
#         )

# class TestImageAndURL(unittest.TestCase):
#     def test_extract_markdown_images(self):
#         matches = extract_markdown_images(
#             "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
#         )
#         self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

#     def test_extract_markdown_links(self):
#         matches = extract_markdown_links(
#             "This is text with an link [to boot dev](https://www.boot.dev)"
#         )
#         self.assertListEqual([("to boot dev", "https://www.boot.dev")], matches)

#     def test_extract_markdown_multiple_images(self):
#         matches = extract_markdown_images(
#             "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
#         )
#         self.assertListEqual([("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan","https://i.imgur.com/fJRm4Vk.jpeg")], matches)

#     def test_split_image(self):
#         node = TextNode(
#             "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
#             TextType.PLAIN_TEXT,
#         )
#         new_nodes = split_nodes_image([node])
#         self.assertListEqual(
#             [
#                 TextNode("This is text with an ", TextType.PLAIN_TEXT),
#                 TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
#             ],
#             new_nodes,
#         )

#     def test_split_image_single(self):
#         node = TextNode(
#             "![image](https://www.example.COM/IMAGE.PNG)",
#             TextType.PLAIN_TEXT,
#         )
#         new_nodes = split_nodes_image([node])
#         self.assertListEqual(
#             [
#                 TextNode("image", TextType.IMAGE, "https://www.example.COM/IMAGE.PNG"),
#             ],
#             new_nodes,
#         )

#     def test_split_images(self):
#         node = TextNode(
#             "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
#             TextType.PLAIN_TEXT,
#         )
#         new_nodes = split_nodes_image([node])
#         self.assertListEqual(
#             [
#                 TextNode("This is text with an ", TextType.PLAIN_TEXT),
#                 TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
#                 TextNode(" and another ", TextType.PLAIN_TEXT),
#                 TextNode(
#                     "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
#                 ),
#             ],
#             new_nodes,
#         )

#     def test_split_links(self):
#         node = TextNode(
#             "This is text with a [link](https://boot.dev) and [another link](https://wikipedia.org) with text that follows",
#             TextType.PLAIN_TEXT,
#         )
#         new_nodes = split_nodes_link([node])
#         self.assertListEqual(
#             [
#                 TextNode("This is text with a ", TextType.PLAIN_TEXT),
#                 TextNode("link", TextType.LINK, "https://boot.dev"),
#                 TextNode(" and ", TextType.PLAIN_TEXT),
#                 TextNode("another link", TextType.LINK, "https://wikipedia.org"),
#                 TextNode(" with text that follows", TextType.PLAIN_TEXT),
#             ],
#             new_nodes,
#         )

# class TestHigherFunctions(unittest.TestCase):
#     def test_text_to_node(self):
#         text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
#         node_list = text_to_nodes(text)
#         self.assertListEqual(
#             [
#                 TextNode("This is ", TextType.PLAIN_TEXT),
#                 TextNode("text", TextType.BOLD_TEXT),
#                 TextNode(" with an ", TextType.PLAIN_TEXT),
#                 TextNode("italic", TextType.ITALIC_TEXT),
#                 TextNode(" word and a ", TextType.PLAIN_TEXT),
#                 TextNode("code block", TextType.CODE_TEXT),
#                 TextNode(" and an ", TextType.PLAIN_TEXT),
#                 TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
#                 TextNode(" and a ", TextType.PLAIN_TEXT),
#                 TextNode("link", TextType.LINK, "https://boot.dev"),
#             ], node_list
#         )

#     def test_markdown_to_blocks(self):
#         md = """
# This is **bolded** paragraph

# This is another paragraph with _italic_ text and `code` here
# This is the same paragraph on a new line

# - This is a list
# - with items
# """
#         blocks = markdown_to_blocks(md)
#         self.assertListEqual(
#             blocks,
#             [
#                 "This is **bolded** paragraph",
#                 "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
#                 "- This is a list\n- with items",
#             ],
#         )

#     def test_markdown_to_blocks_extra_newlines(self):
#         md = """
# This is **bolded** paragraph


# This is another paragraph with _italic_ text and `code` here
# This is the same paragraph on a new line




# - This is a list
# - with items
# """
#         blocks = markdown_to_blocks(md)
#         self.assertListEqual(
#             blocks,
#             [
#                 "This is **bolded** paragraph",
#                 "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
#                 "- This is a list\n- with items",
#             ],
#         )

#     def test_markdown_to_blocks_white_space_block(self):
#         md = """
# This is **bolded** paragraph

# This is another paragraph with _italic_ text and `code` here
# This is the same paragraph on a new line

                       

# - This is a list
# - with items
# """
#         blocks = markdown_to_blocks(md)
#         self.assertListEqual(
#             blocks,
#             [
#                 "This is **bolded** paragraph",
#                 "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
#                 "- This is a list\n- with items",
#             ],
#         )

#     def test_markdown_to_blocks_empty_string_block(self):
#         md = """
# This is **bolded** paragraph

# This is another paragraph with _italic_ text and `code` here
# This is the same paragraph on a new line



# - This is a list
# - with items
# """
#         blocks = markdown_to_blocks(md)
#         self.assertListEqual(
#             blocks,
#             [
#                 "This is **bolded** paragraph",
#                 "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
#                 "- This is a list\n- with items",
#             ],
#         )

#     def test_block_to_block_type(self):
#         md = """
# This is **bolded** paragraph

# # This is another paragraph with _italic_ text and `code` here
# # This is the same paragraph on a new line

# ```
# This is a paragraph of code
# ```

# > This is a quote block

# - This is a list
# - with items

# 1. Finally, this is 
# 2. an ordered list
# """
#         blocks = markdown_to_blocks(md)
#         results = []
#         for block in blocks:
#             results.append(block_to_block_type(block))
        
#         self.assertListEqual(
#             results,
#             [BlockType.PARAGRAPH, BlockType.HEADING, BlockType.CODE, BlockType.QUOTE, BlockType.UNORDERED_LIST, BlockType.ORDERED_LIST]
#         )

#     def test_block_to_block_type_wrong_code(self):
#         md = """
# This is **bolded** paragraph

# # This is another paragraph with _italic_ text and `code` here
# # This is the same paragraph on a new line

# ```This is a paragraph of code```

# > This is a quote block

# - This is a list
# - with items

# 1. Finally, this is 
# 2. an ordered list
# """
#         blocks = markdown_to_blocks(md)
#         results = []
#         for block in blocks:
#             results.append(block_to_block_type(block))
        
#         self.assertListEqual(
#             results,
#             [BlockType.PARAGRAPH, BlockType.HEADING, BlockType.PARAGRAPH, BlockType.QUOTE, BlockType.UNORDERED_LIST, BlockType.ORDERED_LIST]
#         )