from manager.note_manager import NoteManager
from datetime import datetime
"""
Основной файл программы для управления заметками.

Этот файл содержит функцию `main`, которая является точкой входа в программу.
Внутри функции `main` создается экземпляр класса `NoteManager`, который представляет менеджер заметок.
Затем программа запускает бесконечный цикл, в котором пользователю предлагается выбрать действие:
создать заметку, прочитать заметки, обновить заметку, удалить заметку или выйти из программы.
В зависимости от выбранного действия вызываются соответствующие методы у экземпляра `NoteManager`.

Автор: [Батраков Роман]

"""

def main():
    # Создаем экземпляр класса NoteManager для управления заметками
    note_manager = NoteManager()

    while True:
        print()
        print("Выберите действие:")
        print("1. Создать заметку")
        print("2. Читать все заметки")
        print("3. Читать заметки по дате")
        print("4. Читать заметки по id")
        print("5. Обновить заметку")
        print("6. Удалить заметку")
        print("7. Выйти")

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
            # Запрос у пользователя начальной даты для выборки заметок
            while True:
                start_date = input("Введите начальную дату (гггг-мм-дд): ")
                try:
                    datetime.strptime(start_date, "%Y-%m-%d")
                    break
                except ValueError:
                    print("Ошибка: Неправильный формат даты. Пожалуйста, введите дату в формате ГГГГ-ММ-ДД.")

            # Запрос у пользователя конечной даты для выборки заметок
            while True:
                end_date = input("Введите конечную дату (гггг-мм-дд): ")
                try:
                    datetime.strptime(end_date, "%Y-%m-%d")
                    break
                except ValueError:
                    print("Ошибка: Неправильный формат даты. Пожалуйста, введите дату в формате ГГГГ-ММ-ДД.")

            # Вывод заметок в указанном диапазоне дат
            note_manager.read_notes_by_date(start_date, end_date)
        elif choice == "4":
            # Запрос у пользователя ID заметки для чтения
            id = input("Введите ID заметки для чтения: ")
            # Вывод заметки по ID
            note_manager.read_note_by_id(id)
        elif choice == "5":
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
        elif choice == "6":
            # Запрос у пользователя ID заметки для удаления
            id = input("Введите ID заметки для удаления: ")
            # Удаление заметки
            note_manager.delete_note(id)
        elif choice == "7":
            # Завершение работы программы
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите правильный номер действия.")

if __name__ == "__main__":
    main()
