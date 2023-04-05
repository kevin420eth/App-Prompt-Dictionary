import json, random

# Add a new word
def add_a_new_word():
    new_word = input('Enter a vocabulary:\n').lower()
    meaning = input('Enter its meaning:\n').lower()
    synonyms = input('Enter its synonyms:\n').lower()
    word_type = input('Enter its type:\n').lower()

    with open('./data/data.json', 'w', encoding='utf-8') as f:
        synonyms_list = []
        if synonyms != '':
            synonyms_list.append(synonyms)
        
        data[new_word]={
            "meaning":meaning,
            "synonyms":synonyms_list,
            "type":word_type
        }
        json.dump(data, f)

# Add a new property to all words
def add_property():
    target_property = input('Enter a new property:\n').lower()
    if target_property == '':
        print("Can't be empty")
        return
    else:
        for _ in data:
            if target_property in data[_]:
                print("This property has existed")
                return
            data[_][target_property]=""
    with open('./data/data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f)

# Delete a property from all words
def delete_property():
    target_property = input('Enter the property you want to delete:\n').lower()
    if target_property == '':
            return
    for _ in data:
        try:
            del data[_][target_property]
        except KeyError:
            print("There's no this property")
            return
        except Exception as error:
            print(error)
            return
            
    with open('./data/data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f)

    print(f"Property: {target_property} has been deleted")

# Modify the value of the property of a specific word
def modify_property_value():
    target_word = input('Enter the word you want to modify:\n').lower()
    target_property = input('Enter the property you want to modify\n').lower()
    property_value = input('Enter the value you want to modify:\n').lower()
    
    if target_word not in data or target_property not in data[target_word]:
        print('Wrong input')
        return
    else:
        data[target_word][target_property] = property_value
        with open('./data/data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f)
        print(f'The {target_property} of {target_word} has been changed')

# Add a new synoyms
def add_a_new_synonyms():
    target_word = input('Enter the word you want to modify:\n').lower()
    new_synonyms = input('Enter the value you want to add:\n').lower()
    new_synonyms = new_synonyms.replace(' ','').split(',')
    if target_word not in data:
        print(f"The word '{target_word}' doesn't exist in your database")
        return
    else:
        for _ in new_synonyms:
            data[target_word]['synonyms'].append(_)
        with open('./data/data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f)
    print(f'New synonymses have been added')

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

# Review words randomly
def random_word():
    while True:
        key = random.choice(list(data))
        print(key)
        user_input = input('\nClick Enter to show detail').lower()
        for _ in data[key]:
            print(f'\n{_}: {data[key][_]}')
        user_input = input('\nClick Enter to check next word\n').lower()
        if user_input != '':
            break

if __name__ == "__main__":
    # Read the dictionary
    with open('./data/data.json','r') as f:
        data = json.load(f)
    
    add_a_new_word()