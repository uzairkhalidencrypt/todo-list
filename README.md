# My To-Do List

A tiny full-stack app: **HTML** for the page, **CSS** for the look, **Python** for saving tasks.

## How to explain it (no jargon)

Imagine a cafe:

- **HTML** is the counter and the menu: the title, the text box, the list, the buttons.
- **CSS** is the paint job: cream background, rounded cards, green Add button.
- **Python** is the notebook behind the counter. When you type a task and press Add, Python writes it down. When you check it off, Python marks it done. When you delete it, Python erases it.

The notebook is a file called `tasks.json`. If you close the app and open it later, the list is still there.

## Run it

You need Python 3 installed.

```bash
cd ~/todo-list
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Then open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

## What each file does

| File | Role |
| --- | --- |
| `templates/index.html` | The page structure (what is on the screen) |
| `static/style.css` | Colors, spacing, and layout |
| `app.py` | Receives button clicks, updates the list, shows the page again |
| `tasks.json` | Saved tasks (created automatically) |

There is no extra JavaScript. Each button is a normal HTML form that talks to Python.
