#!/usr/bin/env python3

import sys
import markdown

def main(argv):
    if len(argv) != 2:
        print("Usage: {} data.md".format(argv[0]))
        exit(64)

    with open(argv[1], 'rt', encoding="utf-8") as stream:
        html = markdown.markdown(stream.read(), extensions=['attr_list'])

    print(html)

if __name__ == "__main__":
   main(sys.argv)
