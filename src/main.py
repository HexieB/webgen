from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode


def main():
    node = TextNode("This is some anchor text", "link", "https://www.boot.dev")
    print(node)

main()
# This is a test for the TextNode class