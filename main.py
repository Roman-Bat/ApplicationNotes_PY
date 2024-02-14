from manager.note_manager import NoteManager

def main():
    note_manager = NoteManager()

    while True:
        print("Выберите действие:")
        print("1. Создать заметку")
        print("2. Читать заметки")
        print("3. Обновить заметку")
        print("4. Удалить заметку")
        print("5. Выйти")

        choice = input("Введите номер действия: ")

        if choice == "1":
            title = input("Введите заголовок заметки: ")
            body = input("Введите тело заметки: ")
            note_manager.create_note(title, body)
        elif choice == "2":
            note_manager.read_notes()
        elif choice == "3":
            id = input("Введите ID заметки для обновления: ")
            new_title = input("Введите новый заголовок заметки: ")
            new_body = input("Введите новое тело заметки: ")
            note_manager.update_note(id, new_title, new_body)
        elif choice == "4":
            id = input("Введите ID заметки для удаления: ")
            note_manager.delete_note(id)
        elif choice == "5":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите правильный номер действия.")


if __name__ == "__main__":
    main()