#!/usr/bin/env python3
import base64 as _b
import importlib as _i
import sys as _s

_M = _b.b64decode('cnVu').decode("utf-8")
_F = _b.b64decode('bWFpbixtZW51LG1lbnVrdSxydW4sc3RhcnQ=').decode("utf-8").split(",")
_L = _b.b64decode('bG9hZF9zZXR0aW5ncw==').decode("utf-8")


def _boot():
    try:
        _mod = _i.import_module(_M)
    except Exception:
        _s.exit(1)

    _fn = getattr(_mod, _L, None)
    if callable(_fn):
        try:
            _fn()
        except Exception:
            pass

    for _n in _F:
        _c = getattr(_mod, _n, None)
        if callable(_c):
            try:
                return _c()
            except KeyboardInterrupt:
                return 0
            except SystemExit:
                raise
            except Exception:
                _s.exit(1)

    _s.exit(1)


if __name__ == "__main__":
    try:
        _s.exit(_boot() or 0)
    except KeyboardInterrupt:
        _s.exit(0)
