# Rust Project Example

This example demonstrates how to use contributor-ready with a Rust project.

## Project Structure

```
my-rust-project/
├── src/
│   ├── lib.rs
│   ├── main.rs
│   ├── models/
│   │   ├── mod.rs
│   │   └── user.rs
│   ├── handlers/
│   │   ├── mod.rs
│   │   └── user.rs
│   ├── services/
│   │   ├── mod.rs
│   │   └── user.rs
│   └── errors.rs
├── tests/
│   ├── integration_test.rs
│   └── user_test.rs
├── benches/
│   └── performance.rs
├── examples/
│   └── basic_usage.rs
├── Cargo.toml
├── Cargo.lock
├── README.md
├── LICENSE
└── .github/
    └── workflows/
        └── ci.yml
```

## Detection

When analyzing a Rust project, contributor-ready detects:

- **Language**: Rust (by `.rs` files and `Cargo.toml`)
- **Build System**: Cargo (by `Cargo.toml`)
- **Testing**: cargo test (by `tests/` directory and `#[test]` attributes)
- **Linter**: Clippy (by `cargo clippy`)
- **Formatter**: rustfmt (by `cargo fmt`)
- **HTTP Framework**: actix-web, axum, or rocket (by dependencies)

## Generated Files

### README.md

```markdown
# my-rust-project

A Rust service for {description}.

## Features

- **Fast** — Built with Rust for maximum performance
- **Type Safe** — Compile-time guarantees
- **Memory Safe** — No null pointers or data races
- **Tested** — Comprehensive test suite

## Installation

### Prerequisites

- Rust 1.75 or higher

### From Source

```bash
git clone https://github.com/{owner}/{repo}.git
cd {repo}
cargo build --release
```

## Quick Start

```bash
# Run the server
cargo run --release
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
| `RUST_LOG` | Log level | `info` |

## Development

### Setup

```bash
# Clone and enter the project
git clone https://github.com/{owner}/{repo}.git
cd {repo}

# Build
cargo build

# Run tests
cargo test

# Run linter
cargo clippy

# Format code
cargo fmt
```

### Project Structure

```
src/
├── lib.rs          # Library root
├── main.rs         # Binary entrypoint
├── models/         # Data models
├── handlers/       # Request handlers
├── services/       # Business logic
└── errors.rs       # Error types
tests/              # Integration tests
benches/            # Benchmarks
examples/           # Usage examples
```

### Common Commands

```bash
# Build
cargo build
cargo build --release

# Run
cargo run
cargo run --release

# Test
cargo test
cargo test -- --nocapture

# Lint
cargo clippy -- -D warnings

# Format
cargo fmt -- --check
cargo fmt

# Generate docs
cargo doc --open

# Benchmarks
cargo bench
```

## Testing

```bash
# Run all tests
cargo test

# Run with output
cargo test -- --nocapture

# Run specific test
cargo test test_user_create

# Run integration tests only
cargo test --test integration_test

# Generate coverage
cargo tarpaulin
```

## Performance

### Benchmarks

```bash
# Run benchmarks
cargo bench

# Run specific benchmark
cargo bench --bench performance
```

### Profiling

```bash
# Install profiling tools
cargo install flamegraph

# Generate flamegraph
cargo flamegraph
```

## Deployment

### Docker

```bash
# Build image
docker build -t my-rust-project .

# Run container
docker run -p 8080:8080 my-rust-project
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT — see [LICENSE](LICENSE) for details.
```

### CONTRIBUTING.md

```markdown
# Contributing to my-rust-project

Thank you for your interest in contributing!

## Getting Started

### Prerequisites

- Rust 1.75 or higher
- cargo-edit (optional)

### Development Setup

1. Fork and clone the repository
2. Build the project:
   ```bash
   cargo build
   ```
3. Run tests:
   ```bash
   cargo test
   ```

### Making Changes

1. Create a branch for your changes
2. Make your changes
3. Run tests: `cargo test`
4. Run linter: `cargo clippy -- -D warnings`
5. Format code: `cargo fmt`
6. Commit your changes

### Commit Convention

```
{type}({scope}): {description}
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`, `perf`

### Code Style

- Follow Rust API Guidelines
- Use `rustfmt` for formatting
- Use `clippy` for linting
- Write doc comments for public items
- Handle errors with `Result` and `?`

## Questions?

Open a discussion or create an issue with the `question` label.
```

### Cargo.toml

```toml
[package]
name = "my-rust-project"
version = "0.1.0"
edition = "2021"
rust-version = "1.75"
description = "A Rust service for {description}"
license = "MIT"
repository = "https://github.com/{owner}/{repo}"

[dependencies]
axum = "0.7"
tokio = { version = "1", features = ["full"] }
serde = { version = "1", features = ["derive"] }
serde_json = "1"
sqlx = { version = "0.7", features = ["runtime-tokio", "postgres"] }
tower-http = { version = "0.5", features = ["cors"] }
tracing = "0.1"
tracing-subscriber = "0.3"

[dev-dependencies]
reqwest = { version = "0.11", features = ["json"] }
tokio-test = "0.4"

[profile.release]
opt-level = 3
lto = true
codegen-units = 1
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

    steps:
      - uses: actions/checkout@v4

      - name: Install Rust
        uses: dtolnay/rust-toolchain@stable
        with:
          components: rustfmt, clippy

      - name: Cache cargo
        uses: actions/cache@v3
        with:
          path: |
            ~/.cargo/registry
            ~/.cargo/git
            target
          key: ${{ runner.os }}-cargo-${{ hashFiles('**/Cargo.lock') }}

      - name: Format check
        run: cargo fmt -- --check

      - name: Lint
        run: cargo clippy -- -D warnings

      - name: Test
        run: cargo test

      - name: Build
        run: cargo build --release
```

## Checklist

When using contributor-ready with a Rust project:

- [ ] Detect Rust edition from Cargo.toml
- [ ] Detect HTTP framework (actix-web, axum, rocket)
- [ ] Detect database driver (sqlx, diesel, sea-orm)
- [ ] Check for proper module structure
- [ ] Check for benchmarks
- [ ] Check for examples
- [ ] Generate Rust-specific README
- [ ] Generate Rust-specific CONTRIBUTING.md
- [ ] Generate Rust-specific CI workflow
