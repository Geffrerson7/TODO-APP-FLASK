class Task:
    def __init__(self, text, created_at, done_at=None, deleted_at=None):
        self.text = text
        self.created_at = created_at
        self.done_at = done_at
        self.deleted_at = deleted_at

    def to_dict(self):
        return {
            'text': self.text,
            'createdAt': self.created_at,
            'doneAt': self.done_at,
            'deletedAt': self.deleted_at
        }
