import textnode as tn


def main():
    text_node1 = tn.TextNode("Hello, world", "bold", None)
    text_node2 = tn.TextNode("boot.dev", "italic", "https://boot.dev")

    print(text_node1)
    print(text_node2)


if __name__ == "__main__":
    main()
