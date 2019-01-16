import webbrowser
import time

break_count = 0
break_max = 3
print("This program started at "+time.ctime())
while break_count < break_max:
    time.sleep(10)
    webbrowser.open('https://www.youtube.com/watch?v=Aj_qAJMWkt0')
    break_count += 1