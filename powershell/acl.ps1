# Setting the path to where you want the directory to be created.
$path = "input path"

# Prompts the user for a name of the directory.
$directory = read-host -prompt "What do you want to name the folder? $directory"

# Creates the directory.
New-Item -ItemType Directory -Path $path -Name $directory

# Setting ACL.
$acl = Get-Acl $directory
$rule = New-Object System.Security.AccessControl.FileSystemAccessRule("<domain>.<user>", "FullControl", "Allow")
$acl.SetAccessRule($rule)
$acl | Set-Acl $directory