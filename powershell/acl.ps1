# The current version of this script doesn't propogate the permissions for the user in the security tab.
# But once you're in the security tab you can go to Advanced and the permissions will be there.
# To Do, use the "propogateflag" to have the permissions displayed on the security tab.

# Setting the path to where you want the directory to be created.
$path = "input path"

# Prompts the user for a name of the directory.
$directory = read-host -prompt "What do you want to name the folder? $directory"

# Creates the directory.
New-Item -ItemType Directory -Path $path -Name $directory
Get-ChildItem -Path $path (Join-Path -Path $path -ChildPath subfolder1) -ItemType Directory | Out-Null
Get-ChildItem -Path $path (Join-Path -Path $path -ChildPath subfolder2) -ItemType Directory | Out-Null

# Setting ACL properties.
$newacl = Get-Acl -Path $directory
$identity = "domain\user"
$filesystemrights = "FullControl"
$type = "Allow"

# Creating the new rule.
$filesystemaccessruleargumentList = $identity, $filesystemrights, $type
$filesystemaccessrule = New-Object -TypeName System.Security.AccessControl.FileSystemAccessRule -ArgumentList $filesystemaccessruleargumentList

# Apply new rule.
$newacl.SetAccessRule($filesystemaccessrule)
Set-Acl -Path $directory -AclObject $newacl