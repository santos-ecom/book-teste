#!/usr/bin/env python3
import glob

PIXELS_CODE = """<script
  src="https://cdn.utmify.com.br/scripts/utms/latest.js"
  data-utmify-prevent-subids
  async
  defer
></script>

<script>
  window.pixelId = "69de0001dccf24bc1b253a01";
  var a = document.createElement("script");
  a.setAttribute("async", "");
  a.setAttribute("defer", "");
  a.setAttribute("src", "https://cdn.utmify.com.br/scripts/pixel/pixel.js");
  document.head.appendChild(a);
</script>

<script>
  window.pixelId = "69ddffb8374ebb0465b86d05";
  var a = document.createElement("script");
  a.setAttribute("async", "");
  a.setAttribute("defer", "");
  a.setAttribute("src", "https://cdn.utmify.com.br/scripts/pixel/pixel.js");
  document.head.appendChild(a);
</script>

<script>
  window.pixelId = "69d7bc797ef80f6cd75c6808";
  var a = document.createElement("script");
  a.setAttribute("async", "");
  a.setAttribute("defer", "");
  a.setAttribute("src", "https://cdn.utmify.com.br/scripts/pixel/pixel.js");
  document.head.appendChild(a);
</script>

<!-- Meta Pixel Code -->
<script>
!function(f,b,e,v,n,t,s)
{if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};
if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];
s.parentNode.insertBefore(t,s)}(window, document,'script',
'https://connect.facebook.net/en_US/fbevents.js');

// PIXELS
fbq('init', '1453980406182561');
fbq('init', '1477769170639862');
fbq('init', '2327194734441309');

// EVENTO
fbq('track', 'PageView');
</script>

<noscript>
<img height="1" width="1" style="display:none"
src="https://www.facebook.com/tr?id=1453980406182561&ev=PageView&noscript=1"/>
<img height="1" width="1" style="display:none"
src="https://www.facebook.com/tr?id=1477769170639862&ev=PageView&noscript=1"/>
<img height="1" width="1" style="display:none"
src="https://www.facebook.com/tr?id=2327194734441309&ev=PageView&noscript=1"/>
</noscript>
<!-- End Meta Pixel Code -->
"""

html_files = list(set(
    glob.glob('/Users/macbook/.gemini/antigravity/scratch/book-teste/**/*.html', recursive=True) +
    glob.glob('/Users/macbook/.gemini/antigravity/scratch/book-teste/*.html')
))

changed = 0
skipped = 0

for filepath in sorted(html_files):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    if '</head>' in content:
        new_content = content.replace('</head>', PIXELS_CODE + '\n</head>', 1)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"✅ Inserido: {filepath.replace('/Users/macbook/.gemini/antigravity/scratch/book-teste/', '')}")
        changed += 1
    else:
        print(f"⚠️  Sem </head>: {filepath.replace('/Users/macbook/.gemini/antigravity/scratch/book-teste/', '')}")
        skipped += 1

print(f"\n{'='*50}")
print(f"✅ Arquivos modificados: {changed}")
print(f"⚠️  Pulados (sem </head>): {skipped}")
print(f"📁 Total processado: {changed + skipped}")
