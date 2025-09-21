# LibraryProject - Advanced Features and Security

## Project Overview
This Django project demonstrates the implementation of:

- A **Custom User Model** with additional fields (`date_of_birth`, `profile_photo`).
- **Book management** with CRUD functionality.
- **Custom permissions** for the Book model (`can_view`, `can_create`, `can_edit`, `can_delete`).
- **Groups and permissions**:
  - Groups: `Admins`, `Editors`, `Viewers`.
  - Permissions assigned according to group roles.
- Enforcement of permissions in views using Django decorators.

## Apps
- `bookshelf`: Manages the `Book` model and permissions.
- `accounts`: Contains the custom user model (if separated).

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd LibraryProject

