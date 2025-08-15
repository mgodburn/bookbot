def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(char_count_dict):
    # Sort by count (value) in descending order
    return dict(sorted(char_count_dict.items(), key=lambda item: item[1], reverse=True))