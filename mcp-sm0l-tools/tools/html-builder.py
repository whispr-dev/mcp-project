from html_fetcher import fetch_subset
from html_template import TEMPLATE
import datetime
import sys

def build_digest_html(source_config, limit=20):
    """
    Builds the complete HTML content for the digest from a list of sources.
    Source config is expected to be a list of dictionaries.
    """
    sections_html = []
    
    for src in source_config:
        try:
            url = src["url"]
            selector = src.get("select", "a")
            
            items = fetch_subset(url, selector, limit=limit)
            
            lis = "".join([f'<li><a href="{href}">{text}</a></li>' for text, href in items])
            sections_html.append(f"<h2>{url}</h2><ul>{lis}</ul>")
            
        except requests.exceptions.RequestException as e:
            print(f"Warning: Failed to fetch {src.get('url')} - {e}", file=sys.stderr)
        except KeyError:
            print(f"Warning: Source configuration is missing 'url' key: {src}", file=sys.stderr)

    html = TEMPLATE.format(
        date=datetime.date.today().isoformat(), 
        sections="\n".join(sections_html)
    )
    return html