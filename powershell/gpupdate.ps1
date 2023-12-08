# List all computers, need to put each computer in its own quotes.
$all = "list", "of", "computers"

write-host "Updates GPO on the specified computers" -foregroundcolor Yellow
$computername = read-host -prompt "Updating GPO on $computername type all to update all computers"
if ($computername -eq 'all'){
invoke-command -computername $all -scriptblock {hostname; gpupdate /force}
}
else {
invoke-command -computername $computername -scriptblock {hostname; gpupdate /force}
}