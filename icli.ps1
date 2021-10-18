$job = Start-Job -ScriptBlock {Set-Location $using:PWD; python fykernel.py}
Receive-Job -Job $job
