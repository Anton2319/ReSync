import os
import this
import token

from requests import get
from telegram.ext import Updater, MessageHandler

print("Kernel running!")

Output("CatABMS Kernel version " + core + " startup...")
lastid = None
# lo("Loading library: detectfull", type="Kernel Loader")
# exec(ReadFF("lib/detectfull.py"))
# #exec(ReadFF("lib/surrogate-manager.py"))
# lo("Loading library: CUMv2", type="Kernel Loader")
# exec(ReadFF("lib/CUMv2.py"))
# lo("Loading library: generrorcode", type="Kernel Loader")
# exec(ReadFF('lib/generrorcode.py'))

lo("Starting of legacy logger...", type="Kernel Loader")
system_errors = ""
service_errors = []
corerc_errors = []
execution_errors = []
hdl_ids = []
systemcare = 0
careless = 0

COMMANDSDIR = "commands/"
lo("COMMANDSDIR is " + COMMANDSDIR, type="Kernel Loader")
VCCOMMANDSDIR = "voice/"
lo("VCCOMMANDSDIR is " + VCCOMMANDSDIR, type="Kernel Loader")
HANDLERSDIR = "handlers/"
lo("HANDLERSDIR is " + HANDLERSDIR, type="Kernel Loader")

peers_list = ReadFF("chats/peers.txt")

lo("Loading commands...", type="Kernel Loader")

for x in os.listdir(COMMANDSDIR):
    try:
        procmsg("Loading: " + x)
        cmdjs = convertjson(ReadFF(f"{COMMANDSDIR}{x}/{x}.json"))
        if not cmdjs["disabled"]:
            authors.append(cmdjs["author"])
            modes.append(cmdjs["mode"])
            ids.append(cmdjs["identificator"])
            commands.append(cmdjs["command_ru"])
            descs.append(cmdjs["description"])
            succ()
            systemcare += 1
        else:
            failcomplete()
            Output(f"Warning: command {cmdjs['command_ru']} is disabled")

    except Exception as e:
        failcomplete()
        Output(e)
        system_errors += "Unable to load command: " + str(e)
        lo("Unable to load command: " + str(e), type="Kernel Loader - ERROR")
        systemcare += 1
        careless += 1
lo("Loading handlers...", type="Kernel Loader")

for x in os.listdir(HANDLERSDIR):
    try:
        procmsg("Loading: " + x)
        cmdjs = convertjson(ReadFF(f"{HANDLERSDIR}{x}/{x}.json"))
        if not cmdjs["disabled"]:
            authors.append(cmdjs["author"])
            modes.append(cmdjs["mode"])
            handlers.append(cmdjs["identificator"])
            hdl_ids.append(cmdjs["identificator"])
            descs.append(cmdjs["description"])
            succ()
            systemcare += 1
        else:
            failcomplete()
            Output(f"Warning: handler {cmdjs['identificator']} is disabled")

    except Exception as e:
        failcomplete()
        Output(e)
        system_errors += "Unable to load command: " + str(e)
        lo("Unable to load command: " + str(e), type="Kernel Loader - ERROR")
        systemcare += 1
        careless += 1

for x in os.listdir(VCCOMMANDSDIR):
    try:
        procmsg("Loading Voice Command: " + x)
        cmdjs = convertjson(ReadFF(f"{VCCOMMANDSDIR}{x}/{x}.json"))
        if not cmdjs["disabled"]:
            vc_authors.append(cmdjs["author"])
            vc_modes.append(cmdjs["mode"])
            vc_ids.append(cmdjs["identificator"])
            vc_commands.append(cmdjs["command_ru"])
            vc_descs.append(cmdjs["description"])
            succ()
            systemcare += 1
        else:
            failcomplete()
            Output(f"Warning: Voice Command - {cmdjs['command_ru']} is disabled.")

    except Exception as e:
        failcomplete()
        Output(e)
        system_errors += "Unable to load voice command: " + str(e)
        lo("Unable to load VCCommand: " + str(e), type="Kernel Loader")
        systemcare += 1
        careless += 1

rcs = []
for x in os.listdir("corerc"):
    try:
        procmsg("CoreRC Module loading: " + x[:-3])
        rcs.append(ReadFF('corerc/' + x))
        succ()
    except Exception as e:
        failcomplete()
        careless += 1
    systemcare += 1

endl = "\n"
services_errors = []

Output("Catware Autostart is starting up...")
for x in os.listdir('services'):
    procmsg("Loading service - " + x[:-3])
    try:
        exec(ReadFF("services/" + x))
        succ()
        systemcare += 1
    except Exception as e:
        systemcare += 1
        careless += 1
        failcomplete()
        system_errors += "Сервис: " + x + ", ошибка: " + str(e) + "\n"
        elo("Service: " + x + ', error: ' + str(e))

__conversations__ = []

Output('CatABMS Kernel loading is done.')

writeTo(time.time(), "start-time.txt")



def Safeexec(event, script, locals_dict):
    global sendvideo
    global message
    def sendvideo(attachment, caption):
        bot.send_video(event.effective_chat.id, video=attachment, caption=caption, supports_streaming=True, timeout=2100)

    def message(text="", attachment="", keyboard="", intent="default", disable_mentions=1, dont_parse=1, reply=True, markdown=False):
        if attachment is None or attachment is "":
            print("sending message")
            if markdown:
                print("markdown is true")
                bot.send_message(event.effective_chat.id, text, parse_mode="Markdown")
            else:
                bot.send_message(event.effective_chat.id, text)
        else:
            if markdown:
                print("markdown is true")
                bot.send_message(event.effective_chat.id, text, parse_mode="Markdown")
            else:
                bot.send_message(event.effective_chat.id, text)
            procmsg("Sending attachment")
            bot.send_photo(event.effective_chat.id, photo=attachment)
    print("running safexec")

    def alias(command):
        try:
            exec(ReadFF(f"{COMMANDSDIR}{command}/{command}.py"), globals(), locals_dict)
        except TypeError:
            raise Exception(f"Alias задан некорректно в команде {identificator}")

    def picturedata(path, text):
        pic = str(path)
        message("Loading...")
        try:
            try:
                print("Adding attachment")
                message(text, attachment=open(path, 'r').read(), reply=True)
                succ()
            except Exception as e:
                message(text + '\n///' + str(e) + '///', reply=True)
        except Exception as e:
            message('picture error: ' + str(e), reply=True)

    def picture(path, text):
        message("Loading...")
        try:
            try:
                print("Adding attachment")
                message(text, attachment=get(path).content, reply=True)
                succ()
            except Exception as e:
                message(text + '\n///' + str(e) + '///', reply=True)
        except Exception as e:
            message('picture error: ' + str(e), reply=True)

    def getname(uid, namecase="nom", nickname_if_possible=True):
        uid = getid(uid)
        if not os.path.exists(
                f"users/{uid}/nick.txt") or not nickname_if_possible:  # если нет никнейма или не нужен никнейм
            if uid != None:
                if not isgroup(uid):
                    unamee = vk.users.get(user_id=uid, name_case=namecase, lang=0)[0]
                    return unamee["first_name"] + " " + unamee["last_name"]
                else:
                    return vk.groups.getById(group_id=uid)[0]["name"]
            else:
                return "пользователь"
        else:
            return ReadFF(f"users/{uid}/nick.txt")

    exec(ReadFF("catenv.py"), globals(), locals_dict)
    locals_dict.update(locals())
    exec(script, globals(), locals_dict)



def Safemessage(event, text, attachment="", keyboard="", intent="default", disable_mentions=1, dont_parse=1, reply=True):
    print("running safemessage")
    bot.send_message(event.effective_chat.id, text)

def process(event, context):
    global media_safelock
    EventMsg(str(event.update_id))
    print(event)
    start = time.time()
    if event.effective_message or event.message:
        if (event.effective_message.text and event.effective_message.text.startswith("/")) or (event.message.caption and event.message.caption.startswith("/")):
            text = ""
            try:
                text = event.effective_message.text[1:].split(" ")
                text_raw = event.effective_message.text
            except:
                text = event.message.caption[1:].split(" ")
                text_raw = event.message.caption
            cmd = text[0].lower()
            flags = []
            parameter = text[1:]
            for word in parameter:
                if word.startswith("-") and word != "-":
                    flags.append(word.lower())
                    parameter.remove(word)
            parameter = " ".join(parameter)

            using = False
            outputd = False
            PlusWrite(text_raw + "\n", "usr/bread.txt")
            user_id = event.message.from_user.id
            peer_id = event.message.chat.id
            print(event.effective_message.text)
            procmsg(vars(event))
            # Поиск соответствия в списке команд
            for x in commands:
                if cmd == x:
                    Output(f"""
=================================
Detected command - {x}!
Syntax: {event.effective_message.text}
Parameter: {parameter}
""")

                    InfoMsg("Executing command - " + x)
                    code_js = convertjson(ReadFF(f"{COMMANDSDIR}{ids[commands.index(x)]}/{ids[commands.index(x)]}.json"))
                    author = code_js["author"]
                    mode = code_js["mode"]
                    identificator = code_js["identificator"]
                    command_ru = code_js["command_ru"]
                    description = code_js["description"]
                    is_media = False
                    if event.message.photo is not None:
                        print("Media attachment detected")
                        is_media = True
                    else:
                        is_media = False

                    if modes[commands.index(x)] == "pic" and is_media is False:
                        Safemessage(event, "Команда требует прикрепленного изображения.")
                    elif modes[commands.index(x)] == "pic" and is_media is True and media_safelock is False:
                        try:
                            procmsg("Enabling safelock")
                            media_safelock = True
                            succ()
                            procmsg("Downloading file")
                            bot.get_file(event.message.photo[-1].file_id).download("attachment_local")
                            writeTo("http://localhost:8000/attachment_local", "argv_picture.txt")
                            if not code_js["restricted"]:
                                code = ReadFF(f"{COMMANDSDIR}{ids[commands.index(x)]}/{ids[commands.index(x)]}.py")
                                procmsg("Command starting...")
                                if not code_js["testing"]:
                                    print("executing safeexec")
                                    Safeexec(event, code, locals())
                                    PlusWrite("used command: " + ids[commands.index(x)] + ".py\n", "commandslog.txt")
                                    if str(user_id) not in os.listdir("users"): os.mkdir(f"users/{user_id}")
                                    succ()
                                else:
                                    if isTester(user_id):
                                        Safeexec(event, code, locals())
                                    else:
                                        Safemessage(event,
                                            "Вы не являетесь тестировщиком, если вы хотите стать тестировщиком, то обратитесь в @catpy.beta!",
                                            reply=True)
                            else:
                                if str(user_id) not in ReadFF("usr/restricted.txt").split(","):
                                    procmsg("")
                                    Safemessage(event,
                                                "Данная команда внесена в пакет потенциально оскорбительных команд. Однако, подключить пакет можно командой \"подключить-пакет\".")
                                else:
                                    try:
                                        code = ReadFF(
                                            f"{COMMANDSDIR}{ids[commands.index(x)]}/{ids[commands.index(x)]}.py")
                                        if not code_js["testing"]:
                                            Safeexec(event, code, locals())
                                        else:
                                            if isTester(user_id):
                                                Safeexec(event, code, locals())
                                            else:
                                                Safemessage(event,
                                                            "Вы не являетесь тестировщиком, если вы хотите стать тестировщиком, то обратитесь в @catpy.beta!",
                                                            reply=True)
                                    except Exception as e:
                                        failcomplete()
                                        Output(e)
                                        Safemessage(event,
                                                    "Команда " + command_ru + " [" + identificator + f"] аварийно завершилась из-за ошибки.\nКод ошибки: {generrorcode(str(e), identificator)}\nАвтор команды: " + author + "\nИнформация об ошибке была автоматически отправлена администрации бота.")
                                        exc_type, exc_value, exc_tb = sys.exc_info()
                                        mta("==CatABMS-Package BugReport==\nОбщая информация:\n\nСерверное время: " + readableDate(
                                            time.time()) + "\nКоманда: " + command_ru + " [" + identificator + "]\nАвтор команды: " + author + "\nПользователь: " + getmention(
                                            user_id) + " (" + str(user_id) + ")\nID диалога (peer_id): " + str(
                                            peer_id) + "\nПереданный параметр: " + parameter + "\nКод ошибки: " + str(
                                            e) + "\n\nTraceback ошибки:\n\n" + "\n".join(
                                            traceback.format_exception(exc_type, exc_value, exc_tb)))
                                        Output("\n".join(traceback.format_exception(exc_type, exc_value, exc_tb)))
                                        # failcomplete()
                                    except vk_api.exceptions.ApiError as e:
                                        if str(e).startswith("[917]"):
                                            Safemessage(event,
                                                        "Упс! Я не могу выполнить эту команду, потому что не являюсь админом этого чата! Назначьте меня админом и повторите попытку снова.")
                        except Exception as e:
                            procmsg("Failed to process media command")
                            fail()
                            e.with_traceback()
                        finally:
                            procmsg("disabling safelock")
                            media_safelock = False
                            is_media = False
                            succ()
                        PlusWrite("used command: " + ids[commands.index(x)] + ".py\n", "commandslog.txt")
                        if str(user_id) not in os.listdir("users"): os.mkdir(f"users/{user_id}")
                        succ()
                    elif media_safelock is True and is_media is True:
                        Safemessage(event, "Бот не может одновременно обрабатывать медиа от нескольких пользователей, пожалуйста подождите")
                    elif modes[commands.index(x)] == "start" and parameter == "":
                        Safemessage(event, "Команда требует аргумента.\n\nПример использования: " + cmd + " текст")
                    else:
                        if not code_js["restricted"]:
                            code = ReadFF(f"{COMMANDSDIR}{ids[commands.index(x)]}/{ids[commands.index(x)]}.py")
                            procmsg("Command starting...")
                            if not code_js["testing"]:
                                print("executing safeexec")
                                Safeexec(event, code, locals())
                                PlusWrite("used command: " + ids[commands.index(x)] + ".py\n", "commandslog.txt")
                                if str(user_id) not in os.listdir("users"): os.mkdir(f"users/{user_id}")
                                succ()
                            else:
                                if isTester(user_id):
                                    Safeexec(event, code, locals())
                                else:
                                    Safemessage(event, "Вы не являетесь тестировщиком, если вы хотите стать тестировщиком, то обратитесь в @catpy.beta!",reply=True)
                            # except Exception as e:
                            #     Output(e)
                            #     message(
                            #         f"Команда {command_ru} [{identificator}] аварийно завершилась из-за ошибки.\nКод ошибки: {generrorcode(str(e), identificator)}\nАвтор команды: {author}\nИнформация об ошибке была автоматически отправлена администрации бота.")
                            #     exc_type, exc_value, exc_tb = sys.exc_info()
                            #     mta(f"==CatABMS-Package BugReport==\nОбщая информация:\n\nСерверное время: {readableDate(time.time())}\nКоманда: {command_ru} [{identificator}]\nАвтор команды: {author}\nПользователь: {getmention(user_id)} ({user_id})\nID диалога (peer_id): {peer_id}\nПереданный параметр: {parameter}\nКод ошибки: {e}\n\nTraceback ошибки:\n\n" + '\n'.join(
                            #         traceback.format_exception(exc_type, exc_value, exc_tb)))
                            #     Output("\n".join(traceback.format_exception(exc_type, exc_value, exc_tb)))
                            #     failcomplete()
                        else:
                            if str(user_id) not in ReadFF("usr/restricted.txt").split(","):
                                procmsg("")
                                Safemessage(event, "Данная команда внесена в пакет потенциально оскорбительных команд. Однако, подключить пакет можно командой \"подключить-пакет\".")
                            else:
                                try:
                                    code = ReadFF(f"{COMMANDSDIR}{ids[commands.index(x)]}/{ids[commands.index(x)]}.py")
                                    if not code_js["testing"]:
                                        Safeexec(event, code, locals())
                                    else:
                                        if isTester(user_id):
                                            Safeexec(event, code, locals())
                                        else:
                                            Safemessage(event, "Вы не являетесь тестировщиком, если вы хотите стать тестировщиком, то обратитесь в @catpy.beta!",reply=True)
                                except Exception as e:
                                    failcomplete()
                                    Output(e)
                                    Safemessage(event,
                                        "Команда " + command_ru + " [" + identificator + f"] аварийно завершилась из-за ошибки.\nКод ошибки: {generrorcode(str(e), identificator)}\nАвтор команды: " + author + "\nИнформация об ошибке была автоматически отправлена администрации бота.")
                                    exc_type, exc_value, exc_tb = sys.exc_info()
                                    mta("==CatABMS-Package BugReport==\nОбщая информация:\n\nСерверное время: " + readableDate(
                                        time.time()) + "\nКоманда: " + command_ru + " [" + identificator + "]\nАвтор команды: " + author + "\nПользователь: " + getmention(
                                        user_id) + " (" + str(user_id) + ")\nID диалога (peer_id): " + str(
                                        peer_id) + "\nПереданный параметр: " + parameter + "\nКод ошибки: " + str(
                                        e) + "\n\nTraceback ошибки:\n\n" + "\n".join(
                                        traceback.format_exception(exc_type, exc_value, exc_tb)))
                                    Output("\n".join(traceback.format_exception(exc_type, exc_value, exc_tb)))
                                    # failcomplete()
                                except vk_api.exceptions.ApiError as e:
                                    if str(e).startswith("[917]"):
                                        Safemessage(event, "Упс! Я не могу выполнить эту команду, потому что не являюсь админом этого чата! Назначьте меня админом и повторите попытку снова.")

        else:
            procmsg("not a command, skipping")
            procmsg("triggering handlers")
            if event.effective_message.text or event.message.caption:
                text = ""
                try:
                    text = event.effective_message.text
                    text_raw = event.effective_message.text
                except:
                    text = event.message.caption
                    text_raw = event.message.caption
                using = False
                outputd = False
                user_id = event.message.from_user.id
                peer_id = event.message.chat.id
                print(event.effective_message.text)
                procmsg(vars(event))
                procmsg(handlers)
                # Старт обработчиков по событию
                for x in handlers:
                    try:
                        Output(f"""
    =================================
    Triggering handler - {x}!
                        """)
                        print(f"{HANDLERSDIR}{hdl_ids[handlers.index(x)]}/{hdl_ids[handlers.index(x)]}.json")
                        code_js = convertjson(
                            ReadFF(f"{HANDLERSDIR}{hdl_ids[handlers.index(x)]}/{hdl_ids[handlers.index(x)]}.json"))
                        author = code_js["author"]
                        mode = code_js["mode"]
                        identificator = code_js["identificator"]
                        command_ru = code_js["identificator"]
                        description = code_js["description"]
                        if not code_js["restricted"]:
                            code = ReadFF(f"{HANDLERSDIR}{hdl_ids[handlers.index(x)]}/{hdl_ids[handlers.index(x)]}.py")
                            procmsg("Handler starting...")
                            if not code_js["testing"]:
                                print("executing safeexec")
                                Safeexec(event, code, locals())
                        else:
                            if str(user_id) not in ReadFF("usr/restricted.txt").split(","):
                                procmsg("not responding - restricted handler")
                            else:
                                try:
                                    code = ReadFF(
                                        f"{HANDLERSDIR}{hdl_ids[handlers.index(x)]}/{hdl_ids[handlers.index(x)]}.py")
                                    if not code_js["testing"]:
                                        Safeexec(event, code, locals())
                                    else:
                                        if isTester(user_id):
                                            Safeexec(event, code, locals())
                                except Exception as e:
                                    print(e)
                                    print(e.with_traceback(e.__traceback__))
                                    procmsg("could not run handler for this event")
                                    fail()
                    except Exception as e:
                        print(e)
                        print(e.__traceback__)

    else:
        procmsg("not a message, skipping")


    # lastid = event.update_id
    # writeTo(event.update_id, "lastid.txt")
    # print(str(event.update_id) + " written into lastid")
try:
    for x in diff:
        exec(f"del {x}")
except:
    pass
old_list = dir()
old_list.append("old_list")
old_list.append("diff")
old_list.append("textic")
old_list.append("textic_2")
InfoMsg("Started main cycle")

if only_admins:
    addition = " (безопасный режим)"
else:
    addition = ""
    mta(f"""Бот запущен{addition}.
Сервер: {Get("http://ident.me/")}
Операционная система: {osname}
Хостнейм: {platform.uname()[1]}""")
del addition

                # if peer_id not in __conversations__: __conversations__.append(peer_id)
                # Output(
                #     f"\n\n\n=================================\nNew message from user {getname(user_id)} ({str(user_id)}) in chat {str(peer_id)}\nContents: \"{event.object['text']}\"\nAttachments: {str(len(event.object['attachments']))}")
                # if len(event.object["attachments"]) > 0:
                #     atchmnts = []
                #     for atchmnt in event.object["attachments"]:
                #         atchmnts.append(atchmnt["type"])
                #     Output("Types of attachments: " + ", ".join(atchmnts) + "\n=================================\n\n")
                #     del atchmnt, atchmnts
                # else:
                #     Output("=================================")

                # useprefix = False
                # if event.from_chat:
                #     chat_id = event.chat_id
                # if textic.startswith(ReadFF("mention.txt")) and event.from_chat:
                #     textic = textic[len(ReadFF("mention.txt"))]
                #     textic_2 = textic_2[len(ReadFF("mention.txt"))]
                #     useprefix = True
                # if textic.startswith('/'):
                #     textic = textic[1:]
                #     textic_2 = textic_2[1:]
                #     useprefix = True
                #     using = True
                # if event.from_user:
                #     useprefix = True
                # cmd = textic.split(' ')[0]
                # parameter = textic_2.split(' ')[1:]
                # flags = []
                # for word in parameter:
                #     if word.startswith("-") and word != "-":
                #         flags.append(word.lower())
                #         parameter.remove(word)
                # parameter = ' '.join(parameter)

                # if cmd in commands:  # and (not "#hide" in ReadFF(COMMANDSDIR + cmd) or user_id in admins):
                #     using = True
                #     InfoMsg("Обработка...")
                # if textic_2 == "":
                #     using = False
                #
                # coun = 0
                # for x in rcs:
                #     coun += 1
                #     try:
                #         procmsg("Starting CoreRC module - " + str(coun))
                #         exec(x)
                #         succ()
                #     except Exception as e:
                #         failcomplete()
                #         exc_type, exc_value, exc_tb = sys.exc_info()
                #         messagecust(
                #             'Proccess died: \n' + "\n".join(traceback.format_exception(exc_type, exc_value, exc_tb)),
                #             242722587)
                #         system_errors += "Unable to start coreRC module - " + str(e) + endl
                #
                # if using == True and user_id in banned:
                #     using = False
                #
                # if using == True and str(user_id) in trolling.keys():
                #     using = False
                #
                # using = using and permitting_()
                #
                # #
                # # Обработчик-оптимизатор команд. Кусается!
                # #
                # if using:
                #     try:
                #         replytext = event.object["reply_message"]["text"]
                #         if parameter == "":
                #             parameter = replytext
                #             InfoMsg("Detected reply to message")
                #     except:
                #         pass
                #     try:
                #         writeTo(detectfull(event.object['attachments'][0]), 'argv_picture.txt')
                #     except:
                #         writeTo("none", "argv_picture.txt")
                #     ins = 'false'
                #


    #                 elif user_id in banned and useprefix == True:
    #                     message("Вы были заблокированы администрацией catpy.")
    #                 elif str(user_id) in trolling.keys() and useprefix == True:
    #                     message(trolling[str(user_id)])
    #                 else:
    #                     InfoMsg("Request will be ignored due to optimization.")
    #
    #             if int(psutil.virtual_memory().percent) >= 90:
    #                 mta(f"ПЕРЕМОГА БЛЯДЬ! ЗАНЯТО {psutil.virtual_memory().percent}% ОЗУ!!")
    #             new_list = dir()
    #             diff = list(set(new_list) - set(old_list))
    #             Output("Catware Memory Gun: u should clean this variables: " + ", ".join(diff))
    #             if enable_memgun_cleaning:
    #                 for kef in diff:
    #                     exec(f"del {kef}")

# except Exception as e:
#     InfoMsg("Hardened Core is working: main cycle crashed due to " + str(e) + ": " + str(__name__))
#     exc_type, exc_value, exc_tb = sys.exc_info()
#     mta(f"Ядро успещьно рухнуло!!1!! Трейс:\n" + '\n'.join(traceback.format_exception(exc_type, exc_value, exc_tb)))

