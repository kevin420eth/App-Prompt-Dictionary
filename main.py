import json

# Read the dictionary
with open('data.json','r') as f:
    data = json.load(f)

def add_a_new_word():
    new_word = input('Enter a vocabulary:\n').lower()
    meaning = input('Enter its meaning:\n').lower()
    synonyms = input('Enter its synonyms:\n').lower()
    word_type = input('Enter its type:\n').lower()

    with open('data.json', 'w', encoding='utf-8') as f:
        data[new_word]={
            "meaning":meaning,
            "synonyms":synonyms,
            "type":word_type
        }
        json.dump(data, f)

def add_property():
    pass

def delete_property():
    pass


