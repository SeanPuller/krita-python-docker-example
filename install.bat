@echo off
::Set Folders
set SOURCE_FOLDER=docker_example
set SOURCE_FILE=docker_example.desktop
set DESTINATION=%APPDATA%\krita\pykrita
set DESTINATIONFOLDER=%APPDATA%\krita\pykrita\docker_Example

::Remove folder and files if they exist already
if exist del /q "%APPDATA%\Krita\Pykrita\docker_example.desktop"
if exist rd /s /q "%APPDATA%\Krita\Pykrita\docker_example"

::Create docker_example folder
if not exist "%APPDATA%\Krita\Pykrita\docker_example" mkdir "%APPDATA%\Krita\Pykrita\docker_Example"

::Add files
xcopy /s /y %SOURCE_FOLDER% %DESTINATIONFOLDER%
copy /y "%SOURCE_FILE%" %DESTINATION%

::cmd /c "C:\Program Files\Krita (x64)\bin\krita.exe"