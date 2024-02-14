from datetime import datetime

class Note:
    def __init__(self, id, title, body, created_at):
        """
        Конструктор класса Note.

        Args:
            id (int): Идентификатор заметки.
            title (str): Заголовок заметки.
            body (str): Текст заметки.
            created_at (datetime): Дата и время создания заметки.
        """
        self.id = id
        self.title = title
        self.body = body
        self.created_at = created_at

    def __str__(self):
        """
        Метод для представления объекта заметки в виде строки.

        Returns:
            str: Строковое представление заметки.
        """
        return f"ID: {self.id}\nЗаголовок: {self.title}\nТекст заметки: {self.body}\nДата создания: {self.created_at}"
