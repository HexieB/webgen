from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType, text_node_to_html_node

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    """
    Takes a list of "old nodes", a delimiter, and a text type. 
    It should return a new list of nodes, where any markdown "text" type nodes in the input list are (potentially) split 
    into multiple nodes based on the syntax

    """
    new_nodes = []
    for node in old_nodes:
        if isinstance(node, TextNode) and node.text_type != TextType.TEXT:
            # If a matching closing delimiter is not found, just raise an exception with a helpful error message, "invalid Markdown syntax."
            if node.text.count(delimiter) % 2 != 0:
                raise ValueError("Invalid Markdown syntax.")
            # Split the text into parts based on the delimiter   
            parts = node.text.split(delimiter)
            # Create new nodes for each part
            for i, part in enumerate(parts):
                if i % 2 == 0:
                    # Even index: regular text
                    new_nodes.append(TextNode(part, TextType.TEXT))
                else:
                    # Odd index: styled text
                    new_nodes.append(TextNode(part, text_type))
        else:
            # If the node is not a TextNode or doesn't match the text type, just append it as is
            new_nodes.append(node)
    return new_nodes
            

