## API Endpoints

| Method | Endpoint               | Description                     | Permissions   |
|--------|------------------------|---------------------------------|---------------|
| GET    | /api/books/             | List all books                  | Public        |
| GET    | /api/books/<id>/        | Retrieve single book            | Public        |
| POST   | /api/books/create/      | Create a new book               | Authenticated |
| PUT    | /api/books/<id>/update/ | Update a book                   | Authenticated |
| DELETE | /api/books/<id>/delete/ | Delete a book                   | Authenticated |

## Notes
- Uses DRF Generic Views for efficiency.
- `perform_create()` and `perform_update()` allow custom logic.
- Permissions restrict write actions to authenticated users only.
