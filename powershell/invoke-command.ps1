# This will prompt the user for input on whatever the variable you define.

[CmdletBinding()]
Param(
	[parameter(Mandatory=$true)] $variable
)

# You can then run commands on a remote computer with.

Invoke-Command -ComputerName $variable -ScriptBlock { enter commands here }