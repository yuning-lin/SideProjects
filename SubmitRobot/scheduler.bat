cd C:\Users\user_name\eclipse-workspace\robot
echo %CD% >> .\env_robot\Lib\site-packages\a.pth
call env_robot\Scripts\activate
python main.py
