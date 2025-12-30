TaskTracker CLI

TaskTracker is a simple command-line task management application written in Python.
It allows you to add, update, delete, and view tasks with different statuses using intuitive CLI arguments.

Features

Add new tasks
Update task status (TODO, INPROGRESS, DONE)
Delete existing tasks
View all tasks or filter by status
Clean CLI interface using argparse
Uses Enum for reliable status management

Status Values
Tasks can have one of the following statuses:
todo
in progress
done
Internally, statuses are managed using a Python Enum to ensure consistency.

Usage

Run the application from the command line:

python main.py [OPTIONS]

Commands
Add a Task
python main.py -a "Buy groceries"

Update a Task Status
python main.py -u "Buy groceries" inprogress
Valid statuses: todo, inprogress, done

Delete a Task
python main.py -d 'Buy groceries'

Show Tasks
Show all tasks:
python main.py -s

Show only tasks with a specific status:
python main.py -s todo
python main.py -s inprogress
python main.py -s done
