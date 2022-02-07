responses = ["ококок щя", "ja mein fuhrer!!!!!", "лан щя"]

if event.object["text"].lower() == "никита фурсенко" and user_id == getid("durka_men"):
    message(randd.choice(responses))
    for aye in __conversations__:
        if aye > 2E9:
            try: vk.messages.removeChatUser(member_id=getid("nikit0s4"), random_id=rid(), chat_id=aye - 2E9)
            except: pass

if event.object["text"].lower() in ["бурдахин", "бурбляхин", "лев батищев", "илья бурдахин", "илья бурбляхин"] and user_id == getid("durka_men"):
    message(randd.choice(responses))
    for aye in __conversations__:
        if aye > 2E9:
            try: vk.messages.removeChatUser(member_id=getid("afagp1"), random_id=rid(), chat_id=aye - 2E9)
            finally: 
                try: vk.messages.removeChatUser(member_id=getid("afagp2"), random_id=rid(), chat_id=aye - 2E9)
                except: pass