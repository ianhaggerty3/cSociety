gci -Path ".\directory_names\*" | Where {$_.psIsContainer -eq $true} | ForEach-Object {
	$targetFolder = $_
    $d = gci -Path (".\images\test_" + $targetFolder.Name + "\*.jpg") | Where {$_.psIsContainer -eq $false} | resolve-path
    if ($d)  {
        Copy-Item $d -destination (".\images\train_" + $targetFolder.Name + "\")
        Remove-Item $d
    }
    $d = gci -Path (".\images\train_" + $targetFolder.Name + "\*.jpg") | Where {$_.psIsContainer -eq $false} | resolve-path  |  get-random -count 20
    Copy-Item $d -destination (".\images\test_" + $targetFolder.Name + "\")
    Remove-Item $d
}