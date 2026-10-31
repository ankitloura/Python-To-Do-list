
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Store tasks in memory
tasks = []
next_id = 1


@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["POST"])
def add_task():
    global next_id

    title = request.form.get("title", "").strip()

    if title:
        tasks.append({
            "id": next_id,
            "title": title,
            "done": False
        })
        next_id += 1

    return redirect(url_for("index"))


@app.route("/toggle/<int:task_id>", methods=["POST"])
def toggle_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = not task["done"]
            break

    return redirect(url_for("index"))


@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    global tasks

    tasks = [
        task for task in tasks
        if task["id"] != task_id
    ]

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
