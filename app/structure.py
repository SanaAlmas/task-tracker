import json
import os
from app.model import Task
from app.status import Status

class Structure:
    def __init__(self):
        self.filename = "taskTracker.json"
        self.tasks = self.load()

    def load(self):
        if not os.path.exists(self.filename) or os.path.getsize(self.filename) == 0:
            return {}

        with open(self.filename, "r") as f:
            return json.load(f)

    def save(self,task):
        with open(self.filename, "w") as f:
            json.dump(task, f, indent=4)

    def generate_task_id(self):
        if not self.tasks:
            return 1
        return max(map(int, self.tasks.keys())) + 1

    def add(self, data):
        taskId = self.generate_task_id()
        task = Task(taskId, data)
        self.tasks[task.get_task_id()] = task.to_dict()
        self.save(self.tasks)

    def update(self, data, new_status):
        try:
            status_enum = new_status.replace(" ", "").upper()
            status_enum = Status[status_enum]
        except ValueError:
            return "Invalid status"

        if data in self.tasks:
            self.tasks[data] = status_enum.value
            self.save(self.tasks)
        else:
            return('Task not found')

    def delete(self, data):
        if data in self.tasks:
            self.tasks.pop(data)
            self.save(self.tasks)
        else:
            return('Task not found')

    def show(self, status):
        if not self.tasks:
            print("No tasks available.")
            return
        if status == 'all':
            for t,s in self.tasks.items():
                print(f"{t} -> {s}")
            return
        status_enum = status.replace(" ", "").upper()
        status= Status[status_enum].value
        filtered = {}
        for task,s in self.tasks.items():
            if s == status:
               filtered[task]=status
            if not filtered:
               print(f"No tasks with status '{status}'")
            else:
                for task, s in filtered.items():
                    print(f"{task} -> {s}")



