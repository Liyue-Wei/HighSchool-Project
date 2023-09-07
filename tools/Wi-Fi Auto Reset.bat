chcp 65001
@echo off
title Wi-Fi Auto Reset
echo 正在重新啟動Wi-Fi
netsh interface set interface "Wi-Fi" disable
echo Wi-Fi已關閉
netsh interface set interface "Wi-Fi" enable
echo Wi-Fi已重新開啟
pause