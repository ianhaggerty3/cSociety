$d = gci "C:\Users\themi\PycharmProjects\cSociety_project\random_tests\selected\*.txt" | Where {$_.psIsContainer -eq $false} | resolve-path
Copy-Item $d -destination C:\Users\themi\PycharmProjects\cSociety_project\random_tests
Remove-Item $d
$d = gci "C:\Users\themi\PycharmProjects\cSociety_project\random_tests\*.txt" | Where {$_.psIsContainer -eq $false} | resolve-path  |  get-random -count 2
Copy-Item $d  -destination C:\Users\themi\PycharmProjects\cSociety_project\random_tests\selected
Remove-Item $d