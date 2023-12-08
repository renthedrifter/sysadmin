# Start putting items in c:\temp then possibly have a new script to check for items in c:\temp.

$item = "path to item"
$computer =  "computer name"
$session = New-PSSession $computer

Copy-Item $item -Destination c:\temp -ToSession $session
$session | Remove-PSSession