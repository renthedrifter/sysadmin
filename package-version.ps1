# List machines
$machines = "computer1", "computer2"

# Run the command
Invoke-command -computername $machines -scriptblock { get-apppackage -name "<name of the package>" | Select-Object PackageFamilyName, Version }

# grep equivalent is select-string '<string>'