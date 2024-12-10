"""
This script generates a markdown link with URL encoded text.
"""

import sys
import urllib.parse


def generate_markdown_link(text, bumper="Placeholder:"):
    """
    Generates a markdown link with URL encoded text.

    Args:
        text: The text to display in the link and use for URL encoding.

    Returns:
        A string containing the markdown link. with URL encoded text.
    """
    encoded_text = urllib.parse.quote_plus(f"{bumper} {text}")
    return f"![{bumper} {text}](https://placehold.co/600x400?text={encoded_text})"


if __name__ == "__main__":
    # Pass the second argument as the bumper text if it exists
    if len(sys.argv) > 2:
        markdown_link = generate_markdown_link(text=sys.argv[1], bumper=sys.argv[2])
        print(markdown_link)
    # Otherwise, use only the first argument
    elif len(sys.argv) > 1:
        markdown_link = generate_markdown_link(text=sys.argv[1])
        print(markdown_link)
    else:
        print("Please provide a text string as the first argument.")
