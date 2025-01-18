@echo off
call venv\scripts\activate
pytest -s -v -m "sanity" --html=.\Reports\report.html Test_cases --browser chrome               
rem pytest -s -v -m "reression" --html=.\Reports\report.html Test_cases --browser chrome               
rem pytest -s -v -m "sanity" or "regression" --html=.\Reports\report.html Test_cases --browser chrome               

pause