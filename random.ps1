#cd images
#Get-ChildItem | ForEach-Object {
#	$targetFolder = $_
#	cd $targetFolder
$d = gci ".\images\*.jpg" | Where {$_.psIsContainer -eq $false} | resolve-path
Copy-Item $d -destination .\images\
Remove-Item $d
$d = gci ".\images\*.jpg" | Where {$_.psIsContainer -eq $false} | resolve-path  |  get-random -count 2
Copy-Item $d  -destination .\images\selected
Remove-Item $d