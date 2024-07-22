class Bookstore:
    def __init__(self):
        self.stock = {}

    # Method to add a new publication
    def add_publication(self, title, quantity):
        if title in self.stock:
            print("Publication already exists. Use update_quantity to change the quantity.")
        else:
            self.stock[title] = quantity
            print(f"Publication added: {title} with quantity: {quantity}")

    # Method to update the quantity of an existing publication
    def update_quantity(self, title, quantity):
        if title in self.stock:
            self.stock[title] = quantity
            print(f"Updated {title} to quantity: {quantity}")
        else:
            print("Publication not found. Use add_publication to add new publications.")

    # Method to search for a publication by title
    def search_publication(self, title):
        return self.stock.get(title)

# Demonstration of how to use the Bookstore class
if __name__ == "__main__":
    bookstore = Bookstore()

    # Add new publications
    bookstore.add_publication("Harry Potter and the Philosopher's Stone", 10)
    bookstore.add_publication("The Hobbit", 5)

    # Update the quantity of an existing publication
    bookstore.update_quantity("Harry Potter and the Philosopher's Stone", 15)

    # Search for a publication by title
    quantity = bookstore.search_publication("The Hobbit")
    if quantity is not None:
        print(f"The Hobbit is available with quantity: {quantity}")
    else:
        print("The Hobbit is not in stock.")
