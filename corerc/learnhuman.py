try:
    if event.object["reply_message"] and textic_2 != "":
        o = event.object["reply_message"]["text"] + "\\" + textic_2
        Get("http://artificalintellect.pythonanywhere.com/add?access_token=OUJFVHLKRUHlWURHGKURGFkygsRKHFLSEHUFJjKJFhJLSLHRFJ<SHFGKJSDGFKJHGSDFhjsdkfhbjSDHGFukSDF&text=" + o)
    elif len(event.object['attachments']) == 1 and event.object['attachments'][0]['type'] == 'audio_message':
        if event.object['attachments'][0]['audio_message']['transcript_state'] == "done":
            Get("http://artificalintellect.pythonanywhere.com/voicebread?access_token=OUJFVHLKRUHlWURHGKURGFkygsRKHFLSEHUFJjKJFhJLSLHRFJ<SHFGKJSDGFKJHGSDFhjsdkfhbjSDHGFukSDF&text=" + event.object['attachments'][0]['audio_message']['transcript'])
    else:
        pass
except:
    pass