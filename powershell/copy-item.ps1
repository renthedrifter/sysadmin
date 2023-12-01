# HAS NOT BEEN TESTED YET!!!!

$item = "path to item"
$computer =  "computer name"
$session = New-PSSession $computer

Copy-Item $item -Destination c:\ -ToSession $session
$session | Remove-PSSession