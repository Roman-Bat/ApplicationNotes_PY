import csv
from datetime import datetime
from model.note import Note

class NoteManager:
    def __init__(self):
        self.notes = []
        self.load_from_file()

    def load_from_file(self):
        try:
            with open("notes.csv", newline="") as file:
                reader = csv.reader(file, delimiter=";")
                next(reader)  # skip header
                for row in reader:
                    id, title, body, created_at = row
                    self.notes.append(Note(id, title, body, created_at))
        except FileNotFoundError:
            self.create_empty_file()

    def create_empty_file(self):
        with open("notes.csv", "w", newline="") as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerow(["ID", "Title", "Body", "Created At"])

    def create_note(self, title, body):
        id = self.generate_unique_id()
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        note = Note(id, title, body, created_at)
        self.notes.append(note)
        self.save_to_file()

    def generate_unique_id(self):
        if not self.notes:
            return 1
        else:
            return int(self.notes[-1].id) + 1

    def read_notes(self):
        separator_line = "-" * 30
        for note in self.notes:
            print(separator_line)
            print(note)
            print(separator_line)
            print()

    def update_note(self, id, new_title, new_body):
        for note in self.notes:
            if note.id == id:
                note.title = new_title
                note.body = new_body
                note.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.save_to_file()
                break

    def delete_note(self, id):
        self.notes = [note for note in self.notes if note.id != id]
        self.save_to_file()

    def save_to_file(self):
        with open("notes.csv", "w", newline="") as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerow(["ID", "Title", "Body", "Created At"])
            for note in self.notes:
                writer.writerow([note.id, note.title, note.body, note.created_at])
