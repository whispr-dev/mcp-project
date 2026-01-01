# sm0l requirements profiles

Generated: 2026-01-01T07:32:09Z
Tools scanned: 297

## Recommended installs

Start light:

```bash
pip install -r requirements_base.txt
```

Then add what you need, e.g.:

```bash
pip install -r requirements_domain_web.txt
pip install -r requirements_heavy_browser.txt
```

### Notes
- `requirements_full_everything.txt` is intentionally maximal and may be fragile.
- OCR and audio tooling often needs system packages (`tesseract`, `ffmpeg`).
- Browser automation may require extra setup (`playwright install` etc.).
