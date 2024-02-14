from manager.note_manager import NoteManager

def main():
    # Создаем экземпляр класса NoteManager для управления заметками
    note_manager = NoteManager()

    while True:
        print()
        print("Выберите действие:")
        print("1. Создать заметку")
        print("2. Читать заметки")
        print("3. Обновить заметку")
        print("4. Удалить заметку")
        print("5. Выйти")

        choice = input("Введите номер действия: ")

        if choice == "1":
            # Запрос у пользователя заголовка и текста заметки для создания
            title = input("Введите заголовок заметки: ")
            body = input("Введите тело заметки: ")
            # Создание заметки
            note_manager.create_note(title, body)
        elif choice == "2":
            # Чтение всех заметок
            note_manager.read_notes()
        elif choice == "3":
            # Запрос у пользователя ID заметки для обновления
            id = input("Введите ID заметки для обновления: ")
            # Проверка наличия заметки с указанным ID
            note_to_update = next((note for note in note_manager.notes if note.id == id), None)
            if note_to_update:
                # Запрос нового заголовка и текста заметки для обновления
                new_title = input("Введите новый заголовок заметки: ")
                new_body = input("Введите новое тело заметки: ")
                # Обновление заметки
                note_manager.update_note(id, new_title, new_body)
            else:
                print("Ошибка: Заметка с указанным ID не найдена. Пожалуйста, введите другой ID.")
        elif choice == "4":
            # Запрос у пользователя ID заметки для удаления
            id = input("Введите ID заметки для удаления: ")
            # Удаление заметки
            note_manager.delete_note(id)
        elif choice == "5":
            # Завершение работы программы
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите правильный номер действия.")

if __name__ == "__main__":
    main()
