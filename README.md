# Task Management System

## Overview

This project is a simple **Python Task Management System** that allows users to add tasks, mark tasks as complete, view pending tasks, and track progress.
The program uses **functions, modules, packages, and input validation** to organize the code and manage tasks effectively.

## Project Structure
task_project/
│
├── main.py
│
└── task_manager/
    ├── __init__.py
    ├── task_utils.py
    └── validation.py

**main.py** – Runs the program and provides the menu interface.
**task_utils.py** – Contains functions for managing tasks.
**validation.py** – Contains functions to validate user input.

## Task Structure

Each task is stored as a dictionary:

task = {
 "title": "Groceries",
 "description": "Shop at Market Basket for food",
 "due_date": "2024-06-26",
 "completed": False
}

Tasks are stored in a **list of dictionaries**.

## Functions

**Validation Functions**

* `validate_task_title`
* `validate_task_description`
* `validate_due_date`

**Task Functions**

* `add_task`
* `mark_task_as_complete`
* `view_pending_tasks`
* `calculate_progress`

## How to Run

Run the program from the project folder:

python3 main.py

## Features

* Add new tasks
* Mark tasks as completed
* View pending tasks
* Track task progress

## Concepts Used

* Functions
* Modules and Packages
* Dictionaries and Lists
* Input Validation

## Author
Sharon bochaberi.