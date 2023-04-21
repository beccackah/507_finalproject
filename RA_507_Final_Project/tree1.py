class Node:
    def __init__(self, title, rating, genre):
        self.title = title
        self.rating = rating
        self.genre = genre
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, title, rating, genre):
        new_node = Node(title, rating, genre)
        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            while True:
                if rating < current.rating:
                    if current.left is None:
                        current.left = new_node
                        break
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = new_node
                        break
                    else:
                        current = current.right

    def search(self, rating):
        current = self.root
        while current is not None:
            if current.rating == rating:
                return f"Title: {current.title}, Rating: {current.rating}, Genre: {current.genre}"
            elif rating < current.rating:
                current = current.left
            else:
                current = current.right
        return "Movie not found."

# Example usage
bst = BinarySearchTree()
bst.insert("The Shawshank Redemption", 9.3, "Drama")
bst.insert("The Godfather", 9.2, "Crime")
bst.insert("The Dark Knight", 9.0, "Action")
bst.insert("12 Angry Men", 8.9, "Drama")
bst.insert("Schindler's List", 8.9, "Biography")
bst.insert("The Lord of the Rings: The Return of the King", 8.9, "Adventure")

print(bst.search(9.3)) # Output: Title: The Shawshank Redemption, Rating: 9.3, Genre: Drama
print(bst.search(9.2)) # Output: Title: The Godfather, Rating: 9.2, Genre: Crime
print(bst.search(9.5)) # Output: Movie not found.
