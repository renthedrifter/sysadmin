$src = Read-Host -Prompt "something $src"
$dest = Read-Host -Prompt "something $dest"
$copy = Read-Host -Prompt "something $copy"

if($copy -eq 'file') {Invoke-Command -ScriptBlock {Get-ChildItem -Path $src; Write-Host "something" -ForegroundColor Yellow; $file = Read-Host -Prompt $file; robocopy.exe $src $dest $file /v}}
if($copy -eq 'directory') {Invoke-Command -ScriptBlock {robocopy.exe $src \\$dest\\ /copy:dat /s /e /z /v /r:2 /w:0}}