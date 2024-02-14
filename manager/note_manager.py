import csv
from datetime import datetime
from model.note import Note

class NoteManager:
    """
        Класс NoteManager представляет собой менеджер заметок.
        Он отвечает за управление операциями с заметками, такими как создание, чтение,
        обновление и удаление, а также за загрузку и сохранение заметок в файл.
        -------------------------------------------------------------------------------
        Атрибуты:
        notes (list): Список объектов заметок.
        --------------------------------------------------------------------------------
        Методы:
        load_from_file(): Загружает заметки из файла.
        create_empty_file(): Создает пустой файл заметок, если файл не существует.
        create_note(title, body): Создает новую заметку с указанным заголовком и текстом.
        generate_unique_id(): Генерирует уникальный идентификатор для новой заметки.
        read_notes(): Выводит все заметки в консоль.
        update_note(id, new_title, new_body): Обновляет существующую заметку с
                                                    указанным идентификатором.
        delete_note(id): Удаляет заметку с указанным идентификатором.
        save_to_file(): Сохраняет все заметки в файл.
        """
    def __init__(self):
        # Список заметок
        self.notes = []
        # Загружаем заметки из файла при инициализации объекта
        self.load_from_file()

    # Метод для загрузки заметок из файла
    def load_from_file(self):
        try:
            # Пытаемся открыть файл notes.csv для чтения
            with open("notes.csv", newline="") as file:
                # Создаем объект reader для чтения файла в формате CSV
                reader = csv.reader(file, delimiter=";")
                # Пропускаем первую строку (заголовки)
                next(reader)
                # Для каждой строки в файле CSV создаем объект Note и добавляем его в список заметок
                for row in reader:
                    id, title, body, created_at = row
                    self.notes.append(Note(id, title, body, created_at))
        except FileNotFoundError:
            # Если файл не найден, создаем пустой файл
            self.create_empty_file()

    # Метод для создания пустого файла заметок
    def create_empty_file(self):
        with open("notes.csv", "w", newline="") as file:
            writer = csv.writer(file, delimiter=";")
            # Записываем заголовки в файл
            writer.writerow(["ID", "Title", "Body", "Created At"])

    # Метод для создания новой заметки
    def create_note(self, title, body):
        # Генерируем уникальный ID для новой заметки
        id = self.generate_unique_id()
        # Получаем текущую дату и время создания заметки
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Создаем объект заметки и добавляем его в список заметок
        note = Note(id, title, body, created_at)
        self.notes.append(note)
        # Сохраняем заметку в файл
        self.save_to_file()

    # Метод для генерации уникального ID для новой заметки
    def generate_unique_id(self):
        if not self.notes:
            return 1
        else:
            # Получаем ID последней заметки, увеличиваем на 1 и возвращаем
            return int(self.notes[-1].id) + 1

    # Метод для чтения всех заметок
    def read_notes(self):
        separator_line = "-" * 30
        for note in self.notes:
            # Выводим разделительную линию перед каждой заметкой
            print(separator_line)
            # Выводим заметку
            print(note)
            # Выводим разделительную линию после каждой заметки
            print(separator_line)
            # Переводим на новую строку для улучшения читаемости
            print()

    # Метод для обновления заметки
    def update_note(self, id, new_title=None, new_body=None):
        note_found = False
        for note in self.notes:
            if note.id == id:
                note_found = True
                break

        if not note_found:
            print("Ошибка: Заметка с указанным ID не найдена. Пожалуйста, введите другой ID.")
            return

        # Если заметка найдена, запрашиваем новые данные
        if new_title is None:
            new_title = input("Введите новое название заметки: ")
        if new_body is None:
            new_body = input("Введите новый текст заметки: ")

        for note in self.notes:
            if note.id == id:
                # Обновляем заметку
                note.title = new_title
                note.body = new_body
                note.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                # Сохраняем изменения в файл
                self.save_to_file()
                print("Заметка успешно обновлена.")
                break

    # Метод для удаления заметки
    def delete_note(self, id):
        # Удаляем заметку из списка по ID
        self.notes = [note for note in self.notes if note.id != id]
        # Сохраняем изменения в файл
        self.save_to_file()

    # Метод для сохранения всех заметок в файл
    def save_to_file(self):
        with open("notes.csv", "w", newline="") as file:
            writer = csv.writer(file, delimiter=";")
            # Записываем заголовки в файл
            writer.writerow(["ID", "Title", "Body", "Created At"])
            # Записываем каждую заметку в файл
            for note in self.notes:
                writer.writerow([note.id, note.title, note.body, note.created_at])