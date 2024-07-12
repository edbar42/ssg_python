from textnode import TextNode
from htmlnodes import HTMLNode


def main():
    text_node1 = TextNode("Hello, world", "bold", None)
    text_node2 = TextNode("boot.dev", "italic", "https://boot.dev")

    print(text_node1)
    print(text_node2)

    htmlNode1 = HTMLNode(
        "p", "Hello, world", None, {"style": "font-weight: bold"}
    )

    print(htmlNode1)


if __name__ == "__main__":
    main()
