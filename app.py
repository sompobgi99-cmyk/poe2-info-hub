"""PoE 2 Info Hub — Flask Backend v2.1
Features: health check, JSON API, economy tracker, freshness timestamps, in-memory cache
"""
from flask import Flask, render_template, jsonify, request
import markdown
import os, re, json, time
from datetime import datetime, timezone, timedelta
from functools import wraps

app = Flask(__name__)

# === Paths ===
import os as _os
BASE_DIR = _os.path.dirname(_os.path.abspath(__file__))
CONTENT_DIR = _os.path.join(BASE_DIR, "content")
GUIDE_PATH = _os.path.join(CONTENT_DIR, "poe2-guide-thai.md")
NEWS_PATH = _os.path.join(CONTENT_DIR, "poe2-news.md")
PATCH_PATH = _os.path.join(CONTENT_DIR, "poe2-patch-notes.md")
BUFF_PATH = _os.path.join(CONTENT_DIR, "poe2-buff-nerf.md")
META_PATH = _os.path.join(CONTENT_DIR, "poe2-meta-builds.md")
LEAGUE_PATH = _os.path.join(CONTENT_DIR, "poe2-league-mechanics.md")
NEW_ITEMS_PATH = _os.path.join(CONTENT_DIR, "poe2-new-items-0.5.md")
CURRENCY_PATH = _os.path.join(CONTENT_DIR, "poe2-currency-reference.md")
GEM_PATH = _os.path.join(CONTENT_DIR, "poe2-gem-reference.md")

START_TIME = datetime.now(timezone.utc).isoformat()

PAGES = {
    "คู่มือ": ("/guide", GUIDE_PATH),
    "ข่าวสาร": ("/news", NEWS_PATH),
    "Patch Notes": ("/patch-notes", PATCH_PATH),
    "Buff/Nerf": ("/buff-nerf", BUFF_PATH),
    "Meta & Builds": ("/meta", META_PATH),
    "League Mechanics": ("/mechanics", LEAGUE_PATH),
    "ของใหม่ 0.5": ("/new-items", NEW_ITEMS_PATH),
    "Currency": ("/currency", CURRENCY_PATH),
    "Gems": ("/gems", GEM_PATH),
}


# ============================================================
#  In-Memory Cache
# ============================================================

# Cache: {key: {"data": ..., "mtime": float, "hits": int}}
_RENDER_CACHE = {}
_CACHE_HITS = 0
_CACHE_MISSES = 0


def cache_get_or_compute(key, file_path, compute_fn):
    """Get from cache if file hasn't changed, otherwise recompute."""
    global _CACHE_HITS, _CACHE_MISSES
    try:
        current_mtime = os.path.getmtime(file_path)
    except (FileNotFoundError, OSError):
        current_mtime = 0

    entry = _RENDER_CACHE.get(key)
    if entry and entry["mtime"] == current_mtime:
        _CACHE_HITS += 1
        entry["hits"] += 1
        return entry["data"]

    _CACHE_MISSES += 1
    data = compute_fn()
    _RENDER_CACHE[key] = {"data": data, "mtime": current_mtime, "hits": 1}
    return data


def cache_stats():
    """Return cache statistics."""
    return {
        "entries": len(_RENDER_CACHE),
        "hits": _CACHE_HITS,
        "misses": _CACHE_MISSES,
        "hit_ratio": f"{_CACHE_HITS / max(1, _CACHE_HITS + _CACHE_MISSES) * 100:.1f}%",
    }


# ============================================================
#  Helpers
# ============================================================

def md_to_html(path, default="ยังไม่มีข้อมูล"):
    """Render markdown to HTML with in-memory cache."""
    def render():
        try:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            return markdown.markdown(content, extensions=["tables", "fenced_code", "toc"])
        except FileNotFoundError:
            return f"<p class='empty-state'>📭 {default}</p>"

    cache_key = f"html:{path}"
    return cache_get_or_compute(cache_key, path, render)


def read_file_cached(path):
    """Read file contents with in-memory cache."""
    def read():
        with open(path, "r", encoding="utf-8") as f:
            return f.read()

    cache_key = f"raw:{path}"
    return cache_get_or_compute(cache_key, path, read)


def file_mtime(path):
    """Return formatted timestamp of file modification, or None."""
    try:
        ts = os.path.getmtime(path)
        dt = datetime.fromtimestamp(ts, tz=timezone.utc) + timedelta(hours=7)
        return dt.strftime("%d/%m/%Y %H:%M น.")
    except (FileNotFoundError, OSError):
        return None


def file_size(path):
    """Return file size in KB."""
    try:
        return round(os.path.getsize(path) / 1024, 1)
    except (FileNotFoundError, OSError):
        return 0


def strip_markdown(text):
    text = re.sub(r'#+ ', '', text)
    text = re.sub(r'\*\*', '', text)
    text = re.sub(r'\|', ' ', text)
    text = re.sub(r'[\\`*_{}[\\]()>#+\\-!.~]', '', text)
    return ' '.join(text.split())


# ============================================================
#  Pages
# ============================================================

@app.route("/")
def index():
    freshness = {k: file_mtime(v[1]) for k, v in PAGES.items()}
    return render_template("index.html", freshness=freshness)


@app.route("/guide")
def guide():
    html = md_to_html(GUIDE_PATH, "ยังไม่มีไฟล์คู่มือ — รอการสร้างครั้งแรก")
    mtime = file_mtime(GUIDE_PATH)
    return render_template("guide.html", content=html, last_updated=mtime)


@app.route("/news")
def news():
    html = md_to_html(NEWS_PATH, "ยังไม่มีข่าว — cron job จะอัปเดตทุกวัน 09:00 น.")
    mtime = file_mtime(NEWS_PATH)
    return render_template("news.html", content=html, last_updated=mtime)


@app.route("/patch-notes")
def patch_notes():
    html = md_to_html(PATCH_PATH, "ยังไม่มีสรุป Patch Notes")
    mtime = file_mtime(PATCH_PATH)
    return render_template("patch_notes.html", content=html, last_updated=mtime)


@app.route("/buff-nerf")
def buff_nerf():
    html = md_to_html(BUFF_PATH, "ยังไม่มีข้อมูล Buff/Nerf")
    mtime = file_mtime(BUFF_PATH)
    return render_template("buff_nerf.html", content=html, last_updated=mtime)


@app.route("/meta")
def meta():
    html = md_to_html(META_PATH, "ยังไม่มีข้อมูล Meta & Builds")
    mtime = file_mtime(META_PATH)
    return render_template("meta.html", content=html, last_updated=mtime)


@app.route("/mechanics")
def mechanics():
    html = md_to_html(LEAGUE_PATH, "ยังไม่มีข้อมูล League Mechanics")
    mtime = file_mtime(LEAGUE_PATH)
    return render_template("mechanics.html", content=html, last_updated=mtime)


@app.route("/new-items")
def new_items():
    html = md_to_html(NEW_ITEMS_PATH, "ยังไม่มีข้อมูล — รอการ scrape จาก poe2db.tw")
    mtime = file_mtime(NEW_ITEMS_PATH)
    return render_template("new_items.html", content=html, last_updated=mtime)


@app.route("/currency")
def currency():
    html = md_to_html(CURRENCY_PATH, "ยังไม่มีข้อมูล Currency Reference")
    mtime = file_mtime(CURRENCY_PATH)
    return render_template("currency.html", content=html, last_updated=mtime)


@app.route("/gems")
def gems():
    html = md_to_html(GEM_PATH, "ยังไม่มีข้อมูล Gem Reference")
    mtime = file_mtime(GEM_PATH)
    return render_template("gems.html", content=html, last_updated=mtime)


# ============================================================
#  Health & Status
# ============================================================

@app.route("/health")
def health():
    page_status = {}
    for name, (url, path) in PAGES.items():
        exists = os.path.exists(path)
        page_status[name] = {
            "exists": exists,
            "size_kb": file_size(path) if exists else 0,
            "last_updated": file_mtime(path),
        }
    return jsonify({
        "status": "ok",
        "uptime_since": START_TIME,
        "cache": cache_stats(),
        "pages": page_status,
    })


# ============================================================
#  JSON API
# ============================================================

@app.route("/api/page/<name>")
def api_page(name):
    """Return raw markdown + metadata for a page."""
    mapping = {
        "guide": ("คู่มือ", GUIDE_PATH),
        "news": ("ข่าวสาร", NEWS_PATH),
        "patch-notes": ("Patch Notes", PATCH_PATH),
        "buff-nerf": ("Buff/Nerf", BUFF_PATH),
        "meta": ("Meta & Builds", META_PATH),
        "mechanics": ("League Mechanics", LEAGUE_PATH),
    }
    if name not in mapping:
        return jsonify({"error": "not found"}), 404
    label, path = mapping[name]
    try:
        raw = read_file_cached(path)
        html = md_to_html(path)
        return jsonify({
            "name": name,
            "label": label,
            "last_updated": file_mtime(path),
            "size_kb": file_size(path),
            "markdown": raw,
            "html": html,
        })
    except FileNotFoundError:
        return jsonify({"error": "file not found"}), 404


@app.route("/api/pages")
def api_pages_index():
    """List all pages with metadata (no content)."""
    pages = []
    for name, (url, path) in PAGES.items():
        pages.append({
            "name": name,
            "url": url,
            "last_updated": file_mtime(path),
            "size_kb": file_size(path),
        })
    return jsonify(pages)


# ============================================================
#  Search API (cached)
# ============================================================

def _build_search_index():
    """Build full search index (used by cache)."""
    entries = []
    for page_name, (url, path) in PAGES.items():
        try:
            content = read_file_cached(path)
            sections = re.split(r'\n(?=## )', content)
            for section in sections:
                lines = section.strip().split('\n')
                title = lines[0].strip('# ').strip()
                if not title:
                    continue
                body = '\n'.join(lines[1:]) if len(lines) > 1 else ''
                entries.append({
                    "title": title,
                    "page": page_name,
                    "url": url,
                    "content": strip_markdown(body[:400]),
                    "full_section": strip_markdown(section[:800]),
                })
        except FileNotFoundError:
            pass
    return entries


@app.route("/api/search-index")
def search_index():
    """Return section-level search index (cached per-file)."""
    # Use the first page's mtime as cache key proxy — any file change invalidates
    proxy_path = NEWS_PATH  # News changes daily, good proxy
    return jsonify(cache_get_or_compute("search-index", proxy_path, _build_search_index))


# ============================================================
#  Economy (on hold)
# ============================================================

@app.route("/api/economy")
def economy():
    return jsonify({
        "status": "unavailable",
        "message": "poe.ninja API has changed. Economy data will return after PoE 2 league launch (29 May 2026).",
        "currencies": {},
    })


# ============================================================
#  RSS Feed (cached)
# ============================================================

def _build_rss():
    """Build RSS XML (used by cache)."""
    from xml.sax.saxutils import escape
    try:
        content = read_file_cached(NEWS_PATH)
    except FileNotFoundError:
        content = ""

    items_xml = ""
    blocks = re.split(r'\n---\n', content)
    for block in blocks[:20]:
        block = block.strip()
        if not block:
            continue
        date_match = re.search(r'\[(\d{4}-\d{2}-\d{2})\]', block)
        date_str = date_match.group(1) if date_match else "2026-01-01"
        title_match = re.search(r'#### (.+)', block)
        title = title_match.group(1) if title_match else "PoE 2 News"
        desc = escape(strip_markdown(block[:500]))
        title_esc = escape(title)

        items_xml += f"""  <item>
    <title>{title_esc}</title>
    <description>{desc}</description>
    <pubDate>{date_str}T09:00:00+07:00</pubDate>
    <link>https://poe2-info-hub.onrender.com/news</link>
  </item>
"""

    return f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
<channel>
  <title>PoE 2 Info Hub — ข่าวสารภาษาไทย</title>
  <link>https://poe2-info-hub.onrender.com/news</link>
  <description>ศูนย์รวมข่าวสาร Path of Exile 2 ภาษาไทย อัปเดตทุกวัน</description>
  <language>th</language>
{items_xml}
</channel>
</rss>"""


@app.route("/rss.xml")
def rss():
    xml = cache_get_or_compute("rss", NEWS_PATH, _build_rss)
    return xml, 200, {"Content-Type": "application/xml; charset=utf-8"}


# ============================================================
#  Cache Debug (dev only)
# ============================================================

@app.route("/api/cache")
def cache_debug():
    """Show cache contents (for debugging)."""
    entries = {}
    for key, entry in _RENDER_CACHE.items():
        data = entry["data"]
        if isinstance(data, str):
            entries[key] = {
                "mtime": entry["mtime"],
                "hits": entry["hits"],
                "len": len(data),
                "preview": data[:80] + "...",
            }
        elif isinstance(data, list):
            entries[key] = {
                "mtime": entry["mtime"],
                "hits": entry["hits"],
                "count": len(data),
            }
        else:
            entries[key] = {"mtime": entry["mtime"], "hits": entry["hits"]}
    return jsonify({"stats": cache_stats(), "entries": entries})


# ============================================================
#  Main
# ============================================================

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5050, debug=False)
