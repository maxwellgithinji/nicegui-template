# Changelog

All notable changes to this project will be documented in this file.

## [v1.0.3] - 2026-02-20

### Fixed
- CI workflow now correctly triggers on version tag pushes (`git tag vX.Y.Z`)
- Ubuntu build uses `--system-site-packages` venv to access system `python3-gi` (PyGObject)
- Pinned Ubuntu runner to `ubuntu-22.04` to ensure `libwebkit2gtk-4.0-dev` availability

## [v1.0.2] - 2026-02-20

### Fixed
- PyInstaller spec and build commands now use absolute `$GITHUB_WORKSPACE` paths to resolve "spec file not found" error on Windows runner

## [v1.0.1] - 2026-02-20

### Fixed
- Added `tags: ["v*"]` trigger to GitHub Actions workflow so release job fires on version tag pushes
- Replaced `ubuntu-latest` (Ubuntu 24.04) with `ubuntu-22.04` — Ubuntu 24 dropped `libwebkit2gtk-4.0-dev`
- Removed `pip install PyGObject` step (fails without `girepository-2.0` headers); use system `python3-gi` via apt instead

## [v1.0.0] - 2026-02-20

### Added
- Initial release of NiceGUI desktop application
- Minimalist UI layout: Form panel (left) with Name, Email, Note inputs
- Actions panel (right) with Action 1 (log form values) and Action 2 (clear form)
- Scrollable Action Log panel with timestamps
- Native desktop window via `pywebview` (`native=True`) — no browser required
- GitHub Actions CI/CD pipeline building standalone executables for Ubuntu and Windows in parallel
- PyInstaller `build.spec` with platform-aware hidden imports (GTK on Linux, WebView2/WinForms on Windows)
- `setup.sh` helper for Ubuntu (deps / run / build)
- `setup.ps1` helper for Windows (run / build)
- Automatic GitHub Release with zipped artifacts on version tag push
