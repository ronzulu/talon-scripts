$ErrorActionPreference = 'Stop'

cd "D:\github\talon-community-wiki"

Write-Host "1. npm start"
Write-Host "2. npm run build"
Write-Host "3. npm run serve"
Write-Host "4. stop port 3000 processes"
Write-Host "exit"

$selection = Read-Host "Please enter your selection"
$selection


switch ($selection) {
    "1" {
        npm start
    }
    "2" {
        npm run build
    }
    "3" {
        npm run serve
    }
    "4" {
        $process = Get-Process -Id (Get-NetTCPConnection -LocalPort 3000).OwningProcess | Where-Object { $_.Id -ne 0 }
        $process
        $process | Stop-Process
    }
    "exit" {
    }
    default {
        Write-Host "The action is not recognized."
    }
}
