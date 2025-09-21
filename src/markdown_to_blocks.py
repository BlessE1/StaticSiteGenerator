def markdown_to_blocks(markdown):
   blocks = map(str.strip, markdown.split("\n\n"))

   return list(filter(lambda block: block != "", blocks))

