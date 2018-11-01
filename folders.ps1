gci ".\images\" | Where {$_.psIsContainer -eq $true} | ForEach-Object {
    $folder = $_
    Rename-Item ".\images\$($_.Name)" -NewName "train_$( $_.Name )"
    new-item -Name "images\test_$( $_ )" -ItemType directory
}