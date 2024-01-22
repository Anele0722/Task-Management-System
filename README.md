# Project Management System
## Overview

Welcome to the Project Management System, a simple, effective, and reliable tool designed to ensure smooth and efficient execution of projects. This system incorporates key features to enhance project management, including a unique identifier and description for each project, task assignments, deadlines, task dependencies, progress tracking, and a centralized database for easy access and updates.

# Features
## A. Project Details
Each project is assigned a unique identifier and a clear description. Tasks and team members are associated with each project, providing a comprehensive overview.

## B. Deadline Management
The set_deadline() method is utilized to set deadlines for tasks, promoting timely completion. This ensures that team members adhere to specified timeframes, contributing to project success.

## C. Task Dependencies
By setting task dependencies, the system ensures that tasks are carried out in the correct order, optimizing workflow efficiency. Teams can manage dependencies to enhance project coordination.

## D. Progress Tracking
The system employs the complete() method to mark tasks as completed. The get_progress() method calculates project progress, displaying the percentage of completed tasks. This allows teams to make informed decisions and adjust their approach as needed.

## E. Centralized Database
A secure and centralized database facilitates easy access and updates to project data. This promotes collaboration among team members, ensuring that information is stored in a reliable and organized manner.

## F. Interactive Menu System
An interactive menu system provides users with various options, such as creating tasks, projects, assigning team members, checking project progress, and exiting the system. This user-friendly interface enhances the overall experience.

# To-Do List
The To-Do List is a vital tool within the system, serving as a checklist for tasks required to achieve project goals. Each task includes details such as a brief name, a comprehensive description, assigned team member, task dependencies, and a deadline. These details aid in effective task management and project organization.

## Task Details:
Task Name: Brief description of the task.
Description: Additional information or instructions for task completion.
Assigned Team Member: Designated person responsible for task completion.
Dependencies: Notation of tasks that must be completed before others can begin.
Deadline: Date by which the task should be completed.
Challenges Faced and Solutions
Deadline Validation
Challenge: Ensuring correct deadline formats.
Solution: Implemented a validation mechanism to check if entered dates follow the required format (YYYY-MM-DD).
