#!/usr/bin/env python3
"""
Launcher untuk menjalankan entry point dari .so module.
Dibuat otomatis oleh cyencrypt.py.
"""
import importlib
import sys

MODULE_NAME = 'e'


def main():
    try:
        mod = importlib.import_module(MODULE_NAME)
    except Exception as e:
        print(f"[launcher] gagal import {MODULE_NAME}: {e}", file=sys.stderr)
        sys.exit(1)

    if hasattr(mod, "load_settings") and callable(getattr(mod, "load_settings")):
        try:
            mod.load_settings()
        except Exception:
            pass

    if hasattr(mod, "menu") and callable(getattr(mod, "menu")):
        try:
            mod.menu()
        except KeyboardInterrupt:
            print("\nStopped by user")
        except Exception as e:
            print(f"[launcher] error: {e}", file=sys.stderr)
            sys.exit(1)
    elif hasattr(mod, "main") and callable(getattr(mod, "main")):
        try:
            return mod.main()
        except KeyboardInterrupt:
            print("\nStopped by user")
    else:
        print(
            f"[launcher] {MODULE_NAME} tidak punya menu()/main()",
            file=sys.stderr,
        )
        sys.exit(1)


if __name__ == "__main__":
    sys.exit(main() or 0)
