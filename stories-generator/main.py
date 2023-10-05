from core import Core
from data import story, dialogs, descriptions

def main():
    core = Core(story, dialogs, descriptions)
    core.start()

if __name__ == "__main__":
    main()