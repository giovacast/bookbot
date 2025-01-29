def main():
    with open("books/frankenstein.txt") as file:
        file_contents = file.read()
    def count_words():
        word_count = 0
        words = file_contents.split()
        for word in words:
            word_count += 1
        return word_count
    
    def count_characters():
        character_count = {}
        for i in file_contents.lower():
            if i not in character_count:
                character_count[i] = 0
            if i in character_count:
                character_count[i] += 1
        return character_count

    print(count_characters())
    print(count_words())
main()