from __future__ import annotations

try:
    import gradio as gr
except ImportError:
    print("Missing dependency: gradio. Install with: pip install gradio")
    raise SystemExit(0)

def greet(name: str):
    return f"hello {name}"

if __name__ == "__main__":
    gr.Interface(greet, "text", "text", title="Gradio demo").launch()
