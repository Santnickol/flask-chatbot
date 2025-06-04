from __future__ import annotations
import uuid
from datetime import datetime
from typing import List, Dict

from .storage import load_json, save_json

TASKS_FILE = 'tasks.json'


def _load_tasks() -> List[Dict]:
    return load_json(TASKS_FILE)


def _save_tasks(tasks: List[Dict]) -> None:
    save_json(TASKS_FILE, tasks)


def create_task(title: str, description: str = '', assignee: str = '', due_date: str | None = None) -> Dict:
    tasks = _load_tasks()
    task = {
        'id': str(uuid.uuid4()),
        'title': title,
        'description': description,
        'assignee': assignee,
        'due_date': due_date,
        'status': 'todo',
        'created_at': datetime.utcnow().isoformat()
    }
    tasks.append(task)
    _save_tasks(tasks)
    return task


def list_tasks() -> List[Dict]:
    return _load_tasks()


def update_task(task_id: str, **updates) -> Dict | None:
    tasks = _load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task.update(updates)
            _save_tasks(tasks)
            return task
    return None
