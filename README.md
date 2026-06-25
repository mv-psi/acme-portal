# ACME Portal

A minimal Flask web app: a login form, and a page that greets the user after a
successful login. Intended as a small, self-contained local target for security
demonstrations.

## Run

```bash
uv sync
uv run acme-portal        # serves on http://localhost:8080
```

Or run the module directly:

```bash
uv run python app.py
```

Set `PORT`, `PORTAL_USER`, `PORTAL_PASS`, or `SECRET_KEY` via environment
variables to override the defaults.

## Routes

- `GET /` — login form
- `POST /` — submit credentials
- `GET /dashboard` — post-login page (`hello pwned`); redirects to `/` if not logged in
- `GET /logout` — clear the session
