def get_num_words(file_contents):
    # with open(path_to_file) as f:
    #    file_contents = f.read()
    return len(file_contents.split())

def get_num_characters(file_contents):
    num_characters = {}
    for character in file_contents:
        character = character.lower()
        if character in num_characters:
            num_characters[character] += 1
        else:
            num_characters[character] = 1
    return num_characters

def sort_on(num_characters):
    return num_characters["num"]

def get_list_of_characters(num_characters):
    num_characters_sorted = []
    for character in num_characters:
        num_characters_sorted.append({"char": character, "num": num_characters[character]})
    num_characters_sorted.sort(reverse=True, key=sort_on)
    return num_characters_sorted
    

    
    