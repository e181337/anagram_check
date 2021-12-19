def count_occur(sub_list):
    character_set = {}
    for i in sub_list:
        if i in character_set:
            character_set[i] += 1
        else:
            character_set[i] = 1
    return character_set

def removed_number(dict_1, dict_2):
    number_remove = 0
    for i in dict_1:
        if (i not in dict_2) or (dict_1[i] > dict_2[i]):
            number_remove += 1
    return number_remove
    
def check_anagram(s_1, s_2): 
    if(sorted(s_1)== sorted(s_2)):
        print("they are anagrams")
    else:
        character_set_1 = count_occur(s_1)
        character_set_2 = count_occur(s_2)
        remove_1 = removed_number(character_set_1, character_set_2)
        remove_2 = removed_number(character_set_2, character_set_1)
        return_string = [f"remove {remove_1} characters from '{s_1}' and {remove_2} characters from '{s_2}'"]  
        print(return_string[0])

def main():
    string_first = input('a:')
    string_second = input('b:')
    check_anagram(string_first, string_second)

if __name__ == '__main__':
    main()