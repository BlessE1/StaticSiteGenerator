import sys
from copy_source_to_dest import copy_from_source_to_destination
from generate_pages_recursive import generate_pages_recursive

def main():
   basepath = sys.argv[1] if len(sys.argv) == 2 else "/"
   copy_from_source_to_destination(".", "static", "docs")
   generate_pages_recursive("content", "template.html", "docs", basepath)

if __name__ == "__main__":
   main()
