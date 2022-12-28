import re
import csv
from pprint import pprint


def read_file(file_name):
    with open(file_name, encoding="utf-8") as file:
        rows = csv.reader(file, delimiter=",")
        contacts_list = list(rows)
    return contacts_list

def format_number(data):
    number_search = r'(\+7|8)\s*\(*(\d{3})\)*[\s|-]*(\d{3})[-]*(\d{2})[-]*(\d{2})((\s*)\(*(доб.)\s*(\d{4})\)*)?'
    number_new_format = r'+7(\2)\3-\4-\5\7\8\9'
    new_contacts_list = []
    for text in data:
        text_search = ','.join(text)
        format_text = re.sub(number_search, number_new_format, text_search)
        format_list = format_text.split(',')
        new_contacts_list.append(format_list)
    return new_contacts_list

def format_name(data):
    name_search = r'(^[А-ё]+)(\s*)(\,?)([А-ё]+)(\s*)(\,?)([А-ё]+)?(\,?)(\,?)(\,?)'
    name_new_format = r'\1,\4\6\9\7\8'
    new_contacts_list = []
    for text in data:
        text_search = ','.join(text)
        format_text = re.sub(name_search, name_new_format, text_search)
        format_list = format_text.split(',')
        new_contacts_list.append(format_list)
    return new_contacts_list

def join_duplicate(data):
    dict_ = {}   
    new_contacts_list = []
    for x in data:
        if x[0] not in dict_.keys():
            dict_[x[0]] = x[1:]
        else:
            for j, element in enumerate(dict_[x[0]]):
                if element == "" and x[1:][j] != "":
                    dict_[x[0]][j] = x[1:][j]
    
    for x in dict_.items():
        x[1].insert(0, x[0])
        new_contacts_list.append(x[1])
    return new_contacts_list

def write_file(data):
    with open("phone_book.csv", "w", encoding='utf-8') as file:
        data_writer = csv.writer(file, delimiter=',')
        data_writer.writerows(data)


if __name__ == '__main__':
    phonebook = read_file('phonebook_raw.csv')
    x = format_number(phonebook)
    contacts = format_name(x)
    # contacts = delete_space(contacts)
    # print(contacts)
    contacts = join_duplicate(contacts)
    # print(contacts)
    
    # contacts[0][2] = 'patronymic'
    write_file(contacts)