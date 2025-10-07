class MyAgent:
    def __init__(self, name):
        self.name = name

    def act(self):
        print(f"{self.name} is acting.")

    def think(self):
        print(f"{self.name} is thinking.")

    def greet(self):
        print(f"Hello, I am {self.name}!")


if __name__ == "__main__":
    agent = MyAgent("SampleAgent")
    agent.greet()
    agent.think()
    agent.act()