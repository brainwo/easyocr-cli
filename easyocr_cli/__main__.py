#!/usr/bin/env python

import argparse
from argparse import Namespace
from easyocr import easyocr, Reader
from easyocr_cli import languages


parser = argparse.ArgumentParser(
    description='A CLI program to interact with EasyOCR library'
)
parser.add_argument(
    'image',
    help='location of image',
)
parser.add_argument(
    '--list-langs',
    action='store_true',
    help='print all supported languages',
)


def print_list_lang() -> None:
    lang_list = easyocr.all_lang_list
    lang_list.sort()
    print('List of supported languages:')
    print(
        "\n".join(map(lambda x: f'{x} {languages.all_langs_name.get(x, "(Unnamed language)")}', lang_list)))
    print()
    print('For more info please visit https://www.jaided.ai/easyocr/')


def main() -> None:
    args: Namespace = parser.parse_args()
    if args.list_langs:
        print_list_lang()
    else:
        reader = Reader(['en'])
        reader.readtext(args.image)


if __name__ == "__main__":
    main()
