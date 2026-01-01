from __future__ import annotations

try:
    from pyecharts.charts import Bar
    from pyecharts import options as opts
except ImportError:
    print("Missing dependency: pyecharts. Install with: pip install pyecharts")
    raise SystemExit(0)

if __name__ == "__main__":
    bar = (
        Bar()
        .add_xaxis(["A","B","C"])
        .add_yaxis("vals", [1,4,9])
        .set_global_opts(title_opts=opts.TitleOpts(title="Pyecharts demo"))
    )
    out = "pyecharts_demo.html"
    bar.render(out)
    print("Wrote", out)
