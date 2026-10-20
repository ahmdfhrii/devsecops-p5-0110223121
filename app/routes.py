from flask import Blueprint, current_app, jsonify, request
from .utils import validate_title

bp = Blueprint("tasks", __name__)

def _store():
    return current_app.config["STORAGE"]

@bp.get("/tasks")
def list_tasks():
    return jsonify([t.to_dict() for t in _store().all()])

@bp.post("/tasks")
def create_task():
    data = request.get_json(silent=True) or {}
    title = data.get("title")
    if not validate_title(title):
        return jsonify({"error": "title tidak valid"}), 400
    return jsonify(_store().add(title.strip()).to_dict()), 201

@bp.put("/tasks/<int:task_id>/complete")
def complete_task(task_id):
    task = _store().complete(task_id)
    if not task:
        return jsonify({"error": "tidak ditemukan"}), 404
    return jsonify(task.to_dict())

@bp.delete("/tasks/<int:task_id>")
def delete_task(task_id):
    if not _store().delete(task_id):
        return jsonify({"error": "tidak ditemukan"}), 404
    return "", 204