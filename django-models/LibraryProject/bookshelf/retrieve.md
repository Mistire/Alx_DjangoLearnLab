
---

### `retrieve.md`

```markdown
# Retrieve Book Instance

```python
from bookshelf.models import Book
retrieved_book = Book.objects.get(title="1984")
print(retrieved_book.title, retrieved_book.author, retrieved_book.publication_year)
# 1984 George Orwell 1949
