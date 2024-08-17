## FastAPI Boilerplate

A FastAPI boilerplate project designed to help you kickstart your API development with best practices and essential features.

### Features

- **Database Integration**: Configured with SQLAlchemy for ORM and database management.
- **Authentication and Authorization**: Basic setup for user management and access control.
- **Environment Configuration**: Uses `.env` files for easy management of sensitive settings.
- **Modular Architecture**: Well-organized structure for easy extension and maintenance.

### Getting Started

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/Phanith-LIM/fastapi_boilerplate.git
    cd fastapi_boilerplate
    ```

2. **Set Up Environment:**

    - Copy `.env.example` to `.env`:

      ```bash
      cp .env.example .env
      ```

    - Update the `.env` file with your actual configuration values.

3. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Application:**

    ```bash
    uvicorn app.main:app --reload
    ```

5. **Migrations**

    - **Initialize Alembic** (if not already initialized):

      ```bash
      alembic init alembic
      ```

    - **Create a Migration Script:**

      After making changes to your models, generate a new migration script:

      ```bash
      alembic revision --autogenerate -m "description of the changes"
      ```

    - **Apply Migrations:**

      Apply the generated migration script to your database:

      ```bash
      alembic upgrade head
      ```

    - **Downgrade Migrations (if needed):**

      If you need to revert to a previous migration, use:

      ```bash
      alembic downgrade <revision_id>
      ```

### Contributing

Feel free to open issues or submit pull requests. Contributions are welcome!

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE.txt) file for details.