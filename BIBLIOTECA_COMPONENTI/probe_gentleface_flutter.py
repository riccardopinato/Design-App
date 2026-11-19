#!/usr/bin/env python3
"""Read-only public MIT source probe. Never archives a pseudo-conversion."""
from urllib.request import urlopen, Request
from html.parser import HTMLParser
import re

class CodeBlocks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.depth = 0
        self.code = ""
        self.blocks = []
    def handle_starttag(self, tag, attrs):
        if tag in ("code", "pre"): self.depth += 1
    def handle_endtag(self, tag):
        if tag in ("code", "pre"):
            self.depth = max(0, self.depth-1)
            if self.depth == 0 and self.code:
                self.blocks.append(self.code)
                self.code = ""
    def handle_data(self, txt):
        if self.depth > 0: self.code += txt

for slug in ("bell-ring","pause","battery-charging"):
    for ext in (".md",""):
        url=f"https://gentleface.com/icons/{slug}{ext}"
        try:
            with urlopen(Request(url,headers={"User-Agent":"AppFactory-OSS-Research/1.0"}),timeout=15) as r:
                raw=r.read().decode("utf-8")
                content_type=r.headers.get("content-type")
        except Exception as exc:
            print("FAIL",url,str(exc)[:160])
            continue
        print("SOURCE",url,"bytes",len(raw),"ctype",content_type)
        blocks=re.findall(r"```(?:dart|flutter)[^\n]*\n([\s\S]*?)```",raw,re.I)
        print("MARKDOWN_DART",len(blocks),[len(b) for b in blocks[:6]])
        if blocks:print("DART_START",repr(blocks[0][:250]))
        parser=CodeBlocks();parser.feed(raw)
        candidates=[b for b in parser.blocks if "CustomPainter" in b and "StatelessWidget" in b]
        print("PRE_DART",len(candidates),[len(b) for b in candidates[:5]])
        if candidates:print("PRE_START",repr(candidates[0][:250]))
        for token in ("class BellRingIcon","class PauseIcon","CustomPainter","## Flutter","Flutter: see"):
            pos=raw.find(token)
            if pos>=0:print("TOKEN",token,pos,repr(raw[pos:pos+150]))
