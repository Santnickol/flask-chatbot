from __future__ import annotations
import uuid
from typing import List, Dict

from .storage import load_json, save_json

RISKS_FILE = 'risks.json'


def _load_risks() -> List[Dict]:
    return load_json(RISKS_FILE)


def _save_risks(risks: List[Dict]) -> None:
    save_json(RISKS_FILE, risks)


def add_risk(name: str, description: str) -> Dict:
    risks = _load_risks()
    risk = {
        'id': str(uuid.uuid4()),
        'name': name,
        'description': description,
        'status': 'open'
    }
    risks.append(risk)
    _save_risks(risks)
    return risk


def list_risks() -> List[Dict]:
    return _load_risks()
