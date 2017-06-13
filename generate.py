#!/usr/bin/env python3
#- * -coding: utf - 8 - * -
from pprint import pprint as p
from json import load
with open("rules.json") as f:
    RULES = load(f)


def main():
    p(RULES)


if __name__ == "__main__":
    main()
