from project import add_contact, search_contact, delete_contact

def test_add_contact():
    contacts = {}
    assert add_contact(contacts, "Alice", "12345", "alice@example.com") is True
    assert "Alice" in contacts
    assert add_contact(contacts, "Alice", "12345", "alice@example.com") is False

def test_search_contact():
    contacts = {"Bob": {"phone": "67890", "email": "bob@example.com"}}
    assert search_contact(contacts, "Bob") == {"phone": "67890", "email": "bob@example.com"}
    assert search_contact(contacts, "Charlie") is None

def test_delete_contact():
    contacts = {"Eve": {"phone": "11111", "email": "eve@example.com"}}
    assert delete_contact(contacts, "Eve") is True
    assert "Eve" not in contacts
    assert delete_contact(contacts, "Eve") is False
