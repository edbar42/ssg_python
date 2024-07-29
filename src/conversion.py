# Conversion from HTML to Markdown and vice-versa
from htmlnodes import LeafNode


def text_node_to_html_node(text_node):
    valid_txt_node_types = ["text", "bold", "italic", "code", "link", "image"]
    if text_node.text_type not in valid_txt_node_types:
        raise Exception("Invalid text node type")

    if text_node.text_type == "text":
        return LeafNode(value=text_node.text)
    elif text_node.text_type == "bold":
        return LeafNode(tag="b", value=text_node.text)
    elif text_node.text_type == "italic":
        return LeafNode(tag="i", value=text_node.text)
    elif text_node.text_type == "code":
        return LeafNode(tag="code", value=text_node.text)
    elif text_node.text_type == "link":
        return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
    elif text_node.text_type == "image":
        return LeafNode(
            tag="img", value="", props={"src": text_node.url, "alt": text_node.text}
        )
