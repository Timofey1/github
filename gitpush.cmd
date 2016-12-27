git add .
set /p text=text: 
git commit -am "%text%"
git push origin master
pause
