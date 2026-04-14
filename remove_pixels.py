#!/usr/bin/env python3
import glob
import re

def clean_html(content):
    original = content

    # ── 1. Meta Pixel blocks: <!-- Meta Pixel Code --> ... <!-- End Meta Pixel Code -->
    # Removes everything between those exact comment markers (inclusive)
    content = re.sub(
        r'<!-- Meta Pixel Code -->.*?<!-- End Meta Pixel Code -->',
        '',
        content,
        flags=re.DOTALL | re.IGNORECASE
    )

    # ── 2. Utmify pixelId blocks:
    # <script>
    #     window.pixelId = "...";
    #     ...
    #     document.head.appendChild(a);
    # </script>
    # We look ONLY within a single <script>...</script> that contains pixelId
    content = re.sub(
        r'<script>\s*window\.pixelId\s*=\s*["\'][^"\']*["\'].*?</script>',
        '',
        content,
        flags=re.DOTALL | re.IGNORECASE
    )

    # ── 3. Utmify utms/latest.js single-line script tag
    content = re.sub(
        r'<script\s[^>]*cdn\.utmify\.com\.br/scripts/utms/latest\.js[^>]*>\s*</script>',
        '',
        content,
        flags=re.DOTALL | re.IGNORECASE
    )

    # ── 4. Clean up extra blank lines (max 2 consecutive)
    content = re.sub(r'\n{3,}', '\n\n', content)

    return content, content != original

# Find all HTML files
html_files = list(set(
    glob.glob('/Users/macbook/.gemini/antigravity/scratch/book-teste/**/*.html', recursive=True) +
    glob.glob('/Users/macbook/.gemini/antigravity/scratch/book-teste/*.html')
))

changed = 0
unchanged = 0

for filepath in sorted(html_files):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    new_content, was_changed = clean_html(content)

    if was_changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"✅ Limpo: {filepath.replace('/Users/macbook/.gemini/antigravity/scratch/book-teste/', '')}")
        changed += 1
    else:
        print(f"⏭️  Sem pixels: {filepath.replace('/Users/macbook/.gemini/antigravity/scratch/book-teste/', '')}")
        unchanged += 1

print(f"\n{'='*50}")
print(f"✅ Arquivos modificados: {changed}")
print(f"⏭️  Arquivos sem alteração: {unchanged}")
print(f"📁 Total processado: {changed + unchanged}")
