from core import Core
from story_automaton import StoryAutomaton
from interactions import Interactions
from customization import Customization
from data import story, descriptions

def main():
    core = Core(story, descriptions, StoryAutomaton(), Interactions(), Customization())
    core.start()

if __name__ == "__main__":
    main()