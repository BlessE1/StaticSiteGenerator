from textnode import TextNode, TextType

def convert_to_text_nodes(nodes, text_type):
   nodes[0] = TextNode(nodes[0], TextType.TEXT)
   nodes[1] = TextNode(nodes[1], text_type)
   nodes[2] = TextNode(nodes[2], TextType.TEXT)

def split_node_delimiter(node, delimiter, text_type):
   if node.text.count(delimiter) % 2 != 0:
      raise Exception("Invalid Markdown Syntax: Matching closing delimiter not found in text")

   nodes = node.text.split(delimiter, 2)
   convert_to_text_nodes(nodes, text_type)

   while any(delimiter in node.text for node in nodes):
      new_nodes = nodes[-1].text.split(delimiter, 2)
      del nodes[-1]
      convert_to_text_nodes(new_nodes, text_type)
      nodes.extend(new_nodes)

   return nodes

def split_nodes_delimiter(old_nodes, delimiter, text_type):
   new_nodes = []

   for node in old_nodes:
      if node.text_type != TextType.TEXT or delimiter not in node.text:
         new_nodes.append(node)
         continue

      new_nodes.extend(split_node_delimiter(node, delimiter, text_type))

   return list(filter(lambda node: node.text != "", new_nodes))
