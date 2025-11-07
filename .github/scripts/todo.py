# todo.py
class Task:
    def __init__(self, title, status="ToDo"):
        self.title = title
        self.status = status

    def mark_completed(self):
        self.status = "Done"

class TaskPool:
    def __init__(self):
        self.tasks = []

    def populate(self):
        self.tasks = [
            Task("Buy milk", "Done"),
            Task("Read lecture", "Done"),
            Task("Write report", "Done"),
            Task("Call Alice", "ToDo"),
            Task("Plan project", "ToDo"),
            Task("Push code", "ToDo"),
        ]

    def get_open_tasks(self):
        return [t for t in self.tasks if t.status == "ToDo"]

    def get_done_tasks(self):
        return [t for t in self.tasks if t.status == "Done"]

if __name__ == "__main__":
    pool = TaskPool()
    pool.populate()
    print("ToDo Tasks:")
    for t in pool.get_open_tasks():
        print(t.title)
    print("\nDone Tasks:")
    for t in pool.get_done_tasks():
        print(t.title)

