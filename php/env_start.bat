@echo off

cd /D %~dp0

;;;;;;;;;;;;;;;;;

call env_stop.bat
ping 127.0.0.1 -n 2 >nul

;;;;;;;;;;;;;;;;;

echo Starting PHP FastCGI ...
cd php-5.5.6-nts-Win32-VC11-x64
..\RunHiddenConsole php-cgi.exe -b 127.0.0.1:9000 -c php.ini

echo Starting Nginx ...
cd ../nginx-1.7.9
..\RunHiddenConsole nginx.exe

cd \sites\www.eyebuydirect.com\static





