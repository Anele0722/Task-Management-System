# Importing datetime module for handling deadlines
from datetime import datetime

# Initializing variables for each constant: identifier, name, description and an empty list of tasks
class Project:
    def __init__(self, identifier, name, description):
        self.identifier = identifier
        self.name = name
        self.description = description
        self.tasks = []

    # Adding a task to the project's list of tasks
    # by defining a method that takes in the task as a parameter and then appends it to the list. 
    # This method can be called whenever a new task needs to be added to the project.
    def add_task(self, task):
        self.tasks.append(task)

    # Method to assign a team member to a task within the project
    def assign_team_member(self, task, team_member):
        task.assign_team_member(team_member)

    # Method to set a task's dependency within the project
    def set_dependency(self, task, dependency):
        task.set_dependency(dependency)

    # Method to establish a project task's deadline
    def set_deadline(self, task, deadline):
        task.set_deadline(deadline)

    # Method to calculate and return project progress
    def get_progress(self):
        total_tasks = len(self.tasks)
        completed_tasks = sum(task.is_completed() for task in self.tasks)
        try:
            return completed_tasks / total_tasks * 100 if total_tasks > 0 else 0
        except ZeroDivisionError:
            print("Error: Division by zero. Please make sure there are tasks in the project.")
            return 0


# Creating a Task class with an init method to set its attributes
class Task:
    def __init__(self, identifier, name, description):
        self.identifier = identifier
        self.name = name
        self.description = description
        self.team_member = None
        self.dependency = None
        self.deadline = None
        self.completed = False

    # Method to assign a team member to the task
    def assign_team_member(self, team_member):
        self.team_member = team_member

    # to set a task's dependency
    def set_dependency(self, dependency):
        try:
            datetime.strptime(dependency, "%Y-%m-%d")
            self.dependency = dependency
        except ValueError:
            print("Invalid dependency format. Please use YYYY-MM-DD.")

    # setting a task's deadline
    def set_deadline(self, deadline):
        try:
            datetime.strptime(deadline, "%Y-%m-%d")
            self.deadline = deadline
        except ValueError:
            print("Invalid deadline format. Please use YYYY-MM-DD.")

    # to check if the task is completed
    def is_completed(self):
        return self.completed

    # Marking the task as completed
    def complete(self):
        self.completed = True


class TeamMember:
    def __init__(self, name):
        self.name = name


# Database (list) for storing tasks and projects
tasks_database = []
projects_database = []


# Functions for user prompts and menu system
def create_task_interactive():
    identifier = input("Enter task identifier: ")
    name = input("Enter task name: ")
    description = input("Enter task description: ")
    return Task(identifier, name, description)


def create_project_interactive():
    identifier = input("Enter project identifier: ")
    name = input("Enter project name: ")
    description = input("Enter project description: ")
    return Project(identifier, name, description)


def assign_team_member_interactive(project):
    task_id = input("Enter task identifier to assign team member: ")
    task = next((t for t in project.tasks if t.identifier == task_id), None)
    if task:
        team_member_name = input("Enter team member name: ")
        team_member = TeamMember(team_member_name)
        project.assign_team_member(task, team_member)
    else:
        print(f"Task with identifier '{task_id}' not found.")

# displaying a simple menu of options to the user
def display_menu():
    print("1. Create Task")
    print("2. Create Project")
    print("3. Assign Team Member")
    print("4. Get Project Progress")
    print("5. Exit")


def user_menu_choice():
    return input("Enter your choice: ")


# Interactive menu system to keep the program running until the user chooses to exit

while True:
    display_menu()
    choice = user_menu_choice()

    # Calls the create_task_interactive() function to interactively create a task.The created task is then appended to the tasks_database list.
    if choice == "1":
        task = create_task_interactive()
        tasks_database.append(task)
        if projects_database:
            project_id = input("Enter project identifier to add the task: ")
            project = next((p for p in projects_database if p.identifier == project_id), None)
            if project:
                project.add_task(task)
            else:
                print(f"Project with identifier '{project_id}' not found.")

    # Create Project
    # checks if there are any projects in the projects_database.
    elif choice == "2":
        project = create_project_interactive()
        projects_database.append(project)

    # Assign Team Member
    elif choice == "3":
        if not projects_database:
            print("No projects available. Please create a project first.")
        else:
            project_id = input("Enter project identifier: ")
            project = next((p for p in projects_database if p.identifier == project_id), None)
            if project:
                assign_team_member_interactive(project)
            else:
                print(f"Project with identifier '{project_id}' not found.")

    # Get Project Progress
    elif choice == "4":
        if not projects_database:
            print("No projects available. Please create a project first.")
        else:
            project_id = input("Enter project identifier: ")
            project = next((p for p in projects_database if p.identifier == project_id), None)
            if project:
                try:
                    progress = project.get_progress()
                    print(f"Project progress: {progress}%")
                except ZeroDivisionError:
                    print("No tasks found in the project.")
                except Exception as e:
                    print(f"An error occurred: {str(e)}")
            else:
                print(f"Project with identifier '{project_id}' not found.")

    # Exit
    elif choice == "5":
        break

    else:
        print("Invalid choice. Please enter a valid option.")
