from textnode import TextNode, TextType
from extract_markdown_images_links import extract_markdown_images, extract_markdown_links

def convert_to_text_nodes(nodes, text_type, extract):
   nodes[0] = TextNode(nodes[0], TextType.TEXT)
   nodes[1] = TextNode(nodes[1], TextType.TEXT)
   nodes.insert(1, TextNode(extract[0], text_type, extract[1]))

def split_node(node, text_type):
   if node.text.count("[") != node.text.count("]") or node.text.count("(") != node.text.count(")"):
      raise Exception("Invalid Markdown Syntax: Matching closing brakcet not found.")

   extracted = extract_markdown_images(node.text) if text_type == TextType.IMAGE else extract_markdown_links(node.text)

   nodes = node.text.split(f"{'!'*bool(text_type == TextType.IMAGE)}[{extracted[0][0]}]({extracted[0][1]})", 1)
   convert_to_text_nodes(nodes, text_type, extracted[0])

   for extract in extracted[1:]:
      new_nodes = nodes[-1].text.split(f"{'!'*bool(text_type == TextType.IMAGE)}[{extract[0]}]({extract[1]})", 1)
      del nodes[-1]
      convert_to_text_nodes(new_nodes, text_type, extract)
      nodes.extend(new_nodes)

   return nodes

def split_nodes_image(old_nodes):
   new_nodes = []

   for node in old_nodes:
      if node.text_type != TextType.TEXT or extract_markdown_images(node.text) == []:
         new_nodes.append(node)
         continue

      new_nodes.extend(split_node(node, TextType.IMAGE))

   return list(filter(lambda node: node.text != "", new_nodes))

def split_nodes_link(old_nodes):
   new_nodes = []

   for node in old_nodes:
      if node.text_type != TextType.TEXT or extract_markdown_links(node.text) == []:
         new_nodes.append(node)
         continue

      new_nodes.extend(split_node(node, TextType.LINK))

   return list(filter(lambda node: node.text != "", new_nodes))
