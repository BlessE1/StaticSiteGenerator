import re
from markdown_to_blocks import markdown_to_blocks
from block_type import BlockType, block_to_block_type
from text_to_textnodes import text_to_textnodes
from text_node_to_html_node import text_node_to_html_node
from htmlnode import ParentNode
from textnode import TextNode, TextType

def text_to_children(text):
   text_nodes = []

   for line in text.split("\n"):
      text_nodes.extend(text_to_textnodes(line))

   children = list(map(text_node_to_html_node, text_nodes))
   return children

def markdown_to_html_node(markdown):
   blocks = markdown_to_blocks(markdown)
   html_children = []

   for block in blocks:
      block_type = block_to_block_type(block)
      html_node = None

      match block_type:
         case BlockType.PARAGRAPH:
            para_lines = block.split("\n")
            children = text_to_children(" ".join(para_lines))
            html_node = ParentNode("p", children)

         case BlockType.HEADING:
            html_node = ParentNode(f"h{block[:6].count('#')}", text_to_children(block.lstrip("# ")))

         case BlockType.CODE:
            code_node = TextNode(block.lstrip("`\n").rstrip("`"), TextType.CODE)
            html_node = ParentNode("pre", [text_node_to_html_node(code_node)])

         case BlockType.QUOTE:
            quote_lines = []

            for line in block.split("\n"):
               line = line.lstrip("> ")
               if line == "":
                 continue
               quote_lines.append(line)

            children = text_to_children(" ".join(quote_lines))
            html_node = ParentNode("blockquote", children)

         case BlockType.UNORDERED_LIST:
            children = []

            for line in block.split("\n"):
               line = line.lstrip("- ")
               text_nodes = text_to_children(line)
               list_item = ParentNode("li", [*text_nodes])
               children.append(list_item)

            html_node = ParentNode("ul", children)

         case BlockType.ORDERED_LIST:
            children = []

            for line in block.split("\n"):
               line = re.sub(r"^\d+\. ", "", line)
               text_nodes = text_to_children(line)
               list_item = ParentNode("li", [*text_nodes])
               children.append(list_item)

            html_node = ParentNode("ol", children)

      html_children.append(html_node)

   return ParentNode("div", html_children)
