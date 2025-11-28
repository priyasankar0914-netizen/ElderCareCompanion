def message(sender: str, receiver: str, mtype: str, payload: dict):
    return {
        "sender": sender,
        "receiver": receiver,
        "type": mtype,
        "payload": payload
    }
