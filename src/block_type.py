import re
from enum import Enum

class BlockType(Enum):
   PARAGRAPH = "paragraph"
   HEADING = "heading"
   CODE = "code"
   QUOTE = "quote"
   UNORDERED_LIST = "unordered_list"
   ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
   if re.search(r"^#{1,6} .+", block, re.DOTALL):
      return BlockType.HEADING
   elif re.search(r"^`{3}.+`{3}$", block, re.DOTALL):
      return BlockType.CODE
   elif all([line.startswith(">") for line in block.split("\n")]):
      return BlockType.QUOTE
   elif all([line.startswith("- ") for line in block.split("\n")]):
      return BlockType.UNORDERED_LIST
   elif all([line.startswith(f"{num + 1}. ") for num, line in enumerate(block.split("\n"))]):
      return BlockType.ORDERED_LIST

   return BlockType.PARAGRAPH
