cd images
Get-ChildItem | ForEach-Object {
	$targetFolder = $_
	cd $targetFolder
	$i = 1
	Get-ChildItem *.jpg | %{Rename-Item $_ -NewName ($targetFolder.Name + "_{0:D2}.jpg" -f $i++)}
	cd ..
	}
cd ..