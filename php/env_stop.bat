@echo off

cd /D %~dp0

echo Stopping Nginx ...
cd nginx-1.7.9
nginx.exe -s stop 2>nul
taskkill /F /IM nginx.exe 2>nul
cd ..

echo Stopping PHP FastCGI ...
taskkill /F /IM php-cgi.exe 2>nul
