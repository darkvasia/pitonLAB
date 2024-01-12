import tkinter as tk
from tkinter import simpledialog, Listbox, messagebox
import pickle

class Task:
    def __init__(self, title, description, priority, deadline):
        self.title = title
        self.description = description
        self.priority = priority
        self.deadline = deadline

    def __str__(self):
        return f"{self.title} (Priority: {self.priority}, Deadline: {self.deadline})"

class Project:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

class DataManager:
    @staticmethod
    def save_data(filename, data):
        with open(filename, 'wb') as file:
            pickle.dump(data, file)

    @staticmethod
    def load_data(filename):
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except FileNotFoundError:
            return []

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")

        self.projects = DataManager.load_data('tasks.dat') or []
        self.initialize_ui()

    def initialize_ui(self):
        self.project_listbox = Listbox(self.root, height=6)
        self.project_listbox.pack()
        self.task_listbox = Listbox(self.root, height=6)
        self.task_listbox.pack()

        add_project_btn = tk.Button(self.root, text="Add Project", command=self.add_project)
        add_project_btn.pack()

        add_task_btn = tk.Button(self.root, text="Add Task", command=self.add_task)
        add_task_btn.pack()

        edit_task_btn = tk.Button(self.root, text="Edit Task", command=self.edit_task)
        edit_task_btn.pack()

        delete_task_btn = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        delete_task_btn.pack()

        move_task_btn = tk.Button(self.root, text="Move Task", command=self.move_task)
        move_task_btn.pack()

        self.update_project_list()

    def add_project(self):
        project_name = simpledialog.askstring("Project Name", "Enter project name:")
        if project_name:
            project = Project(project_name)
            self.projects.append(project)
            self.update_project_list()
            DataManager.save_data('tasks.dat', self.projects)

    def add_task(self):
        project_index = self.project_listbox.curselection()
        if not project_index:
            messagebox.showwarning("Warning", "Select a project first.")
            return

        project = self.projects[project_index[0]]
        task_title = simpledialog.askstring("Task Title", "Enter task title:")
        task_description = simpledialog.askstring("Task Description", "Enter task description:")
        task_priority = simpledialog.askstring("Task Priority", "Enter task priority:")
        task_deadline = simpledialog.askstring("Task Deadline", "Enter task deadline:")

        if task_title and task_priority and task_deadline:
            task = Task(task_title, task_description, task_priority, task_deadline)
            project.add_task(task)
            self.update_task_list(project)
            DataManager.save_data('tasks.dat', self.projects)

    def edit_task(self):
        project_index = self.project_listbox.curselection()
        task_index = self.task_listbox.curselection()

        if not project_index or not task_index:
            messagebox.showwarning("Warning", "Select a project and task first.")
            return

        project = self.projects[project_index[0]]
        task = project.tasks[task_index[0]]

        new_title = simpledialog.askstring("Edit Task", "Enter new title:", initialvalue=task.title)
        new_description = simpledialog.askstring("Edit Task", "Enter new description:", initialvalue=task.description)
        new_priority = simpledialog.askstring("Edit Task", "Enter new priority:", initialvalue=task.priority)
        new_deadline = simpledialog.askstring("Edit Task", "Enter new deadline:", initialvalue=task.deadline)

        if new_title and new_priority and new_deadline:
            task.title = new_title
            task.description = new_description
            task.priority = new_priority
            task.deadline = new_deadline
            self.update_task_list(project)
            DataManager.save_data('tasks.dat', self.projects)

    def delete_task(self):
        project_index = self.project_listbox.curselection()
        task_index = self.task_listbox.curselection()

        if not project_index or not task_index:
            messagebox.showwarning("Warning", "Select a project and task first.")
            return

        project = self.projects[project_index[0]]
        task = project.tasks.pop(task_index[0])

        self.update_task_list(project)
        DataManager.save_data('tasks.dat', self.projects)

    def move_task(self):
        project_index = self.project_listbox.curselection()
        task_index = self.task_listbox.curselection()

        if not project_index or not task_index:
            messagebox.showwarning("Warning", "Select a project and task first.")
            return

        target_project_index = simpledialog.askinteger("Target Project",
                                                       "Enter the target project number:",
                                                       minvalue=0, maxvalue=len(self.projects)-1)

        if target_project_index is None or target_project_index == project_index[0]:
            return

        task = self.projects[project_index[0]].tasks.pop(task_index[0])
        self.projects[target_project_index].add_task(task)

        self.update_task_list(self.projects[project_index[0]])
        DataManager.save_data('tasks.dat', self.projects)

    def update_project_list(self):
        self.project_listbox.delete(0, tk.END)
        for project in self.projects:
            self.project_listbox.insert(tk.END, project.name)

    def update_task_list(self, project):
        self.task_listbox.delete(0, tk.END)
        for task in project.tasks:
            self.task_listbox.insert(tk.END, str(task))

    def on_closing(self):
        DataManager.save_data('tasks.dat', self.projects)
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()
