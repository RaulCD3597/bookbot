from typing import Dict, List


def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as file:
        file_contents = file.read()
        print_report(book_path, file_contents)


def count_words(text: str) -> int:
    return len(text.split())


def character_count(text: str) -> Dict[str, int]:
    characters = {}
    for c in text:
        character = c.lower()
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1
    return characters


def dict_to_list(char_dict: Dict[str, int]) -> List[dict]:
    return [
        {"char": key, "count": value}
        for key, value in char_dict.items()
        if key.isalpha()
    ]


def print_report(book_path: str, book_content: str):
    print(f"--- Begin report of {book_path} ---")
    print(f"{count_words(book_content)} words found in the document")
    print()
    char_list = dict_to_list(character_count(book_content))
    char_list.sort(reverse=True, key=lambda dict: dict["count"])
    for char in char_list:
        character = char["char"]
        amount = char["count"]
        print(f"The '{character}' character was found {amount} times")
    print("--- End report ---")


main()
