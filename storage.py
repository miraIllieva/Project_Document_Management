from project.category import Category
from project.document import Document
from project.topic import Topic

class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        for category in self.categories:
            if category.id == category_id:
                category.name == new_name
                break
    def edit_document(self, document_id: int, new_file_name: str):
        for document in self.documents:
            if document.id == document_id:
                document.file_name == new_file_name
                break
    def delete_category(self, category_id: int):
        self.categories = [c for c in self.categories if category_id != category_id]

    def delete_document(self, document_id: int):
        self.documents = [document for document in self.documents if document.id != document_id]

    def get_document(self, document_id: int):
        for document in self.documents:
            if document.id == document_id:
                return document
        return None

    def __repr__(self):
        return f"\n".join((str(document) for document in self.documents))

