"""Write a single Wi-Fi network name to the output file.

The name is an original joke, written for this bounty: a divorcé(e)
whose Wi-Fi outlasted the marriage -- a character, an event, and a
punchline in 29 characters, well under the 32-character limit.
"""

import os
import sys

# Original Wi-Fi name, 29 characters: "This WiFi survived my divorce".
NAME = "This WiFi survived my divorce"


def output_path() -> str:
    if len(sys.argv) > 1:
        return sys.argv[1]
    return os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main() -> None:
    assert 1 <= len(NAME) <= 32, "name must be 1-32 characters"
    assert NAME.strip(), "name must not be only whitespace"
    assert "\n" not in NAME and "\r" not in NAME, "name must be one line"
    path = output_path()
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(NAME)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
