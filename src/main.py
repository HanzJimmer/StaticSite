import os
import shutil
from helpfunctions import markdown_to_html_node

def main():
    static_path = "static"
    public_path = "public"
    copy_static(static_path, public_path)
    
    generate_page("content/index.md", "template.html", "public/index.html")

def copy_static(src, dest):
    if os.path.exists(dest):
        shutil.rmtree(dest)
    os.mkdir(dest)

    copy_list = os.listdir(src)
    for item in copy_list:
        new_src = os.path.join(src, item)
        new_dest = os.path.join(dest, item)
        if os.path.isdir(new_src):
            os.mkdir(new_dest)
            copy_static(new_src, new_dest)
        else:
            shutil.copy(new_src, new_dest)

def extract_title(markdown):
    if not markdown.startswith("# "):
        raise Exception
    header = (markdown.split("\n"))[0]
    header = header.removeprefix("# ")
    return header

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    read_file = None
    with open(from_path) as f:
        read_file = f.read()
    template = None
    with open(template_path) as f:
        template = f.read()
    my_html_string = markdown_to_html_node(read_file).to_html()
    print(read_file)
    head = extract_title(read_file)

    template = template.replace("{{ Title }}", head)
    template = template.replace("{{ Content }}", my_html_string)
    if (not os.path.exists(dest_path)):
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    
    with open(dest_path, "w") as f:
        f.write(template)

main()