class Cli:
    """
    Cli class for handling user input
    """

    def __init__(self):
        self.map = {}

    def route(self, user_input: str):
        def _route(f):
            self.map[user_input] = f
            return f
        return _route

    def run(self):
        while True:
            s = input('>> ')
            if s in self.map:
                self.map[s]()


cli = Cli()


@cli.route('hello')
def on_hello():
    print("I see Hello")


cli.run()
