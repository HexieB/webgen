from enum import Enum
class TextType(Enum):
    """Enum for text types."""
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    LINK = "link"
    IMAGE = "image"
    CODE = "code"

class TextNode():
    def __init__(self, text: str, text_type, url: str = None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url