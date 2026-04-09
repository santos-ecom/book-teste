$snippet = @"
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
fbq('init', '1453980406182561');
fbq('track', 'PageView');
</script>
<noscript><img height="1" width="1" style="display:none"
src="https://www.facebook.com/tr?id=1453980406182561&ev=PageView&noscript=1"
/></noscript>
<!-- End Meta Pixel Code -->


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
fbq('init', '1477769170639862');
fbq('track', 'PageView');
</script>
<noscript><img height="1" width="1" style="display:none"
src="https://www.facebook.com/tr?id=1477769170639862&ev=PageView&noscript=1"
/></noscript>
<!-- End Meta Pixel Code -->
"@

$files = Get-ChildItem -Path "c:\Users\Usuario\Downloads\book-teste-main\book-teste-main" -Filter "*.html" -Recurse

$utf8NoBom = New-Object System.Text.UTF8Encoding($false)
$count = 0

foreach ($file in $files) {
    if ($file.Extension -eq ".html") {
        $content = [System.IO.File]::ReadAllText($file.FullName, $utf8NoBom)
        
        if ($content -match "(?i)</head>" -and $content -notmatch "1453980406182561") {
            $content = [regex]::Replace($content, "(?i)</head>", "`n$snippet`n</head>")
            [System.IO.File]::WriteAllText($file.FullName, $content, $utf8NoBom)
            Write-Host "Updated $($file.FullName)"
            $count++
        }
    }
}
Write-Host "Total files updated: $count"