from datetime import datetime
from app.status import Status


class Task:
    def __init__(self, taskid, data):
        self.taskId = taskid
        self.task = data
        self.status = Status.TODO.value
        self.createdAt = self.get_current_time()
        self.updatedAt = self.get_current_time()

    def to_dict(self):
        return {
            "task": self.task,
            "status": self.status,
            "created on": self.createdAt,
            "updated on": self.updatedAt,
        }

    def get_task_data(self):
        return self.task

    def get_status_data(self):
        return self.status.value

    def set_status_data(self):
        self.status = Status.DONE

    def get_current_time(self):
        return datetime.now().isoformat()

    def get_task_id(self):
        return self.taskId
