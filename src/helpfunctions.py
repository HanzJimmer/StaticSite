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
    
# using regex, search for ![] and return the stuff inside as the alt_text, then search for \(w+\)
# should return a list of tuples (alt_text, imgage_url)
# text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
# print(extract_markdown_images(text))
# [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]


def extract_markdown_links(text):
    tuple_list = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return tuple_list

# returns list of tuples (anchor_text, url)
# text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
# print(extract_markdown_links(text))
# [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]