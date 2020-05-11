import time 
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Dear user, it's the time to drink water :)",
            message = "An adequate daily fluid intake is required, 15.5 cups (3.7 ltrs) for men and 11.5 cups (2.7 ltrs) for women.",
            app_icon = 'C:\\Users\\uday_\\Downloads\\Google-Noto-Emoji-Food-Drink-32431-glass-of-milk.ico',
            timeout = 7

        )
        time.sleep(15)

# To run the script as background process 
#Type pythonw <file_name.py> p.s. You can also use 'pythonw.exe' instead of 'pythonw'
