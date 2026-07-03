# FastAPI Project Example

This example demonstrates how to use contributor-ready with a FastAPI project.

## Project Structure

```
my-fastapi-project/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── user.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── user.py
│   ├── api/
│   │   ├── __init__.py
│   │   └── v1/
│   │       ├── __init__.py
│   │       └── users.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── user_service.py
│   └── utils/
│       ├── __init__.py
│       └── helpers.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_users.py
│   └── test_items.py
├── alembic/
│   └── versions/
├── docs/
│   └── api.md
├── requirements.txt
├── requirements-dev.txt
├── pyproject.toml
├── alembic.ini
├── Dockerfile
├── docker-compose.yml
├── README.md
├── LICENSE
└── .github/
    └── workflows/
        └── ci.yml
```

## Detection

When analyzing a FastAPI project, contributor-ready detects:

- **Framework**: FastAPI (by `fastapi` in requirements or pyproject.toml)
- **Language**: Python (by `.py` files)
- **Package Manager**: pip, poetry, or conda (by lock files)
- **Build System**: setuptools, poetry, or hatch (by pyproject.toml)
- **Test Framework**: pytest, httpx (by test files and config)
- **Linter**: flake8, pylint, ruff (by config files)
- **Formatter**: black, isort (by config files)
- **Database**: SQLAlchemy, Tortoise, or motor (by dependencies)
- **Migration**: Alembic (by alembic.ini)

## Generated Files

### README.md

```markdown
# My FastAPI Project

A FastAPI application for {description}.

## Features

- **Fast** — Built on FastAPI for high performance
- **Async** — Full async/await support
- **Type Safe** — Pydantic models for validation
- **Auto Docs** — Automatic OpenAPI documentation

## Installation

### From Source

```bash
git clone https://github.com/{owner}/{repo}.git
cd {repo}
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### Using Docker

```bash
docker-compose up --build
```

## Quick Start

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

# Run with: uvicorn app.main:app --reload
```

## API Documentation

### Interactive Docs

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Endpoints

#### Users

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/users` | List all users |
| GET | `/api/v1/users/{id}` | Get user by ID |
| POST | `/api/v1/users` | Create a user |
| PUT | `/api/v1/users/{id}` | Update a user |
| DELETE | `/api/v1/users/{id}` | Delete a user |

#### Items

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/items` | List all items |
| GET | `/api/v1/items/{id}` | Get item by ID |
| POST | `/api/v1/items` | Create an item |
| PUT | `/api/v1/items/{id}` | Update an item |
| DELETE | `/api/v1/items/{id}` | Delete an item |

## Usage

### Creating a User

```python
import httpx

async def create_user():
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "http://localhost:8000/api/v1/users",
            json={
                "name": "John Doe",
                "email": "john@example.com"
            }
        )
        return response.json()
```

### Using Dependencies

```python
from fastapi import Depends, FastAPI
from app.dependencies import get_db, get_current_user

app = FastAPI()

@app.get("/users/me")
async def read_users_me(current_user = Depends(get_current_user)):
    return current_user
```

## Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `DATABASE_URL` | Database connection string | `sqlite:///./app.db` |
| `SECRET_KEY` | JWT secret key | (required) |
| `DEBUG` | Enable debug mode | `false` |
| `ALLOWED_ORIGINS` | CORS allowed origins | `http://localhost:3000` |

### Configuration File

Create a `.env` file:

```env
DATABASE_URL=postgresql://user:password@localhost/dbname
SECRET_KEY=your-secret-key
DEBUG=true
ALLOWED_ORIGINS=http://localhost:3000,http://localhost:8080
```

## Database

### Migrations

```bash
# Generate migration
alembic revision --autogenerate -m "description"

# Apply migrations
alembic upgrade head

# Rollback
alembic downgrade -1
```

### Models

```python
from sqlalchemy import Column, Integer, String
from app.database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
```

## Testing

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app

# Run specific tests
pytest tests/test_users.py
```

### Test Structure

```python
import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_create_user():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post(
            "/api/v1/users",
            json={"name": "Test User", "email": "test@example.com"}
        )
        assert response.status_code == 200
        assert response.json()["name"] == "Test User"
```

## Docker

### Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Docker Compose

```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://postgres:postgres@db/postgres
      - SECRET_KEY=your-secret-key
    depends_on:
      - db
  
  db:
    image: postgres:15
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

## Deployment

### Heroku

```bash
# Login to Heroku
heroku login

# Create app
heroku create my-fastapi-app

# Set environment variables
heroku config:set SECRET_KEY=your-secret-key
heroku config:set DATABASE_URL=your-database-url

# Deploy
git push heroku main
```

### AWS

See [DEPLOYMENT.md](DEPLOYMENT.md) for AWS deployment instructions.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT — see [LICENSE](LICENSE) for details.
```

### CONTRIBUTING.md

```markdown
# Contributing to My FastAPI Project

Thank you for your interest in contributing!

## Getting Started

### Prerequisites

- Python 3.10 or higher
- pip
- PostgreSQL (for production)
- Docker (optional)

### Development Setup

1. Fork the repository
2. Clone your fork
3. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   ```
5. Set up environment:
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```
6. Run migrations:
   ```bash
   alembic upgrade head
   ```

### Making Changes

1. Create a branch for your changes
2. Make your changes
3. Run tests:
   ```bash
   pytest
   ```
4. Run linter:
   ```bash
   flake8 app/
   ```
5. Format code:
   ```bash
   black app/
   ```
6. Commit your changes

### Commit Convention

```
{type}({scope}): {description}
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `style`: Formatting
- `refactor`: Code refactoring
- `test`: Adding tests
- `chore`: Maintenance

### Submitting a Pull Request

1. Push your branch
2. Create a pull request
3. Fill out the PR template
4. Wait for review

## Code Style

- Follow PEP 8
- Use Black for formatting
- Use isort for import sorting
- Use flake8 for linting
- Use type hints

## Testing

- Write tests for new features
- Maintain test coverage
- Use pytest for testing
- Use httpx for API testing
- Use async tests for async code

## API Guidelines

- Use proper HTTP status codes
- Use Pydantic models for validation
- Use proper error handling
- Document endpoints with docstrings
- Use proper naming conventions

## Questions?

If you have questions, feel free to:

- Open a discussion
- Ask in Discord
- Create an issue with the `question` label
```

### requirements.txt

```txt
fastapi==0.104.1
uvicorn[standard]==0.24.0
sqlalchemy==2.0.23
alembic==1.13.0
pydantic==2.5.3
pydantic-settings==2.1.0
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
python-multipart==0.0.6
httpx==0.25.2
```

### requirements-dev.txt

```txt
-r requirements.txt
pytest==7.4.3
pytest-asyncio==0.23.3
pytest-cov==4.1.0
httpx==0.25.2
flake8==6.1.0
black==23.12.1
isort==5.13.2
mypy==1.8.0
```

### .github/workflows/ci.yml

```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    
    services:
      postgres:
        image: postgres:15
        env:
          POSTGRES_USER: postgres
          POSTGRES_PASSWORD: postgres
          POSTGRES_DB: test_db
        ports:
          - 5432:5432
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements-dev.txt
      
      - name: Lint with flake8
        run: |
          flake8 app/
      
      - name: Format with black
        run: |
          black --check app/
      
      - name: Test with pytest
        env:
          DATABASE_URL: postgresql://postgres:postgres@localhost/test_db
          SECRET_KEY: test-secret-key
        run: |
          pytest --cov=app
```

## Checklist

When using contributor-ready with a FastAPI project:

- [ ] Detect FastAPI framework
- [ ] Detect database (SQLAlchemy, Tortoise, etc.)
- [ ] Detect migration tool (Alembic)
- [ ] Detect testing framework (pytest, httpx)
- [ ] Check for API documentation
- [ ] Check for Pydantic models
- [ ] Check for proper error handling
- [ ] Generate FastAPI-specific README
- [ ] Generate FastAPI-specific CONTRIBUTING.md
- [ ] Generate FastAPI-specific CI workflow
- [ ] Generate FastAPI-specific SECURITY.md
- [ ] Generate API documentation
