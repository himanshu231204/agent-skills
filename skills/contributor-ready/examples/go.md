# Go Project Example

This example demonstrates how to use contributor-ready with a Go project.

## Project Structure

```
my-go-project/
├── cmd/
│   └── server/
│       └── main.go
├── internal/
│   ├── handler/
│   │   └── user.go
│   ├── service/
│   │   └── user.go
│   ├── repository/
│   │   └── user.go
│   └── model/
│       └── user.go
├── pkg/
│   └── utils/
│       └── helpers.go
├── api/
│   └── openapi.yaml
├── migrations/
│   └── 001_initial.sql
├── scripts/
│   └── build.sh
├── go.mod
├── go.sum
├── Makefile
├── Dockerfile
├── README.md
├── LICENSE
└── .github/
    └── workflows/
        └── ci.yml
```

## Detection

When analyzing a Go project, contributor-ready detects:

- **Language**: Go (by `.go` files and `go.mod`)
- **Build System**: go build (by `go.mod`)
- **Testing**: go test (by `_test.go` files)
- **Linter**: golangci-lint (by `.golangci.yml`)
- **Module**: Go modules (by `go.mod` and `go.sum`)

## Generated Files

### README.md

```markdown
# my-go-project

A Go service for {description}.

## Features

- **Fast** — Built with Go for high performance
- **Type Safe** — Strong typing throughout
- **Tested** — Comprehensive test suite
- **Dockerized** — Ready for container deployment

## Installation

### Prerequisites

- Go 1.21 or higher

### From Source

```bash
git clone https://github.com/{owner}/{repo}.git
cd {repo}
go mod download
```

### Build

```bash
go build -o bin/server ./cmd/server
```

## Quick Start

```bash
# Run the server
go run ./cmd/server

# Or run the built binary
./bin/server
```

## Usage

### API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/users` | List all users |
| GET | `/api/v1/users/{id}` | Get user by ID |
| POST | `/api/v1/users` | Create a user |
| PUT | `/api/v1/users/{id}` | Update a user |
| DELETE | `/api/v1/users/{id}` | Delete a user |

### Configuration

| Variable | Description | Default |
|----------|-------------|---------|
| `PORT` | Server port | `8080` |
| `DATABASE_URL` | Database connection string | `postgres://localhost/mydb` |
| `LOG_LEVEL` | Logging level | `info` |

## Development

### Setup

```bash
# Clone and enter the project
git clone https://github.com/{owner}/{repo}.git
cd {repo}

# Install dependencies
go mod download

# Run tests
go test ./...

# Run linter
golangci-lint run
```

### Project Structure

```
cmd/            # Application entrypoints
internal/       # Private application code
├── handler/    # HTTP handlers
├── service/    # Business logic
├── repository/ # Data access
└── model/      # Data models
pkg/            # Public library code
api/            # API definitions
migrations/     # Database migrations
scripts/        # Build and utility scripts
```

### Common Commands

```bash
# Run the server
go run ./cmd/server

# Run tests
go test ./...

# Run tests with coverage
go test -cover ./...

# Run linter
golangci-lint run

# Build
go build -o bin/server ./cmd/server

# Generate API docs
go generate ./...
```

## Testing

```bash
# Run all tests
go test ./...

# Run with verbose output
go test -v ./...

# Run with coverage
go test -cover ./...

# Run specific test
go test -run TestUser ./internal/handler/

# Generate coverage report
go test -coverprofile=coverage.out ./...
go tool cover -html=coverage.out
```

## Deployment

### Docker

```bash
# Build image
docker build -t my-go-project .

# Run container
docker run -p 8080:8080 my-go-project
```

### Docker Compose

```bash
docker-compose up --build
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT — see [LICENSE](LICENSE) for details.
```

### CONTRIBUTING.md

```markdown
# Contributing to my-go-project

Thank you for your interest in contributing!

## Getting Started

### Prerequisites

- Go 1.21 or higher
- golangci-lint
- Docker (optional)

### Development Setup

1. Fork and clone the repository
2. Install dependencies:
   ```bash
   go mod download
   ```
3. Run tests:
   ```bash
   go test ./...
   ```

### Making Changes

1. Create a branch for your changes
2. Make your changes
3. Run tests: `go test ./...`
4. Run linter: `golangci-lint run`
5. Commit your changes

### Commit Convention

```
{type}({scope}): {description}
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`, `perf`

### Code Style

- Follow Effective Go guidelines
- Use `gofmt` for formatting
- Use `golangci-lint` for linting
- Write godoc comments for exported functions
- Handle errors explicitly

## Questions?

Open a discussion or create an issue with the `question` label.
```

### Makefile

```makefile
.PHONY: build test lint run clean

# Build
build:
	go build -o bin/server ./cmd/server

# Run
run:
	go run ./cmd/server

# Test
test:
	go test ./...

test-cover:
	go test -coverprofile=coverage.out ./...
	go tool cover -html=coverage.out

# Lint
lint:
	golangci-lint run

# Clean
clean:
	rm -rf bin/
	rm -f coverage.out

# Docker
docker-build:
	docker build -t my-go-project .

docker-run:
	docker run -p 8080:8080 my-go-project
```

### go.mod

```
module github.com/{owner}/{repo}

go 1.21

require (
    github.com/gin-gonic/gin v1.9.1
    github.com/jackc/pgx/v5 v5.5.0
    go.uber.org/zap v1.26.0
)
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
    strategy:
      matrix:
        go-version: ['1.21', '1.22']

    steps:
      - uses: actions/checkout@v4

      - name: Setup Go ${{ matrix.go-version }}
        uses: actions/setup-go@v5
        with:
          go-version: ${{ matrix.go-version }}

      - name: Download dependencies
        run: go mod download

      - name: Lint
        uses: golangci/golangci-lint-action@v3
        with:
          version: latest

      - name: Test
        run: go test -race -coverprofile=coverage.out ./...

      - name: Build
        run: go build -o bin/server ./cmd/server
```

## Checklist

When using contributor-ready with a Go project:

- [ ] Detect Go version from go.mod
- [ ] Detect HTTP framework (gin, echo, fiber, etc.)
- [ ] Detect database driver
- [ ] Check for proper project layout (cmd/, internal/, pkg/)
- [ ] Check for Makefile
- [ ] Check for Dockerfile
- [ ] Generate Go-specific README
- [ ] Generate Go-specific CONTRIBUTING.md
- [ ] Generate Go-specific CI workflow
