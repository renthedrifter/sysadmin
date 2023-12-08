$computers = "computers"

write-host "Checking C:\temp directory on all computers." -foregroundcolor Yellow
Invoke-Command -ComputerName $computers -ScriptBlock {hostname; ls c:\temp}