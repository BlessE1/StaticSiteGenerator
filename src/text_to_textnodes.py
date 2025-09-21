from split_nodes_delimiter import split_nodes_delimiter
from split_nodes_image_link import split_nodes_image, split_nodes_link
from textnode import TextNode, TextType

def text_to_textnodes(text):
   node = TextNode(text, TextType.TEXT)

   text_nodes = split_nodes_image([node])
   text_nodes = split_nodes_link(text_nodes)
   text_nodes = split_nodes_delimiter(text_nodes, "`", TextType.CODE)
   text_nodes  = split_nodes_delimiter(text_nodes, "**", TextType.BOLD)
   text_nodes  = split_nodes_delimiter(text_nodes, "_", TextType.ITALIC)

   return text_nodes
