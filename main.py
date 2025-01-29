def main():
    def count_words(text):
        word_count = 0
        with open(text) as file:
            file_contents = file.read()
            words = file_contents.split()
            for word in words:
                word_count += 1
        return word_count

    print(count_words("books/frankenstein.txt"))
main()