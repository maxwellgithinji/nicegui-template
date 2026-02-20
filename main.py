from nicegui import ui
from datetime import datetime


# ── State ────────────────────────────────────────────────────────────────────
log_entries: list[str] = []
log_container = None  # filled after UI is built


def add_log(message: str) -> None:
    timestamp = datetime.now().strftime("%H:%M:%S")
    entry = f"[{timestamp}]  {message}"
    log_entries.append(entry)
    if log_container is not None:
        with log_container:
            ui.label(entry).classes("log-entry")
        log_container.scroll_to(percent=1.0)


# ── Handlers ─────────────────────────────────────────────────────────────────
def handle_action_1() -> None:
    name_val = name_input.value or "(empty)"
    email_val = email_input.value or "(empty)"
    note_val = note_input.value or "(empty)"
    add_log(f"Action 1 → name={name_val!r}, email={email_val!r}, note={note_val!r}")
    ui.notify("Action 1 executed", color="positive", position="top-right")


def handle_action_2() -> None:
    name_input.value = ""
    email_input.value = ""
    note_input.value = ""
    add_log("Action 2 → form cleared")
    ui.notify("Form cleared", color="warning", position="top-right")


# ── Styles ───────────────────────────────────────────────────────────────────
ui.add_head_html("""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@300;400;500&family=IBM+Plex+Mono:wght@300;400&display=swap" rel="stylesheet">

<style>
  * { box-sizing: border-box; }

  body, .nicegui-content {
    background: #fafafa !important;
    font-family: 'IBM Plex Sans', sans-serif !important;
    color: #1a1a1a !important;
    min-height: 100vh;
  }

  .page-root {
    max-width: 1000px;
    margin: 0 auto;
    padding: 3rem 2rem 4rem;
  }

  /* Title */
  .page-title {
    font-size: 1.4rem !important;
    font-weight: 400 !important;
    letter-spacing: 0.01em;
    color: #1a1a1a !important;
    text-align: center;
    margin-bottom: 3rem;
  }

  /* Layout */
  .layout-cols {
    display: grid;
    grid-template-columns: 1fr 320px;
    gap: 2rem;
    align-items: start;
  }

  /* Cards */
  .card {
    background: #fff;
    border: 1px solid #e8e8e8;
    border-radius: 4px;
    padding: 1.5rem;
  }
  .card-label {
    font-size: 0.7rem !important;
    font-weight: 500 !important;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #999 !important;
    margin-bottom: 1.2rem;
    display: block;
  }

  /* Form inputs */
  .form-card .q-field { margin-bottom: 1rem; }
  .form-card .q-field__control {
    background: #fafafa !important;
    border-radius: 3px !important;
    border: 1px solid #e0e0e0 !important;
    padding: 0 10px !important;
    transition: border-color 0.15s;
    box-shadow: none !important;
  }
  .form-card .q-field__control:hover { border-color: #bbb !important; }
  .form-card .q-field--focused .q-field__control { border-color: #1a1a1a !important; }
  .form-card .q-field__native,
  .form-card .q-field__input {
    color: #1a1a1a !important;
    font-family: 'IBM Plex Sans', sans-serif !important;
    font-size: 0.88rem !important;
  }
  .form-card .q-field__label {
    color: #aaa !important;
    font-family: 'IBM Plex Sans', sans-serif !important;
    font-size: 0.85rem !important;
    font-weight: 300 !important;
  }
  .form-card .q-field__bottom { display: none; }

  /* Buttons */
  .action-card { margin-bottom: 1.2rem; }

  .btn-action-1 {
    width: 100%;
    background: #1a1a1a !important;
    color: #fff !important;
    font-family: 'IBM Plex Sans', sans-serif !important;
    font-weight: 400 !important;
    font-size: 0.82rem !important;
    letter-spacing: 0.04em;
    border-radius: 3px !important;
    height: 40px;
    border: none !important;
    margin-bottom: 0.6rem;
    transition: opacity 0.15s;
    box-shadow: none !important;
  }
  .btn-action-1:hover { opacity: 0.8; }

  .btn-action-2 {
    width: 100%;
    background: #fff !important;
    color: #1a1a1a !important;
    font-family: 'IBM Plex Sans', sans-serif !important;
    font-weight: 400 !important;
    font-size: 0.82rem !important;
    letter-spacing: 0.04em;
    border-radius: 3px !important;
    height: 40px;
    border: 1px solid #e0e0e0 !important;
    transition: border-color 0.15s;
    box-shadow: none !important;
  }
  .btn-action-2:hover { border-color: #1a1a1a !important; }

  /* Log */
  .log-scroll {
    max-height: 240px;
    overflow-y: auto;
  }
  .log-scroll::-webkit-scrollbar { width: 3px; }
  .log-scroll::-webkit-scrollbar-track { background: transparent; }
  .log-scroll::-webkit-scrollbar-thumb { background: #ddd; border-radius: 2px; }

  .log-entry {
    font-family: 'IBM Plex Mono', monospace !important;
    font-size: 0.72rem !important;
    color: #666 !important;
    padding: 4px 0;
    border-bottom: 1px solid #f0f0f0;
    line-height: 1.6;
    word-break: break-all;
  }
  .log-empty {
    font-size: 0.78rem !important;
    color: #ccc !important;
    font-weight: 300 !important;
  }
</style>
""")


# ── UI ────────────────────────────────────────────────────────────────────────
with ui.element("div").classes("page-root"):

    # Title
    ui.label("Page Title").classes("page-title")

    # Two-column grid
    with ui.element("div").classes("layout-cols"):

        # ── LEFT: Form ────────────────────────────────────────
        with ui.element("div").classes("card form-card"):
            ui.label("Form").classes("card-label")
            name_input = ui.input(label="Name").props('outlined dense').classes("full-width")
            email_input = ui.input(label="Email").props('outlined dense').classes("full-width")
            note_input = ui.input(label="Note").props('outlined dense').classes("full-width")

        # ── RIGHT: actions + log ──────────────────────────────
        with ui.element("div"):

            # Action buttons card
            with ui.element("div").classes("card action-card"):
                ui.label("Actions").classes("card-label")
                ui.button("Action 1", on_click=handle_action_1).classes("btn-action-1")
                ui.button("Action 2 — Clear", on_click=handle_action_2).classes("btn-action-2")

            # Action log card
            with ui.element("div").classes("card"):
                ui.label("Action Log").classes("card-label")
                with ui.element("div").classes("log-scroll") as log_container:
                    ui.label("No entries yet…").classes("log-empty")


ui.run(
    title="NiceGUI App",
    native=True,          # opens a native desktop window (pywebview)
    window_size=(1100, 700),
    reload=False,
)