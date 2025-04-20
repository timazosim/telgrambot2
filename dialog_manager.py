from collections import defaultdict

class DialogManager:
    def __init__(self):
        self.user_messages = defaultdict(list)

    def get_history(self, user_id: int) -> list[dict]:
        return self.user_messages[user_id]

    def add_message(self, user_id: int, role: str, content: str):
        self.user_messages[user_id].append({"role": role, "content": content})
        if len(self.user_messages[user_id]) > 20:
            self.user_messages[user_id] = self.user_messages[user_id][-20:]

    def clear_history(self, user_id: int):
        self.user_messages[user_id].clear()

dialog_manager = DialogManager()
