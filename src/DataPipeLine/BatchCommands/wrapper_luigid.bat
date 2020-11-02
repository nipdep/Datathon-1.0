@echo off
FOR /F "tokens=5 delims= " %%I IN (
    'netstat -ano ^| find ":8082"'
) DO (
    set pid= %%I
)

::echo %pid%
if "%pid%"=="" (
    echo null
    @call F:\Deeplearning\Datathon-1.0\src\DataPipeLine\BatchCommands\luigi_pure.bat
)


