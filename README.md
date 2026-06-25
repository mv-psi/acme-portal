# ACME Portal

A minimal Flask web app: a login form, and a page that greets the user after a
successful login. Intended as a small, self-contained local target for security
demonstrations.

The complete deployment lives in [`demo-talk/`](demo-talk/).

## Run

```bash
./demo-talk/start.sh        # syncs deps and serves on http://localhost:8888
```

Or manually:

```bash
cd demo-talk
uv sync
uv run acme-portal
```

Login: **`pentest`** / **`we-got-graybox-reds`** → `hello pwned`.

Override `PORT`, `PORTAL_USER`, `PORTAL_PASS`, or `SECRET_KEY` via environment
variables.

## Routes

- `GET /` — login form
- `POST /` — submit credentials
- `GET /dashboard` — post-login page (`hello pwned`); redirects to `/` if not logged in
- `GET /logout` — clear the session
