from datetime import datetime

class Note:
    def __init__(self, id, title, body, created_at):
        self.id = id
        self.title = title
        self.body = body
        self.created_at = created_at

    def __str__(self):
        return f"ID: {self.id}\nTitle: {self.title}\nBody: {self.body}\nCreated At: {self.created_at}"
