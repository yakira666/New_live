class Viber:
    ll = []

    def add_message(msg):
        """добавление нового сообщения в список сообщений;
        """
        Viber.ll.append(msg)

    def remove_message(msg):
        """удаление сообщения из списка;
        """
        Viber.ll.remove(msg)

    def set_like(msg):
        """поставить/убрать лайк для сообщения msg
        (если лайка нет то он ставится, если уже есть, то убирается);
        """
        if Message.fl_like is False:
            Message.fl_like = True
        else:
            Message.fl_like = False

    def show_last_message(num):
        """отображение последних сообщений;
        """
        print(Viber.ll[:num:-1])

    def total_messages():
        """звращает общее число сообщений.
        """
        return len(Viber.ll)


class Message:
    fl_like = False

    def __init__(self, text):
        self.text = text
