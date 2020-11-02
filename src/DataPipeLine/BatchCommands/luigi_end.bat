@echo off
FOR /F "tokens=5 delims= " %%I IN (
    'netstat -ano ^| find ":8082"'
) DO (
    taskkill /PID %%I
)
