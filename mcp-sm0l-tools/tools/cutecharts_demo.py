from __future__ import annotations

try:
    from cutecharts.charts import Line
except ImportError:
    print("Missing dependency: cutecharts. Install with: pip install cutecharts")
    raise SystemExit(0)

if __name__ == "__main__":
    chart = Line("CuteCharts demo")
    chart.set_options(labels=["A","B","C"], x_label="x", y_label="y")
    chart.add_series("s1", [1,4,9])
    print(chart.render_notebook())
