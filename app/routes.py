from flask import Blueprint, request, jsonify, render_template

from .tasks import create_task, list_tasks, update_task
from .risks import add_risk, list_risks
from .knowledge import add_document, search_documents
from .llm import GeminiClient

bp = Blueprint('routes', __name__)


@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/tasks', methods=['GET', 'POST'])
def tasks():
    if request.method == 'POST':
        data = request.json or {}
        task = create_task(
            title=data.get('title', ''),
            description=data.get('description', ''),
            assignee=data.get('assignee', ''),
            due_date=data.get('due_date'),
        )
        return jsonify(task), 201
    return jsonify(list_tasks())


@bp.route('/tasks/<task_id>', methods=['PATCH'])
def patch_task(task_id: str):
    data = request.json or {}
    task = update_task(task_id, **data)
    if not task:
        return jsonify({'error': 'not found'}), 404
    return jsonify(task)


@bp.route('/risks', methods=['GET', 'POST'])
def risks():
    if request.method == 'POST':
        data = request.json or {}
        risk = add_risk(data.get('name', ''), data.get('description', ''))
        return jsonify(risk), 201
    return jsonify(list_risks())


@bp.route('/knowledge', methods=['GET', 'POST'])
def knowledge():
    if request.method == 'POST':
        data = request.json or {}
        doc = add_document(data.get('title', ''), data.get('content', ''))
        return jsonify(doc), 201
    query = request.args.get('q', '')
    return jsonify(search_documents(query))


@bp.route('/chat', methods=['POST'])
def chat():
    data = request.json or {}
    messages = data.get('messages', [])
    try:
        client = GeminiClient()
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    try:
        reply = client.chat(messages)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    return jsonify({'reply': reply})
