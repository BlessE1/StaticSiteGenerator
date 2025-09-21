from copy_source_to_dest import copy_from_source_to_destination
from generate_pages_recursive import generate_pages_recursive

def main():
   copy_from_source_to_destination(".", "static", "public")
   generate_pages_recursive("content", "template.html", "public")

if __name__ == "__main__":
   main()
