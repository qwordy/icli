import json
import logging

FILENAME = 'commands.txt'

logger = logging.getLogger(__name__)


class Node:
    def __init__(self, word='', help=''):
        # Right most word of the command
        self.word = word
        # Help of the command
        self.help = help
        self.parameters = []
        # [Node]
        self.children = []


class Parameter:
    def __init__(self, name='', help=''):
        # Parameter name
        self.name = name,
        # Parameter help
        self.help = help


class Completer:

    def __init__(self):
        self.root = Node()
        # Load data
        commands = json.load(open(FILENAME))
        for command in commands:
            logger.error(command['command'])
            self._insert(command)
        logger.error(self.root)

    def complete(self, code):
        """
        Code auto completion
        :param code:
        :return: matches, metadata
        """
        tokens = code.split()
        if code[-1] == ' ':
            tokens.append('')
        cursor_start = len(code) - len(tokens[-1])

        node = self.root
        for i in range(len(tokens) - 1):
            find = False
            for child in node.children:
                if tokens[i] == child.word:
                    node = child
                    find = True
                    break
            if not find:
                return None
        # Match last word
        matches = []
        metadata = {}
        word = tokens[-1]
        for child in node.children:
            if child.word.startswith(word):
                matches.append(child.word)
                metadata[child.word] = child.help
        if matches:
            return matches, cursor_start, metadata
        return None

    def _insert(self, command):
        tokens = command['command'].split()
        help = command['help']
        node = self.root
        for token in tokens:
            find = False
            for child in node.children:
                if token == child.word:
                    node = child
                    find = True
                    break
            if not find:
                child = Node(word=token)
                node.children.append(child)
                node = child
        node.help = help


if __name__ == '__main__':
    Completer()
