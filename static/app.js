// PoE 2 Info Hub — Client-side interactivity

// === SEARCH ===
let searchIndex = [];
let searchLoaded = false;

async function loadSearchIndex() {
    if (searchLoaded) return;
    try {
        const res = await fetch('/api/search-index');
        searchIndex = await res.json();
        searchLoaded = true;
    } catch(e) { console.error('Search index load failed:', e); }
}

function doSearch(q) {
    if (!q || q.length < 2) { hideResults(); return; }
    const term = q.toLowerCase();
    const results = [];
    for (const entry of searchIndex) {
        if (entry.content.toLowerCase().includes(term) || entry.title.toLowerCase().includes(term)) {
            // Find matching snippet
            let idx = entry.content.toLowerCase().indexOf(term);
            if (idx < 0) idx = 0;
            const start = Math.max(0, idx - 60);
            const end = Math.min(entry.content.length, idx + 120);
            const snippet = (start > 0 ? '…' : '') + entry.content.slice(start, end) + (end < entry.content.length ? '…' : '');
            results.push({ title: entry.title, page: entry.page, url: entry.url, snippet });
            if (results.length >= 15) break;
        }
    }
    showResults(results, q);
}

function showResults(results, q) {
    let el = document.getElementById('search-results');
    if (!el) {
        el = document.createElement('div');
        el.id = 'search-results';
        el.className = 'search-dropdown';
        document.getElementById('search-box').parentNode.appendChild(el);
    }
    if (results.length === 0) {
        el.innerHTML = `<div class="search-empty">🔍 ไม่พบ "${q}"</div>`;
    } else {
        el.innerHTML = results.map(r =>
            `<a class="search-item" href="${r.url}">
                <span class="search-page">${r.page}</span>
                <span class="search-title">${r.title}</span>
                <span class="search-snippet">${r.snippet}</span>
            </a>`
        ).join('');
    }
    el.style.display = 'block';
}

function hideResults() {
    const el = document.getElementById('search-results');
    if (el) el.style.display = 'none';
}

document.addEventListener('DOMContentLoaded', () => {
    const searchBox = document.getElementById('search-box');
    if (searchBox) {
        searchBox.addEventListener('focus', loadSearchIndex);
        searchBox.addEventListener('input', () => doSearch(searchBox.value));
        searchBox.addEventListener('keydown', e => {
            if (e.key === 'Escape') { searchBox.value = ''; hideResults(); searchBox.blur(); }
        });
    }
    document.addEventListener('click', e => {
        if (!e.target.closest('#search-box') && !e.target.closest('#search-results')) hideResults();
    });

    // === TOC GENERATION ===
    buildTOC();

    // === BACK TO TOP ===
    const btt = document.getElementById('back-to-top');
    if (btt) {
        window.addEventListener('scroll', () => {
            btt.style.display = window.scrollY > 500 ? 'flex' : 'none';
        });
        btt.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
    }

    // === COLLAPSIBLE SECTIONS ===
    document.querySelectorAll('.markdown-body h2').forEach(h2 => {
        h2.style.cursor = 'pointer';
        h2.addEventListener('click', () => {
            let el = h2.nextElementSibling;
            while (el && el.tagName !== 'H2') {
                const wasHidden = el.style.display === 'none';
                el.style.display = wasHidden ? '' : 'none';
                if (el.tagName.startsWith('H')) break;
                el = el.nextElementSibling;
            }
            h2.classList.toggle('collapsed');
        });
    });
});

// === TOC ===
function buildTOC() {
    const article = document.querySelector('.markdown-body');
    if (!article) return;
    const toc = document.getElementById('toc');
    if (!toc) return;

    const headings = article.querySelectorAll('h2, h3');
    if (headings.length < 3) { toc.style.display = 'none'; return; }

    const items = [];
    headings.forEach((h, i) => {
        const id = h.id || `sec-${i}`;
        if (!h.id) h.id = id;
        items.push({ level: h.tagName, text: h.textContent, id });
    });

    toc.innerHTML = `<div class="toc-title">📑 สารบัญ</div>` +
        items.map(item =>
            `<a class="toc-item toc-${item.level.toLowerCase()}" href="#${item.id}">${item.text}</a>`
        ).join('');
    toc.style.display = 'block';
}
