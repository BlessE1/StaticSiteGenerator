from markdown_to_blocks import markdown_to_blocks

def extract_title(markdown):
   blocks = markdown_to_blocks(markdown)

   for block in blocks:
      if block.startswith("# "):
         return block.lstrip("# ").rstrip(" ")

   raise Exeception("Error: No title (h1 header) found")
