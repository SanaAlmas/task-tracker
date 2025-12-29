from status import Status

class Task:
    def __init__(self, data):
        self.task = data
        self.status = Status.TODO

    def to_dict(self):
        return {
            "task": self.task,
            "status": self.status.name
        }

    def get_task_data(self):
        return self.task

    def get_status_data(self):
        return self.status.value

    def set_status_data(self):
        self.status = Status.DONE
