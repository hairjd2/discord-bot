def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == "test bot":
        return "test worked!"
