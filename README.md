# mcp-project

the ultiamte MCP tooling





How to use it (2-minute runbook)

1\) Unzip



Put it wherever you want (repo root):



2\) Put your extracted scripts where the server can find them



Either:



place scripts in ./tools/ next to the project

or



set env var SM0L\_TOOLS\_DIR to wherever you extracted the zip contents:



Windows PowerShell



$env:SM0L\_TOOLS\_DIR = "D:\\path\\to\\extracted\\scripts"





Linux/macOS



export SM0L\_TOOLS\_DIR=/path/to/extracted/scripts



3\) Install base + extras

pip install -e .

pip install -e .\[web,viz]          # example

pip install -e .\[browser]          # if you want browser automation



4\) Run the MCP server

sm0l-tools-mcp



What “install hints” look like in a tool result



If a script fails due to missing deps, you’ll see something like:



"install\_hints": {

  "tool": "sm0l\_bs4\_demo",

  "missing\_module": "bs4",

  "deps\_pypi": \["beautifulsoup4", "requests"],

  "suggested\_extras": \["web"],

  "pip\_commands": \["pip install -e .\[web]"],

  "notes": \["Preferred: install via extras for reproducible capability bundles."]

}





…and if it’s Playwright you’ll also get:



playwright install added automatically, plus a note.





Quick usage reminder

\# point to your extracted scripts root

set SM0L\_TOOLS\_DIR=D:\\path\\to\\extracted\\scripts



\# install base + whichever extras you want

pip install -e .

pip install -e .\[web,viz,browser]



\# run server

sm0l-tools-mcp





Then call:



list\_sm0l\_tools



validate\_environment



any tool like sm0l\_<whatever>



V3: How you’ll use this day-to-day

Once your MCP server is running, you can do:

“What pipelines do you know?”

list_toolchain_recipes()

“Given my goal, what should I run, and am I ready?”

suggest_toolchain("scrape a web page and summarize it")

It will return multiple candidates, each with:

ready: true/false

missing_packages

missing_system

suggested_extras

pip_commands

ordered chain (actual tool steps)

