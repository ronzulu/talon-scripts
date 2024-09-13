$global:baseUrl = "https://talonvoice.com/"
$global:hrefList = @()
$global:infoList = @()
$global:doNotFollowList = @("www.youtube.com", "www.patreon.com", "twitter.com", "talonvoice.com/dl/latest", 
    "slack.com", "itunes.apple.com", "slackhq.com", "slackatwork.com", "slack-status.com", "slack.help",  
    "snapcraft.io", "play.google.com"
    )

 Function NormaliseHref($href) {
    $result = $null
    If ($null -ne $href) {
        if ($href.StartsWith("http")) {
            $result = $href
        } elseif ($href.StartsWith("/")) {
            $result = "$baseUrl$href"
        }
    }
    return $result
 }

 Function ShouldFollowLink($link) {
    If ($link -eq "$") {
        return $false 
    }
    foreach ($item in $global:doNotFollowList) {
        If ($link.Contains($item)) {
            return $false
        }
    }
    
    return $link.Contains($global:baseUrl)
}


 Function AddLinks($parentUrl, $url, $maxDepth) {
    Write-Output "************** $url"
    $domain = ([System.Uri]$url).Host
    If (ShouldFollowLink($url)) {
        try {
            If ($maxDepth -gt 0) {
                $pageLinks = @((Invoke-WebRequest $url).Links.href | 
                    ForEach-Object -Process {NormaliseHref($_)} | 
                    Where-Object {$_ -ne $null} )

                $global:infoList += "$parentUrl`t$url`t$domain"
                foreach ($link in $pageLinks) {
                    If ($global:hrefList -notcontains $link) {
                        $global:hrefList += $link
                        $newLinks += $link
                        AddLinks $url $link ($maxDepth - 1)
                    }
                }
            } Else {
                $global:infoList += "$parentUrl`t$url`t$domain`tMaxDepth"
            }
            If ($maxDepth -gt 0) {
                foreach ($link in $filteredNewLinks) {
                }
            }
            
        }
        catch {
            $global:infoList += "$parentUrl`t$url`t$domain`t$($PSItem.Exception.Message)"
        }
    } Else {
        $global:infoList += "$parentUrl`t$url`t$domain`tIgnore"
    }

 }

AddLinks "" $baseUrl 3
$global:infoList | Set-Clipboard