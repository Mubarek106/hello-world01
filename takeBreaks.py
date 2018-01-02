# The program runs every thirty minutes
import time
import webbrowser

total_breaks = 3
break_count = 0

print("This program started on" + time.ctime())
while(break_count < total_breaks):
    time.sleep(2*60*30) 
    webbrowser.open("https://www.youtube.com/watch?v=5VQi8kbtiLU")
    break_count = break_count + 1  #break_count += 1
