echo off
cls

cd "G:\CondaEnvironment\SeatChangerBuilder\Scripts\"
.\pyinstaller.exe -F -w --upx-dir "G:\upx" --clean "G:\Users\wuboy\PycharmProjects\SeatChanger\SeatChanger.py"
move "G:\CondaEnvironment\SeatChangerBuilder\Scripts\dist\SeatChanger.exe" "G:\Users\wuboy\PycharmProjects\SeatChangerReleases\SeatChanger_v1.0.4_x86-64_win10_win11.exe"

cd "G:\CondaEnvironment\SeatChangerBuilder_Win32\Scripts"
.\pyinstaller.exe -F -w --upx-dir "G:\upx" --clean "G:\Users\wuboy\PycharmProjects\SeatChanger\SeatChanger.py"
move "G:\CondaEnvironment\SeatChangerBuilder_Win32\Scripts\dist\SeatChanger.exe" "G:\Users\wuboy\PycharmProjects\SeatChangerReleases\SeatChanger_v1.0.4_x86-64_win7.exe"

cd "G:\Users\wuboy\PycharmProjects\SeatChangerReleases"
G:\Users\wuboy\PycharmProjects\SeatChanger\.venv\Scripts\pyi-set_version.exe "G:\Users\wuboy\PycharmProjects\SeatChanger\file_version_info.txt" .\SeatChanger_v1.0.4_x86-64_win10_win11.exe
G:\Users\wuboy\PycharmProjects\SeatChanger\.venv\Scripts\pyi-set_version.exe "G:\Users\wuboy\PycharmProjects\SeatChanger\file_version_info.txt" .\SeatChanger_v1.0.4_x86-64_win7.exe

pause