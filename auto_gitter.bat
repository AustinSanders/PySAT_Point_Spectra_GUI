:top
@echo off
For /f "tokens=2-4 delims=/ " %%a in ('date /t') do (set mydate=%%c-%%a-%%b)
For /f "tokens=1-2 delims=/:" %%a in ('time /t') do (set mytime=%%a%%b)
%USERPROFILE%\AppData\Local\GitHub\PortableGit_d76a6a98c9315931ec4927243517bc09e9b731a0\cmd\git.exe config remote.origin.url git@github.com:tisaconundrum2/PySAT.git
%USERPROFILE%\AppData\Local\GitHub\PortableGit_d76a6a98c9315931ec4927243517bc09e9b731a0\cmd\git.exe pull origin master
%USERPROFILE%\AppData\Local\GitHub\PortableGit_d76a6a98c9315931ec4927243517bc09e9b731a0\cmd\git.exe add -A
%USERPROFILE%\AppData\Local\GitHub\PortableGit_d76a6a98c9315931ec4927243517bc09e9b731a0\cmd\git.exe commit -m "Update: %mydate%_%mytime%"
%USERPROFILE%\AppData\Local\GitHub\PortableGit_d76a6a98c9315931ec4927243517bc09e9b731a0\cmd\git.exe push -u origin master
timeout /t 600
goto :top
