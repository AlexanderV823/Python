documents = [
             {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
             {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
             {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
            ]

directories =   {
                '1': ['2207 876234', '11-2'],
                '2': ['10006'],
                '3': []
                }

def print_people(doc_number: str):
    doc_found = False
    for document in documents:
        if document.get("number") == doc_number:
            print(f'Документ с номером "{document.get("number")}" принадлежит: "{document.get("name")}"')
            doc_found = True
    if not doc_found:
        print(f'Документ с указанным номером не найден.')

def print_shelf(doc_number: str):
    doc_found = False
    shelf_found = False
    for document in documents:
        if document.get("number") == doc_number:
            doc_found = True
            for shelf_id, shelf_list in directories.items():
                if doc_number in shelf_list:
                    shelf_found = True
                    print(f'Документ находится на полке: {shelf_id}')
            if not shelf_found:
                print(f'Место хранения документа отсутствует.')
                break
    if not doc_found:
        print(f'Документ с указанным номером не найден.')
    
def print_list():
    for document in documents:
        print(f'{document.get("type")} "{document.get("number")}" "{document.get("name")}"')

def put_document():
    new_doc = {"type": str(input('Введите тип документа: ')), "number": str(input('Введите номер документа: ')), "name": str(input('Введите имя владельца документа: '))}
    shelf_id = str(input('Введите номер полки: '))
    if shelf_id in directories:
        documents.append(new_doc)
        shelf_list = directories.get(shelf_id)
        shelf_list.append(new_doc.get("number"))
        print(f'Документ добавлен на полку: {shelf_id}')
    else:
        print(f'Документ не добавлен в каталог. Указанной полки не существует.')

def del_document(doc_number: str):   
    doc_found = False
    shelf_found = False
    for document in documents:
        if document.get("number") == doc_number:
            doc_found = True            
            for shelf_id, shelf_list in directories.items():
                if doc_number in shelf_list:
                    shelf_found = True
                    shelf_list.remove(doc_number)
                    del(documents[documents.index(document)])
                    print(f'Документ с номером "{document.get("number")}" удален из каталога и с полки: "{shelf_id}"')
                    continue   
            if not shelf_found:
                print(f'Место хранения документа отсутствует.')
                break            
    if not doc_found:
        print(f'Документ с указанным номером не найден.') 

def move_document(doc_number: str, shelf_id: str):
    doc_found = False
    for document in documents:
        if document.get("number") == doc_number:
            doc_found = True
            for old_shelf_id, shelf_list in directories.items():
                if doc_number in shelf_list:
                    shelf_found = True
                    shelf_list.remove(doc_number)
                    new_shelf_list = directories.get(shelf_id)
                    new_shelf_list.append(doc_number)
                    print(f'Документ с номером {doc_number} перемещен с полки: {old_shelf_id} на полку: {shelf_id}')
                    break
            if not shelf_found:
                print(f'Место хранения документа отсутствует.')
                break
    if not doc_found:
        print(f'Документ с указанным номером не найден.')

def add_shelf(shelf_id: str):
    if shelf_id not in directories:
        directories.setdefault(shelf_id, [])
    else:
        print(f'Указанная полка уже существует.')

def print_help():
    print(f'p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит.')
    print(f's – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится.')
    print(f'l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин".')
    print(f'a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.')
    print(f'd – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок.')
    print(f'm – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую.')
    print(f'as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень.')
    print(f'h – help – вывод подсказки')
    print(f'q - quit – выход из программы')

def main():
    while True:
        user_input = input('Введите команду: ')
        if user_input == 'p':
            print_people(str(input('Введите номер документа: ')))
        elif user_input == 's':
            print_shelf(str(input('Введите номер документа: ')))
        elif user_input == 'l':
             print_list()
        elif user_input == 'a':          
            put_document()
        elif user_input == 'd':
            del_document(str(input('Введите номер документа: ')))
        elif user_input == 'm':
            move_document(str(input('Введите номер документа: ')), str(input('Введите номер полки: ')))
        elif user_input == 'as':
            add_shelf(str(input('Введите номер новой полки: ')))
        elif user_input == 'h':
            print_help()
        elif user_input == 'q':
            break
        else:
            print(f'Указана не существующая команда. Для вызова справки введите "h"')

main()

# Эталон:
# def get_name_by_number():
#     number = input('Введите номер документа: ')
#     for doc in documents:
#         if doc['number'] == number:
#             print('{0}'.format(doc['name']))
#             break
#     else:
#         print('Отсутствуют документы с таким номером')


# def show_documents():
#     for doc in documents:
#         print(doc['type'], doc['number'], doc['name'])
#     for key, values in directories.items():
#         print(key, '->', values)


# def get_directory_by_number():
#     number = input('Введите номер документа: ')
#     for directory, list_docs in directories.items():
#         if number in list_docs:
#             print('Документ с номером {0} находится на полке {1}'.format(number, directory))
#             break
#     else:
#         print('Отсутствуют документы с таким номером')


# def add_document():
#     number = input('Введите номер документа:')
#     name = input('Введите имя и фамилию:')
#     doc_type = input('Введите тип документа:')
#     directory_number = input('Введите номер полки:')
#     if number and name and doc_type and directory_number:
#         documents.append({"type": doc_type, "number": number, "name": name})
#         if directory_number in directories:
#             directories[directory_number].append(number)
#         else:
#             directories[directory_number] = [number]
#     else:
#         print('ВНИМАНИЕ! Введены не все данные')


# def remove_document():
#     person_number = input('Введите номер документа: ')
#     bookshelf = ''
#     for elem in documents:
#         if elem['number'] == person_number:
#             documents.remove(elem)
#     for number_shelf, number_documents in directories.items():
#         if person_number in number_documents:
#             number_documents.remove(person_number)
#             bookshelf = number_shelf
#             break
#     print(f'Удален документ с номером: {person_number} из базы данных и убран с полки №{bookshelf}')


# def main():
#     while True:
#         command = input('Введите команду: ')
#         if command == 'p':
#             get_name_by_number()
#         elif command == 'l':
#             show_documents()
#         elif command == 's':
#             get_directory_by_number()
#         elif command == 'a':
#             add_document()
#         elif command == 'd':
#             remove_document()
#             print(documents)
#             print(directories)
#         elif command == 'e':
#             break

# main()