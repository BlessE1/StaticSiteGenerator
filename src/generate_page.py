import os
from extract_title import extract_title
from markdown_to_html_node import markdown_to_html_node

def generate_page(from_path, template_path, dest_path, basepath):
   print(f"Generating page from {from_path} to {dest_path} using {template_path}")

   with open(os.path.abspath(from_path)) as file:
      md = file.read()

   with open(os.path.abspath(template_path)) as file:
      template = file.read()

   html = markdown_to_html_node(md).to_html()
   title = extract_title(md)
   template = template.replace("{{ Title }}", title).replace("{{ Content }}", html)
   template = template.replace('href="/', f'href="{basepath}').replace('src="/', f'src="{basepath}')

   if not os.path.exists(os.path.abspath(dest_path)):
      os.makedirs(os.path.dirname(os.path.abspath(dest_path)), exist_ok=True)

   with open(os.path.abspath(dest_path), "w") as file:
      file.write(template)
