from enum import Enum
from htmlnode import LeafNode
import re
class TextType(Enum):
    """Enum for text types."""
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    LINK = "link"
    IMAGE = "image"
    CODE = "code"

class TextNode():
    def __init__(self, text: str, text_type, url: str = None):
        self.text = text
        self.text_type = TextType(text_type)
        self.url = url
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
    
def text_node_to_html_node(textnode):
    match textnode.text_type:
        case TextType.TEXT:
            return LeafNode(None, textnode.text)
        case TextType.BOLD:
            return LeafNode("b", textnode.text)
        case TextType.ITALIC:
            return LeafNode("i", textnode.text)
        case TextType.LINK:
            if textnode.url is None:
                raise ValueError("Link text node must have a URL")
            if textnode.text is None:
                raise ValueError("Link text node must have text")
            if textnode.text == "":
                raise ValueError("Link text node must have non-empty text")
            if textnode.url == "":
                raise ValueError("Link text node must have non-empty URL")
            return LeafNode("a", textnode.text, {"href": textnode.url})
        case TextType.IMAGE:
            if textnode.url is None:
                raise ValueError("Image text node must have a URL")
            return LeafNode("img", None, {"src": textnode.url})
        case TextType.CODE:
            if textnode.text is None:
                raise ValueError("Code text node must have text")
            if textnode.text == "":
                raise ValueError("Code text node must have non-empty text")
            return LeafNode("code", textnode.text)
        case _:
            raise ValueError(f"Unknown text type: {textnode.text_type}")
        
def extract_markdown_images(text: str):
    """finds image links in raw markdown text using regex. returns a list of tuples alt text and then urls"""
    
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return [(match[0], match[1]) for match in matches]

def extract_markdown_links(text: str):
    """finds links in raw markdown text using regex. returns a list of tuples anchor text and then urls"""
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return [(match[0], match[1]) for match in matches]
