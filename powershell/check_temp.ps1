# List all the computers you want to check C:\temp on.
$computers = "computers"

# Checks c:\temp on the remote system.
Invoke-Command -ComputerName $computers -ScriptBlock {hostname; Get-ChildItem c:\temp}