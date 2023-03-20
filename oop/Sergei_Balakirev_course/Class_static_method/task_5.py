class AppStore:
    apps = []

    def add_application(self, app):
        self.apps.append(app)

    def remove_application(self, app):
        self.apps.remove(app)

    def block_application(self, app):
        Application.blocked = True

    def total_apps(self):
        return len(self.apps)


class Application:
    blocked = False

    def __init__(self, name):
        self.name = name
