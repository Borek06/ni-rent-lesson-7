"""
Czarna lista najemców (B) - wymagania:
- models.py: BlacklistEntry(name, reason) + from_json_file(); Parameters.blacklist_json_path
- data/blacklist.json: lista wpisów {"name", "reason"}, min. 1
- Manager.blacklist: lista BlacklistEntry wczytana z pliku
- Manager.is_blacklisted(name) -> bool (bez rozróżniania wielkości liter i spacji)
- Manager.get_blacklist_reason(name) -> str lub None
"""
from src.models import BlacklistEntry, Parameters
from src.manager import Manager


def test_is_blacklisted():
    manager = Manager(Parameters())
    manager.blacklist = [BlacklistEntry(name='Jan Kowalski', reason='Zaległości w czynszu')]

    assert manager.is_blacklisted('Jan Kowalski') is True
    assert manager.is_blacklisted('  jan KOWALSKI ') is True
    assert manager.is_blacklisted('Piotr Wiśniewski') is False


def test_get_blacklist_reason():
    manager = Manager(Parameters())
    manager.blacklist = [BlacklistEntry(name='Jan Kowalski', reason='Zaległości w czynszu')]

    assert manager.get_blacklist_reason('Jan Kowalski') == 'Zaległości w czynszu'
    assert manager.get_blacklist_reason('Piotr Wiśniewski') is None


def test_blacklist_loaded_from_file():
    manager = Manager(Parameters())

    assert len(manager.blacklist) >= 1
    assert all(isinstance(entry, BlacklistEntry) for entry in manager.blacklist)