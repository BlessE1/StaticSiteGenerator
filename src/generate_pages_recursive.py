import os
from generate_page import generate_page
from copy_source_to_dest import delete_dir_contents

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
   with os.scandir(dir_path_content) as curr_dir:
      for item in curr_dir:
         if item.is_dir():
            new_dest_dir_path = os.path.join(dest_dir_path, item.name)
            generate_pages_recursive(item.path, template_path, new_dest_dir_path, basepath)

         if item.is_file():
            new_dest_dir_path = os.path.join(dest_dir_path, item.name.replace(".md", ".html"))
            generate_page(item.path, template_path, new_dest_dir_path, basepath)
