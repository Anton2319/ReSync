if event.object["text"].lower() == "никита фурсенко" and user_id == getid("durka_men"):
    message("ококок щя")
    for aye in __conversations__:
        if aye > 2E9:
            vk.messages.removeChatUser(member_id=getid("nikit0s4"), random_id=rid(), chat_id=aye - 2E9)