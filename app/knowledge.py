from __future__ import annotations
from pathlib import Path
from typing import List, Dict

from .storage import load_json, save_json, DATA_DIR

DOCS_FILE = 'knowledge.json'


def _load_docs() -> List[Dict]:
    return load_json(DOCS_FILE)


def _save_docs(docs: List[Dict]) -> None:
    save_json(DOCS_FILE, docs)


def add_document(title: str, content: str) -> Dict:
    docs = _load_docs()
    doc = {
        'id': len(docs) + 1,
        'title': title,
        'content': content
    }
    docs.append(doc)
    _save_docs(docs)
    return doc


def search_documents(query: str) -> List[Dict]:
    docs = _load_docs()
    q = query.lower()
    return [d for d in docs if q in d['title'].lower() or q in d['content'].lower()]
