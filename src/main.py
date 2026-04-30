import os
import shutil

def main():
    static_path = "static"
    public_path = "public"
    copy_static(static_path, public_path)

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

main()