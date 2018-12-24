@ECHO OFF

REM Configure your favourite diff program here.
SET DIFF="C:\Program Files\SourceGear\Common\DiffMerge\sgdm.exe"

REM specified command: base theirs mine merged wcfile
SET BASE=%1
SET THEIRS=%2
SET MINE=%3
SET MERGED=%4

REM Call the diff command (change the following line to make sense for
REM your diff program).
%DIFF% -m -t1="Theirs" -t2="Base" -t3="Local" -r="%MERGED%" "%MINE%" "%BASE%" "%THEIRS%"

REM Return an errorcode of 0 if no differences were detected, 1 if some were.
REM Any other errorcode will be treated as fatal.