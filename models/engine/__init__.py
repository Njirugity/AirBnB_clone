class FileStorage:
    """Handles serialization and deserialization of objects to and from JSON files."""

    __file_path = "file.json"  # Path to the JSON file
    __objects = {}            # Dictionary to store all objects

    def __init__(self):
        """Initialize the FileStorage class."""
        self.classes = {
            "BaseModel": BaseModel,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review
        }

