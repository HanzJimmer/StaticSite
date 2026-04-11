from textnode import TextType, TextNode
import re

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

def extract_markdown_images(text):
    tuple_list = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return tuple_list
    
def extract_markdown_links(text):
    tuple_list = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return tuple_list

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