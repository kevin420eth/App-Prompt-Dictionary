import json

# Read the dictionary
with open('data.json','r') as f:
    data = json.load(f)

# Add a new word
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

# Add a new property to all words
def add_property():
    property = input('Enter a new property:\n').lower()
    if property == '':
        print("Can't be empty")
        return
    for _ in data:
        data[_][property]=""
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f)

# Delete a property from all words
def delete_property():
    _property = input('Enter the property you want to delete:\n').lower()
    if _property == '':
            return
    for _ in data:
        try:
            del data[_][_property]
        except KeyError:
            print("There's no this property")
            return
        except Exception as error:
            print(error)
            return
            
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f)

    print(f"Property: {_property} has been deleted")

# Modify the value of the property of a specific word
def modify_property_value():
    target_word = input('Enter the word you want to modify:\n').lower()
    target_property = input('Enter the property you want to modify\n').lower()
    property_value = input('Enter the value you want to modify:\n').lower()
    
    if target_word in data and target_property in data[target_word]:
        data[target_word][target_property] = property_value
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f)
        print(f'The {target_property} of {target_word} has been changed')
    else:
        print('Wrong input')
        return

# Check a word
def check_word():
    target_word = input('Enter a word:\n')
    try:
        for _ in data[target_word]:
            print(f'\n{_}: {data[target_word][_]}')
    except KeyError:
        print("This word doesn't exist")
    except Exception as error:
        print(error)

def random_word():
    while True:
        pass
