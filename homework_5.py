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
    if not doc_found:
        print(f'Документ с указанным номером не найден.')
    
def print_list():
    for document in documents:
        print(f'{document.get("type")} "{document.get("number")}" "{document.get("name")}"')

def put_document(dict_doc: dict, shelf_id: str):
    if shelf_id in directories:
        documents.append(dict_doc)
        print(f'Документ не добавлен на полку: {shelf_id}')
    else:
        print(f'Документ не добавлен в каталог. Указанной полки не существует.')

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
            print_people(input('Введите номер документа: '))
        elif user_input == 's':
            print_shelf(input('Введите номер документа: '))
        elif user_input == 'l':
             print_list()
        elif user_input == 'a':          
            new_doc = {"type": str(input('Введите номер документа: ')), "number": str(input('Введите тип документа: ')), "name": str(input('Введите имя владельца документа: '))}
            put_document(new_doc, str(input('Введите номер полки: ')))
        # elif user_input == 'd':

        # elif user_input == 'm':

        # elif user_input == 'as':
        
        elif user_input == 'h':
            print_help()
        elif user_input == 'q':
            break

main()