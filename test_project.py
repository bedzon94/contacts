from project import add_contact, list_contacts, search_contact, delete_contact


def main():
    test_add_contact()
    test_list_contacts()
    test_search_contact()
    test_delete_contact()


def test_add_contact(monkeypatch):
    inputs = iter(["Norris", "212-505-9000", "norris@aol.com"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    assert add_contact() == "Norris has been added to your contacts!"


def test_list_contacts():
    list_contacts()


def test_search_contact(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "Norris")
    search_contact()


def test_delete_contact(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "Norris")
    delete_contact()





if __name__ == "__main__":
    main()

