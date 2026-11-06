# Point .agents/skills and .claude/skills at the canonical skills/ folders.
# Edit skills/ only. Re-run after adding a skill directory.

$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
$canonical = Join-Path $root "skills"

if (-not (Test-Path $canonical)) {
    throw "Missing $canonical"
}

$linkRoots = @(
    (Join-Path $root ".agents\skills"),
    (Join-Path $root ".claude\skills")
)

foreach ($destRoot in $linkRoots) {
    New-Item -ItemType Directory -Force -Path $destRoot | Out-Null
    Get-ChildItem -Path $canonical -Directory | ForEach-Object {
        $link = Join-Path $destRoot $_.Name
        if (Test-Path $link) {
            $item = Get-Item $link -Force
            $targetOk = $false
            if ($item.Attributes -band [IO.FileAttributes]::ReparsePoint) {
                $existing = $item.Target
                if ($existing -and ($existing | Select-Object -First 1) -eq $_.FullName) {
                    $targetOk = $true
                }
            }
            if ($targetOk) {
                return
            }
            throw "Path exists and is not a junction to $($_.FullName): $link"
        }
        New-Item -ItemType Junction -Path $link -Target $_.FullName | Out-Null
        Write-Output "Linked $link"
    }
}
