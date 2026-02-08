# Sticky Note Task Tracker

A minimal task tracker designed to feel like a real yellow sticky note.
Tasks are written from top to bottom, crossed out with a checkbox, and removed with a subtle hover action.

The app runs as a small desktop window and dynamically resizes as tasks are added, so the sticky note always fits the content.

---

## Features
- Add tasks in a natural, handwritten-style interface
- Tasks appear in the order they are written (top → bottom)
- Checkbox to mark tasks complete or incomplete
- Completed tasks are crossed out
- Delete button appears only on hover, like erasing a note
- Input field sits directly below the last task
- Window automatically resizes as tasks are added or removed
- No scrolling or unnecessary UI elements

---

## Tech Stack
- Python 3
- Flask
- SQLite
- HTML / CSS (Jinja templates)
- pywebview (desktop wrapper)

---

## How to run locally

1. Clone the repository  
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
3. Install Dependencies:
   ```bash
   pip install -r requirements.txt
4. Run the app:
   ```bash
   python3 desktop.py
---

## What I learned

- Building a Flask application with clean route separation
- Using SQLite for lightweight data persistence
- Implementing full CRUD functionality
- Passing data from Flask routes into Jinja templates
- Designing UI behaviour to match real-world mental models
- Styling an interface using only HTML and CSS (no frameworks)
- Wrapping a web app into a desktop window using pywebview
- Dynamically resizing a desktop window based on DOM content
- Iterating on both functionality and user experience