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
        self.notes = []  # Очищаем список перед загрузкой заметок из файла
        try:
            with open("notes.csv", newline="") as file:
                reader = csv.reader(file, delimiter=";")
                next(reader)  # Пропускаем заголовок
                for row in reader:
                    id, title, body, created_at = row
                    self.notes.append(Note(id, title, body, created_at))
        except FileNotFoundError:
            self.create_empty_file()

    # Метод для создания пустого файла заметок
    def create_empty_file(self):
        with open("notes.csv", "w", newline="") as file:
            writer = csv.writer(file, delimiter=";")
            # Записываем заголовки в файл
            writer.writerow(["ID", "Title", "Body", "Created At"])

    # Метод для создания новой заметки
    def create_note(self, title, body):
        # Создаем новую заметку
        id = self.generate_unique_id()
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        note = Note(id, title, body, created_at)
        # Добавляем заметку в список
        self.notes.append(note)
        # Сохраняем заметку в файл
        self.save_to_file()
        # Перезагружаем список заметок из файла, чтобы обновить данные
        self.load_from_file()

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
        # Сортируем заметки по дате создания
        sorted_notes = sorted(self.notes, key=lambda x: x.created_at, reverse=True)
        for note in sorted_notes:
            print(separator_line)
            print(note)
            print(separator_line)
            print()

    # Метод для обновления заметки
    def update_note(self, id, new_title=None, new_body=None):
        note_found = False
        for note in self.notes:
            if note.id == id:
                note_found = True
                # Если указаны новое название и/или текст заметки, обновляем их
                if new_title is not None:
                    note.title = new_title
                if new_body is not None:
                    note.body = new_body
                # Обновляем время создания
                note.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                # Сохраняем изменения в файл
                self.save_to_file()
                print("Заметка успешно обновлена.")
                break

        if not note_found:
            print("Ошибка: Заметка с указанным ID не найдена. Пожалуйста, введите другой ID.")

    # Метод для удаления заметки
    def delete_note(self, id):
        note_exists = False
        for note in self.notes:
            if note.id == id:
                self.notes.remove(note)
                note_exists = True
                break

        if not note_exists:
            print("Ошибка: Заметка с указанным ID не найдена. Пожалуйста, введите другой ID.")
            return

        self.save_to_file()
        print("Заметка успешно удалена.")

    # Метод для сохранения всех заметок в файл
    def save_to_file(self):
        with open("notes.csv", "w", newline="") as file:
            writer = csv.writer(file, delimiter=";")
            # Записываем заголовки в файл
            writer.writerow(["ID", "Title", "Body", "Created At"])
            # Записываем каждую заметку в файл
            for note in self.notes:
                writer.writerow([note.id, note.title, note.body, note.created_at])