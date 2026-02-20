# build.spec — PyInstaller spec for NiceGUI desktop app
# Works on both Windows and Ubuntu (built via GitHub Actions CI).

import sys
import os
from pathlib import Path
import nicegui

block_cipher = None

nicegui_path = Path(nicegui.__file__).parent

# Collect all nicegui web assets
datas = [
    (str(nicegui_path / 'elements'),  'nicegui/elements'),
    (str(nicegui_path / 'static'),    'nicegui/static'),
    (str(nicegui_path / 'templates'), 'nicegui/templates'),
]

hidden = [
    'nicegui',
    'nicegui.elements',
    'uvicorn',
    'uvicorn.logging',
    'uvicorn.loops',
    'uvicorn.loops.auto',
    'uvicorn.protocols',
    'uvicorn.protocols.http',
    'uvicorn.protocols.http.auto',
    'uvicorn.protocols.websockets',
    'uvicorn.protocols.websockets.auto',
    'uvicorn.lifespan',
    'uvicorn.lifespan.on',
    'fastapi',
    'webview',
    'engineio',
    'socketio',
    'multiprocessing',
    'multiprocessing.managers',
]

# Platform-specific backend
if sys.platform == 'linux':
    hidden += ['webview.platforms.gtk', 'gi', 'gi.repository.Gtk',
               'gi.repository.WebKit2', 'gi.repository.GLib']
elif sys.platform == 'win32':
    hidden += ['webview.platforms.winforms', 'clr', 'System',
               'System.Windows.Forms']

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=hidden,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='NiceGUIApp',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='NiceGUIApp',
)
