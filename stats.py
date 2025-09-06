def word_count(book_text):
    return len(book_text.split())


def count_characters(book_text):
    characters = {}
    for char in book_text.lower():
        if char.isalpha():
            characters[char] = characters.get(char, 0) + 1

    result = []
    for key, value in characters.items():
        result.append({"char": key, "num": value})

    return result
