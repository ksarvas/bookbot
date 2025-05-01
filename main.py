import sys
from stats import get_num_words
from stats import get_num_characters
from stats import get_list_of_characters

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path_to_file = sys.argv[1]

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents
 
def main():
    file_contents = get_book_text(path_to_file)
    character_count = get_num_characters(file_contents)
    character_count_list = get_list_of_characters(character_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(file_contents)} total words") 
    print("--------- Character Count -------")
    for char_dict in character_count_list:
        if char_dict["char"].isalpha():
            print (f"{char_dict['char']}: {char_dict['num']}")
    print("============= END ===============")

main()

