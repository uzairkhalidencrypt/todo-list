"""
Simple to-do list app.

Think of this file as the kitchen notebook:
the webpage (HTML) is the front counter,
this Python code is the person who writes tasks down,
checks them off, and erases them.
"""

from flask import Flask, redirect, render_template, request, url_for
import json
from pathlib import Path

app = Flask(__name__)
TASKS_FILE = Path(__file__).parent / "tasks.json"


def load_tasks():
    """Read the saved list from disk. If the file is missing, start empty."""
    if not TASKS_FILE.exists():
        return []
    with TASKS_FILE.open(encoding="utf-8") as file:
        return json.load(file)


def save_tasks(tasks):
    """Write the current list back to disk so it survives a refresh."""
    with TASKS_FILE.open("w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=2)


def next_id(tasks):
    """Give each new task a unique number, like a ticket at a deli counter."""
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1


@app.route("/")
def home():
    """Show the page with the current list of tasks."""
    tasks = load_tasks()
    remaining = sum(1 for task in tasks if not task["done"])
    return render_template("index.html", tasks=tasks, remaining=remaining)


@app.route("/add", methods=["POST"])
def add_task():
    """Take the text from the form and add it as a new task."""
    title = request.form.get("title", "").strip()
    if title:
        tasks = load_tasks()
        tasks.append({"id": next_id(tasks), "title": title, "done": False})
        save_tasks(tasks)
    return redirect(url_for("home"))


@app.route("/toggle/<int:task_id>", methods=["POST"])
def toggle_task(task_id):
    """Mark a task done, or undo it if it was already done."""
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = not task["done"]
            break
    save_tasks(tasks)
    return redirect(url_for("home"))


@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    """Remove a task from the list completely."""
    tasks = [task for task in load_tasks() if task["id"] != task_id]
    save_tasks(tasks)
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
