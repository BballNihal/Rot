import subprocess
import keyboard  
import threading

w_path = './w.ahk'
a_path = './a.ahk'
s_path = './s.ahk'
d_path = './d.ahk'

# track the slow script's state
slow_script_running = False
slow_process = None  # Initialize slow_process

# hotkey to toggle the slow script
toggle_hotkey = 'shift + `'

def set_slow_state(value):
    global slow_script_running
    slow_script_running = value

def start_slow_thread():
    slow_thread = threading.Thread(target=toggle_slow_script)
    slow_thread.daemon = True
    slow_thread.start()
# Function to toggle the slow script
def toggle_slow_script():
    global slow_script_running, slow_process1, slow_process2, slow_process3, slow_process4  
    
    if slow_script_running == True:
        slow_script_running = False

    else:
        # Start the AHK script
        slow_process1 = subprocess.Popen(['AutoHotkey.exe', w_path])
        slow_process2 = subprocess.Popen(['AutoHotkey.exe', a_path])
        slow_process3 = subprocess.Popen(['AutoHotkey.exe', s_path])
        slow_process4 = subprocess.Popen(['AutoHotkey.exe', d_path])
        slow_script_running = True

# Register the hotkey to toggle the AHK script
keyboard.add_hotkey(toggle_hotkey, toggle_slow_script)


# Keep the script running

if __name__ == "__main__":
    start_slow_thread() 
