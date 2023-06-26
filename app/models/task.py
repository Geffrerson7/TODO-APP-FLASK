class Task:
    def __init__(
        self,
        user,
        startingPoint,
        endPoint,
        amount,
        reason,
        date,
        created_at,
        done_at=None,
        deleted_at=None,
    ):
        self.user = user
        self.startingPoint = startingPoint
        self.endPoint = endPoint
        self.amount = amount
        self.reason = reason
        self.date = date
        self.created_at = created_at
        self.done_at = done_at
        self.deleted_at = deleted_at

    def to_json(self):
        return {
            "user": self.user,
            "startingPoint": self.startingPoint,
            "endPoint": self.endPoint,
            "amount": self.amount,
            "reason": self.reason,
            "date": self.date,
            "createdAt": self.created_at,
            "doneAt": self.done_at,
            "deletedAt": self.deleted_at,
        }
