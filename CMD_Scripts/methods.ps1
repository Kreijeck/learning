# press Enter to continue


function press-Enter {
   (Read-Host 'Press Enter to continue…')
}

# GoTo Homedirectory
function Get-Script-DIR {
    #$ScriptDir =  Split-Path -Parent $PSCommandPath
    #return $ScriptDir
    return $PSScriptRoot
    
}

function Get-WhatEver {
    Write-Output "BlA"
    return $PSCommandPath
}

function return-call {
   $my_para = 5

   return $my_para
}

$num = return-call

Write-Host "($num + 4)"
