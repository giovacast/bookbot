def main():
    with open("books/frankenstein.txt") as file:
        file_contents = file.read()
    def count_words():
        word_count = 0
        words = file_contents.split()
        for word in words:
            word_count += 1
        return word_count

    print(count_words())
main()