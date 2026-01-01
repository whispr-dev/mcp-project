from __future__ import annotations
import os, tempfile, textwrap

try:
    from dynaconf import Dynaconf
except ImportError:
    print("Missing dependency: dynaconf. Install with: pip install dynaconf")
    raise SystemExit(0)

if __name__ == "__main__":
    os.environ.setdefault("APP_DEBUG", "true")
    cfg = textwrap.dedent("""
    [default]
    answer = 42

    [production]
    answer = 0
    """)
    with tempfile.TemporaryDirectory() as d:
        path = os.path.join(d, "settings.toml")
        open(path, "w", encoding="utf-8").write(cfg)
        settings = Dynaconf(settings_files=[path], envvar_prefix="APP")
        print("debug:", settings.DEBUG)
        print("answer(default):", settings.ANSWER)
        settings.setenv("production")
        print("answer(prod):", settings.ANSWER)
