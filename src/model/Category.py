class Category:
    def __init__(self, name):
        self._name = name
        self._items = []

    def add_item(self, menu_item):
        self._items.append(menu_item)

    def print_items(self):
        for menu_item in self._items:
            print(menu_item)
