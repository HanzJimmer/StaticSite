from textnode import TextType, TextNode, text_node_to_html_node
from htmlnode import ParentNode
import re
from enum import Enum

# this function takes a list of nodes, a delimiter, and text_type enum 
# and returns the a new list of TextNodes with their type
# (used for bold, italic, and code blocks)
# helper function in text_to_nodes
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN_TEXT:
            new_nodes.append(node)
            continue
        text_list = node.text.split(delimiter)
        if len(text_list) % 2 == 0:
            raise Exception("Missing delimiter")
        for i in range(len(text_list)):
            if not text_list[i]:
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(text_list[i], TextType.PLAIN_TEXT))
            if i % 2 != 0:
                new_nodes.append(TextNode(text_list[i], text_type))
    return new_nodes

# helper function for split_nodes_image
def extract_markdown_images(text):
    tuple_list = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return tuple_list

# function takes a list of nodes and returns a new list
# that includes TextNodes with IMAGE blocks
# helper function in text_to_nodes
def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN_TEXT:
            new_nodes.append(node)
            continue
        image_meta_data = extract_markdown_images(node.text)
        if not image_meta_data:
            new_nodes.append(node)
            continue
        next_string = node.text
        for image in image_meta_data:
            split_node = next_string.split(f"![{image[0]}]({image[1]})", maxsplit=1)
            next_string = split_node[1]
            if split_node[0] != "":
                new_nodes.append(TextNode(split_node[0], TextType.PLAIN_TEXT))
            new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
        if next_string and next_string != "":
            new_nodes.append(TextNode(next_string, TextType.PLAIN_TEXT))
    return new_nodes

# helper function for split_nodes_link
def extract_markdown_links(text):
    tuple_list = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return tuple_list

# function takes a list of nodes and returns a new list
# that includes TextNodes with LINK blocks 
# helper function in text_to_nodes
def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN_TEXT:
            new_nodes.append(node)
            continue
        image_meta_data = extract_markdown_links(node.text)
        if not image_meta_data:
            new_nodes.append(node)
            continue
        next_string = node.text
        for image in image_meta_data:
            split_node = next_string.split(f"[{image[0]}]({image[1]})", maxsplit=1)
            next_string = split_node[1]
            if split_node[0] != "":
                new_nodes.append(TextNode(split_node[0], TextType.PLAIN_TEXT))
            new_nodes.append(TextNode(image[0], TextType.LINK, image[1]))
        if next_string and next_string != "":
            new_nodes.append(TextNode(next_string, TextType.PLAIN_TEXT))
    return new_nodes

# takes a string of text (i.e. a MD block) and returns the block as a list of TextNodes
def text_to_nodes(text):    
    final_nodes = [TextNode(text, TextType.PLAIN_TEXT)]
    final_nodes = split_nodes_delimiter(final_nodes, "**", TextType.BOLD_TEXT)
    final_nodes = split_nodes_delimiter(final_nodes, "_", TextType.ITALIC_TEXT)
    final_nodes = split_nodes_delimiter(final_nodes, "`", TextType.CODE_TEXT)
    final_nodes = split_nodes_image(final_nodes)
    final_nodes = split_nodes_link(final_nodes)
    return final_nodes

# takes a markdown file and returns it split into a list of blocks
def markdown_to_blocks(markdown):
    blocked_strings = markdown.split("\n\n")
    final_blocks = []
    for block in blocked_strings:
        block_text = block.strip()
        if block_text:
            final_blocks.append(block_text)
    return final_blocks

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"

# this takes a block (e.g. from markdown_to_blocks) and returns the type of block it is
def block_to_block_type(block):
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

# This takes a block's text and returns string value of the block's tag for use in HTMLNode creation 
def get_html_tag(block_text):
    block_type = block_to_block_type(block_text)
    match block_type:
        case BlockType.HEADING:
            if block_text.startswith("# "):
                return "h1"
            elif block_text.startswith("## "):
                return "h2"
            elif block_text.startswith("### "):
                return "h3"
            elif block_text.startswith("#### "):
                return "h4"
            elif block_text.startswith("##### "):
                return "h5"
            elif block_text.startswith("###### "):
                return "h6"
        case BlockType.CODE:
            return "code"
        case BlockType.QUOTE:
            return "blockquote"
        case BlockType.UNORDERED_LIST:
            return "ul"
        case BlockType.ORDERED_LIST:
            return "ol"
        case BlockType.PARAGRAPH:
            return "p"
             
# this will be a series of functions to call based on blocktype
def heading_to_html_node(block):
    tag = get_html_tag(block)
    text = block.lstrip("#").lstrip()
    node_list = text_to_nodes(text)
    return ParentNode(tag, node_list)

def paragraph_to_html_node(block):
    tag = get_html_tag(block)
    text = block.replace("\n", " ")
    node_list = text_to_nodes(text)
    return ParentNode(tag, node_list)

def code_to_html_node(block):
    tag = get_html_tag(block)
    #need to strip the ``` characters from beginning and end and then return a TextNode run through text_node_to_html_node 
    # text = block.lstrip("#").lstrip()
    #node_list = text_to_nodes(text)
    #return ParentNode(tag, node_list)
    pass

def quote_to_html_node(block):
    pass

def ul_to_html_node(block):
    pass

def ol_to_html_node(block):
    pass

# takes the md text and returns HTML node list used as children for parent node
def text_to_children(text):
    text_node_list = text_to_nodes(text)
    html_node_list = []
    for node in text_node_list:
        html_node_list.append(text_node_to_html_node(node))
    return html_node_list

def markdown_to_html_node(markdown_text): 
    md_blocks = markdown_to_blocks(markdown_text)
    parent_blocks = []
    for block in md_blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.HEADING:
            node = None
        elif block_type == BlockType.CODE:
            node = None
        elif block_type == BlockType.PARAGRAPH:
            node = None
        elif block_type == BlockType.QUOTE:
            node = None
        elif block_type == BlockType.UNORDERED_LIST:
            node = None
        elif block_type == BlockType.ORDERED_LIST:
            node = None
        else:
            continue
        parent_blocks.append(node)
    return ParentNode("div", None, parent_blocks)

def html_node_to_html(top_node):
    return top_node.to_html()