$all = "list", "of", "computers"

write-host "something" -foregroundcolor Yellow
$computername = read-host -prompt "Updateing GPO on $computername"
if ($computername -eq 'all'){
invoke-command -computername $all -scriptblock {hostname; gpupdate /force}
}
else {
invoke-command -computername $computername -scriptblock {hostname; gpupdate /force}
}