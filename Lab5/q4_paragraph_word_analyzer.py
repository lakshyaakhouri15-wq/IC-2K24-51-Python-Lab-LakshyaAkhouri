"""Analyze word frequencies, rankings, and word groups in a paragraph."""

import string


def normalize_paragraph(text):
    """Lowercase text and remove punctuation while keeping letters and digits."""
    punctuation_table = str.maketrans("", "", string.punctuation)
    return text.lower().translate(punctuation_table)


def main():
    paragraph = input("Enter a paragraph: ")
    cleaned_paragraph = normalize_paragraph(paragraph)
    word_list = cleaned_paragraph.split()

    if not word_list:
        print("Please enter some text.")
        return

    word_counts = {}
    for word in word_list:
        word_counts[word] = word_counts.get(word, 0) + 1

    print("\nWord frequency:")
    print(word_counts)

    try:
        requested_count = int(input("\nHow many top words should be displayed? "))
    except ValueError:
        print("Please enter a whole number.")
        return

    ranked_words = sorted(
        word_counts.items(),
        key=lambda pair: (-pair[1], pair[0]),
    )
    print("\nTop words:")
    for word, count in ranked_words[:max(0, requested_count)]:
        print(word, ":", count)

    used_once = sorted(
        word for word, count in word_counts.items() if count == 1
    )
    print("\nWords used only once:", used_once)

    words_by_frequency = {}
    for word, count in word_counts.items():
        words_by_frequency.setdefault(count, []).append(word)
    for word_group in words_by_frequency.values():
        word_group.sort()
    print("\nFrequency-wise words:", words_by_frequency)

    words_by_length = {}
    for word in word_counts:
        words_by_length.setdefault(len(word), []).append(word)
    for word_group in words_by_length.values():
        word_group.sort()
    print("\nWords grouped by length:", words_by_length)

    query_word = input("\nEnter a word to search: ").lower()
    query_word = "".join(char for char in query_word if char.isalnum())
    if query_word in word_counts:
        print(query_word, "appears", word_counts[query_word], "time(s).")
    else:
        print("Word not found.")


if __name__ == "__main__":
    main()
