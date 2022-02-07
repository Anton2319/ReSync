if user_id in muted and peer_id != user_id:
    try:
        vk.messages.delete(message_ids=globalid(event.object['conversation_message_id'], peer_id), delete_for_all=1)
        using = False
    except Exception as e: 
        succ()
        Output("[DEBUG] Catpy Mute: cannot delete message for everyone - " + str(e))
