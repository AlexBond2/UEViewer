@echo off
setlocal EnableDelayedExpansion
set game_path=G:\SteamGames\steamapps\common\Marvel Heroes\UnrealEngine3\MarvelGame\CookedPCConsole\

set log_file=export_log.txt
set file_count=0

echo Export log for UModel processing

for %%f in ("%game_path%*.upk") do (
    set /a file_count+=1
    echo Processing %%~nf
    umodel -export -dds "%%f" -out=UmodelExport >> "%log_file%" 2>&1
    echo Finished processing [!file_count! / 15800]
)

echo All files have been processed.
pause
