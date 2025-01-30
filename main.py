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

    def generate_report():
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
                    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                    'y', 'z']
        print("--- Begin report of books/frankenstein.txt ---\n"
              f"{count_words()} words found in the document \n")
        for k in count_characters():
            if k in alphabet:
                value = count_characters()[k]
                print(f"The '{k}' character was found {value} times")
        print("--- End report ---")

    generate_report()
main()