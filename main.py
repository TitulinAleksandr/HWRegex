from phbook import Phbook


if __name__ == '__main__':
    phonebook = Phbook()
    x = phonebook.read_file('phonebook_raw.csv')
    x = phonebook.format_number(x)
    x = phonebook.format_name(x)
    x = phonebook.join_duplicate(x)
    phonebook.write_file(x)
