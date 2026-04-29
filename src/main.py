from textnode import TextNode, TextType
import os
import shutil

def main():
    Node1 = TextNode("This is my text", TextType.PLAIN_TEXT)
    print(Node1)

def copy_static(src, dest):
    dest_address = dest
    shutil.rmtree(dest)
    os.mkdir(dest_address)
    copy_list = os.listdir(src)
    for item in copy_list:
        shutil.copy(src, dest)
        if os.path.isdir(item):
            os.mkdir(item) #need to edit this to create new dir in the correct filepath
            copy_static(item, )

main()