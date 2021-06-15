import pyttsx3
import SparrowDB
import auto_script
import wikipedia
import subprocess, webbrowser, os, requests, random, sys, platform, pyautogui, psutil, time, datetime
from speech_files import tc
from SparrowDB import get_answer_from_database, insert_ques_and_ans
from pynput.keyboard import Controller as key_controller
from tkinter import filedialog

engine = pyttsx3.init('sapi5')
voice= engine.getProperty('voices')
engine.setProperty('voice', 'voice[0].id')

global path, path2, keyboard

path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\"
path2 = 'C:\\Windows\\System32\\'

keyboard = key_controller()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def takeScreenshot():
    myScreenshot = pyautogui.screenshot()
    file_path = filedialog.asksaveasfilename(defaultextension='.png')
    myScreenshot.save(file_path)

class response:

    def Process_r():
        #while True:
            #speak("Tell me what i can do for you")
            tc.takeCommand()
            try:
                query = tc.query
            except Exception:
                return
            
            answer = get_answer_from_database(query)
            
            if 'search' in query:
                query = query.replace("search", "")

            if 'on flipkart' in query or 'flipkart' in query:
                query = query.replace("on flipkart", "").replace('flipkart', '')
                webbrowser.open_new_tab("https://www.flipkart.com/search?q="+query)
                speak("showing search results")
                response.say = "showing search results"
                return
            elif 'on reddit' in query:
                query = query.replace("on reddit", "")
                webbrowser.open_new_tab("https://www.reddit.com/search/?q="+query)
                speak("showing search results")
                response.say = "showing search results"
                return
            elif 'on github' in query:
                query = query.replace("on github", "")
                webbrowser.open_new_tab("https://github.com/search?q="+query)
                speak("showing search results")
                response.say = "showing search results"
                return
            elif 'location' in query:
                query = query.replace("location", "")
                webbrowser.open_new_tab("https://www.google.com/maps/search/"+query)
                speak("showing search results")
                response.say = "showing search results"
                return
            elif 'on google' in query:
                query = query.replace("on google", "")
                webbrowser.open_new_tab("https://www.google.com/search?q="+query)
                speak("showing search results")
                response.say = "showing search results"
                return
            elif 'on youtube' in query:
                query = query.replace("on youtube", "")
                webbrowser.open_new_tab("https://www.youtube.com/results?search_query="+query)
                speak("showing search results")
                response.say = "showing search results"
                return
            elif 'wikipedia about' in query or 'on wikipedia' in query:
                query = query.replace("wikipedia about", "")
                query = query.replace("on wikipedia", "")
                webbrowser.open_new_tab("https://en.wikipedia.org/wiki/"+query)
                speak("showing search results")
                response.say = "showing search results"
                results = wikipedia.summary(query, sentences=1)
                speak(results)
                return

            elif answer == "shut down":
                ending=["Ok Bye", "Good bye", "i Hope we will meet again"]
                cending=random.choice(ending)
                speak('Sparrow is closing now,' +cending)
                sys.exit()
                    
            elif answer == "stop listening":
                speak('Click on Listen button to activate me again')
                response.say = "Click on Listen button to activate me again"
                return

            elif 'type' in query:
                query = query.replace("type", "")
                for words in query:
                    keyboard.type(words)
                    time.sleep(0.05)
                response.say = "I have written what you told me to"

            elif answer == "open youtube":
                webbrowser.open_new_tab("https://www.youtube.com")
                speak("opening Youtube")
                response.say = "opening Youtube"
                time.sleep(2)

            elif 'play music' in query or 'play songs' in query or 'play song' in query:
                music_dir = 'E:\\Music'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir,songs[0]))
                time.sleep(2)

            elif answer == 'get current time':
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"The time is {strTime}")
                response.say = f"The time is {strTime}"
            
            elif answer == 'open instagram':
                webbrowser.open_new_tab("https://www.instagram.com")
                speak("opening Insta")
                response.say = "opening Instagram"
                time.sleep(2)

            elif answer == 'open facebook':
                webbrowser.open_new_tab("https://www.facebook.com")
                speak("opening Facebook")
                response.say = "opening Facebook"
                time.sleep(2)
            
            elif answer == 'open whatsapp':
                webbrowser.open_new_tab("https://web.whatsapp.com")
                speak("opening whatsapp")
                response.say = "opening whatsapp"
                time.sleep(2)

            elif answer == 'open reddit':
                webbrowser.open_new_tab("https://www.reddit.com")
                speak("opening Reddit")
                response.say = "opening reddit"
                time.sleep(2)

            elif answer == 'about sparrow':
                speak("My name is Sparrow and i am your personal voice assistant.")
                response.say = "My name is Sparrow and i am your personal voice assistant."
                time.sleep(2)

            elif answer == 'flip a coin':
                moves=["head", "tails"]
                cmove=random.choice(moves)
                #print ("It's " + cmove)
                speak("It's " + cmove)
                response.say = "It's " + cmove

            elif answer == 'open calculator':
                subprocess.Popen(path2 +'calc.exe')
                speak("opening calculator")
                response.say = "opening calculator"

            elif answer == 'open notepad':
                subprocess.Popen(path2 +'notepad.exe')
                speak("opening notepad")
                response.say = "opening notepad"

            elif answer == 'open cmd':
                subprocess.Popen([path2 +'cmd.exe'], shell=True)
                speak("opening command window")
                response.say = "opening command window"

            elif answer == 'open control panel':
                subprocess.Popen(path2 +'control.exe')
                speak("opening control panel")
                response.say = "opening control panel"

            elif answer == 'open registry':
                subprocess.Popen(['C:\\Windows\\regedit.exe'], shell=True)
                speak("opening registry editor")
                response.say = "opening registry editor"

            elif answer == 'configure system':
                subprocess.Popen([path2 +'msconfig.exe'], shell=True)
                speak("opening system configuration")
                response.say = "opening System Configuration"

            elif answer == 'open paint':
                subprocess.Popen([path2 +'mspaint.exe'], shell=True)
                speak("opening Paint app")
                response.say = "opening Paint App"

            elif answer == 'open powershell':
                subprocess.Popen(['C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe'], shell=True)
                speak("opening powershell")
                response.say = "opening Windows Powershell"

            elif answer == 'open task manager':
                subprocess.Popen([path2 +'Taskmgr.exe'], shell=True)
                speak("opening Task Manager")
                response.say = "opening Task Manager"
                time.sleep(2)

            elif answer == 'open explorer':
                subprocess.Popen(['C:\\Windows\\explorer.exe'], shell=True)
                speak("opening explorer")
                response.say = "opening Explorer"
                time.sleep(2)
            
            elif answer == 'open MS excel':
                subprocess.Popen([path +'Excel.lnk'], shell=True)
                speak("opening excel")
                response.say = "opening Microsoft Excel"
                time.sleep(2)

            elif answer == 'open MS word':
                subprocess.Popen([path +'Word.lnk'], shell=True)
                speak("opening word")
                response.say = "opening Microsoft Word"
                time.sleep(2)
            
            elif answer == 'open ppt':
                subprocess.Popen([path +'Powerpoint.lnk'], shell=True)
                speak("opening powerpoint")
                response.say = "opening Microsoft powerpoint"
                time.sleep(2)

            elif answer == 'open MS edge':
                subprocess.Popen([path +'Microsoft Edge.lnk'], shell=True)
                speak("opening MS Edge")
                response.say = "opening Microsoft Edge"
                time.sleep(2)

            elif answer == 'open camera':
                subprocess.run('start microsoft.windows.camera:', shell=True)
                speak("opening Camera App")
                response.say = "opening Camera App"

            elif answer == 'print screen':
                takeScreenshot()
                speak("Saving screenshot")
                response.say = "Screenshot saved"
            
            elif answer == 'increase volume':
                auto_script.increase_volume()
                speak("volume increased")
                response.say = "volume increased"
            elif answer == 'decrease volume':
                auto_script.decrease_volume()
                speak("volume decreased")
                response.say = "volume decreased"
            elif answer == 'mute volume':
                pyautogui.press("volumemute")
                speak("volume muted")
                response.say = "you can't hear me now, Can you?"
            elif answer == 'press enter':
                pyautogui.press("enter")
            elif answer == 'switch window':
                auto_script.switch_window()
            elif answer == 'minimise window':
                auto_script.minimize_window()
            elif answer == 'restore down':
                auto_script.restore_down()
            elif answer == 'maximize window':
                auto_script.maximize_window()
            elif answer == 'copy':
                auto_script.copy()
            elif answer == 'cut':
                auto_script.cut()
            elif answer == 'paste':
                auto_script.paste()
            elif answer == 'select all':
                auto_script.select_all()
            elif answer == 'save':
                auto_script.save()
            elif answer == 'save as':
                auto_script.save_as()
            elif answer == 'close current window':
                auto_script.close_current_program()

            elif answer == 'battery percent':
                battery = psutil.sensors_battery()
                battery_percent = str(battery.percent)
                speak("Current battery percentage is " + battery_percent + "percent")
                response.say = "Current battery percentage is " + battery_percent + "percent"

            elif answer == "question":
                webbrowser.open_new_tab("https://www.google.com/search?q="+query)
                speak("showing search results")
                response.say = "opening google to show about \n"+query
                return

            else:
                speak("Can you please tell me what it means?")
                response.say = "Can you please tell me what it means?"
                tc.speak_for_me()
                query2 = tc.query2
                if "it means" in query2:
                    query2 = query2.replace("it means", "")
                    query2 = query2.strip()

                    value = get_answer_from_database(query2)
                    if value == "":
                        speak("Can't help with this query")
                        response.say = "Can't help with this query"
                    else:
                        insert_ques_and_ans(query, value)
                        speak("Thanks, I will remember it for the next time")
                        response.say = "Thanks, I will remember it for the next time"
                
                elif "cancel" in query2 or "no" in query2 or "i don't want to" in query2:
                    speak("Ok, but i won't be able to know what it means")
                    response.say = "Ok, but i won't be able to know what it means"
                
                else:
                    speak("try to say 'it means' before your sentence")
                    response.say = "try to say 'it means' before your sentence"
                    return
