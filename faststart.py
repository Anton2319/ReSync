
#
# -*- coding: utf-8 -*-
#
# Catware Development. 2016-2021
#
# CatOS FastStart Boot
#
import sys, os
import threading
import catenv

def get_base_prefix_compat():
    """Get base/real prefix, or sys.prefix if there is none."""
    return getattr(sys, "base_prefix", None) or getattr(sys, "real_prefix", None) or sys.prefix

def in_virtualenv():
    return get_base_prefix_compat() != sys.prefix


Ff = open("catenv.py", 'r', encoding='UTF-8')
__catenv__ = Ff.read()
exec(__catenv__)
Ff.close()
del Ff
lo("CatENV successfully started", type="Loader")
global threads
global sys_threads

#lo("", type="Loader")

Output(ReadFF("usr/distro.txt"))

#
# Modules
#

lo("Loading modules...", type="Loader")
for x in os.listdir("modules"):
    lo(" >>> Activation of modules set: " + x[:-3] + "... ", type="Loader")
    exec(ReadFF(f"modules/{x}"))
    for y in modules:
        try:
            procmsg("Executing '" + y + "'...")
            exec(y)
            succ()
        except:
            failcomplete()
            Output(" [!] The " + x[:-3] + " modules set is invalid. Log will write into file modulesinstall.txt. Starting of modules setup...")
            for z in install:
                procmsg("Installing " + z)
                if in_virtualenv():
                    procmsg("Running inside virtualenv, performing nonuser install")
                    os.system("\"" + sys.executable + " \"" + " -m pip install " + z + " >> modulesinstall.txt")
                else:
                    os.system("\"" + sys.executable + " \"" + " -m pip install --user " + z + " >> modulesinstall.txt")
                succ()
            try:
                exec(y)
                Output(" >>> Module successfully activated. ")
            except:
                Output(" [!!!] Importing error. ")
    if script != None:
        Output(" >>> Script executing... ")
        try:
            exec(script)
            Output(" >>> Done. ")
        except Exception as e:
            Output(" [!!] Unable to execute script - " + str(e))
    else:
        Output(" >>> Script executing isn't needed. ")

for x in os.listdir("configs/"):
    procmsg("Loading configuration - " + x[:-3])
    exec(str(catenv.ReadFF("configs/" + x)))
    succ()

# запуск локального сервера для ввозможности скачивания медиа
def start_server(port):
    procmsg("Initializing HTTP handler")
    Handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", port), Handler)
    procmsg("Starting server at port "+str(port))
    httpd.serve_forever()
    succ()

if __name__ == "__main__":
    global sys_threads
    sys_threads = list()
    httpServerThread = threading.Thread(target=start_server,  args=(8000, ), daemon=True)
    httpServerThread.start()
    sys_threads.append(httpServerThread)

nickname_symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzÑñ АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя,.-_0123456789"
lo("Executing: getreportban()", type="Loader")
getreportban()
lo("Executing: getban()", type="Loader")
getban()
lo("Executing: getmuted()", type="Loader")
getmuted()
lo("Executing: gettroll()", type="Loader")
gettroll()
dons = convertjson(ReadFF("json/dons.json"))["dons"]

lo("Detecting OS", type="Loader")
if platform.system() == 'Windows':
    osname = 'Microsoft Windows NT'
if platform.system() == 'Linux':
    osname = 'GNU/Linux'
if platform.system() == 'Darwin':
    osname = 'Apple MacOS'
if os.name == 'os2':
    osname = 'OS/2 Warp'
if os.name == 'ce':
    osname = 'Windows CE'
if os.name == 'java':
    osname = 'Java'
lo("Detected OS: " + osname, type="Loader")

procmsg("Preparing to kernel start...")
authors = []
commands = []
handlers = []
ids = []
descs = []
modes = []
depends = []
codes = []
restr = []
succ()

startkernel = True
trys = 1
while startkernel:
    try:
        procmsg("Authorization - attempt no. " + str(trys))
        # vk_session = VkApi(token=token)
        # longpoll = VkBotLongPoll(vk_session, gid)
        # vk = vk_session.get_api()
        # keyboard = VkKeyboard(one_time=False)
        bot = telegram.Bot(token=token)
        procmsg(bot.get_me())
        updater = Updater(token=token, use_context=True)
        dispatcher = updater.dispatcher
        uptime = str(time.ctime())
        uptime_time = time.time()
        succ()
        startkernel = False
    except KeyboardInterrupt:
        failcomplete()
        print("Interrupted by user request")
        sys.exit()
    except Exception as e:
        failcomplete()
        Output("Authorization error - " + str(e))
        trys += 1

writeTo(admins, "admins.txt")
mta("CatABMS is starting.")
#блокировка обработки медиа в многопоточном режиме
global media_safelock
media_safelock = False
#try:
    #mta(f'Запуск CatABMS {botname} {version} на ядре {core}...')
exec(ReadFF("core.py"))

def onMessage(event, context):
    if __name__ == "__main__":
        global threads
        threads = list()
        processServerThread = threading.Thread(target=process, args=(event,context, ), daemon=True)
        processServerThread.start()
        threads.append(processServerThread)

procmsg("core launched, starting polling")
message_handler = MessageHandler(None, onMessage)
dispatcher.add_handler(message_handler)
updater.start_polling()
succ()
#except Exception as e:
        #Output('Kernel panic: ' + str(e))
#except KeyboardInterrupt:
#        session_console = True
#        print('''
#CatShell v0.0.1
#list = list of commands, exit = exit out of there and start catABMS.
#''')
#        while session_console:
#            cmd_ = input(">")
#            wrds = cmd_.split(' ')
#            command = wrds[0]
#            parameters_ = " ".join(wrds[1:])
#            writeTo(parameters_, 'exf/parameters.txt')
#            et = False
#            try:
#                if command == "exit":
#                    session_console = False
#                else:
#                    exec(ReadFF('exf/' + command + '.py'))
#            except Exception as e:
#                if command + '.py' not in os.listdir('exf'):
#                    print('/' + 'exf/' + command + '.py: command not found')
#                else:
#                    print(e)

# authors = []
# commands = []
# ids = []
# descs = []
# modes = []
# depends = []
# codes = []
# restricted = []
