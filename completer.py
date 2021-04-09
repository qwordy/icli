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
        # Parameters
        self.parameters = []
        # Node
        self.children = []


class Parameter:
    def __init__(self, name='', help=''):
        # Parameter name
        self.name = name
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
        # logger.debug(self.root)

    def complete(self, code):
        """
        Code auto completion
        :param code:
        :return: matches, cursor_start, metadata
        """
        tokens = code.split()
        if code[-1] == ' ':
            tokens.append('')
        cursor_start = len(code) - len(tokens[-1])

        # Find complete command range
        command_len = len(tokens) - 1
        for i in range(len(tokens) - 1):
            if tokens[i][0] == '-':
                command_len = i
                break

        # Match command
        node = self.root
        for i in range(command_len):
            find = False
            for child in node.children:
                if tokens[i] == child.word:
                    node = child
                    find = True
                    break
            if not find:
                return None

        # Match last word
        # Matched words including commands and parameters
        matches = []
        # Extra message. {candidate: message}
        metadata = {}
        word = tokens[-1]
        # Command
        for child in node.children:
            if child.word.startswith(word):
                matches.append(child.word)
                metadata[child.word] = child.help
        # Parameter
        for p in node.parameters:
            if p.name.startswith(word):
                matches.append(p.name)
                metadata[p.name] = p.help
        if matches:
            return matches, cursor_start, metadata
        return None

    def _insert(self, command):
        tokens = command['command'].split()
        help = command['help']
        parameters = command['parameters']
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
                child.parameters = [Parameter(p['name'], p['help']) for p in parameters]
                node.children.append(child)
                node = child
        node.help = help


if __name__ == '__main__':
    Completer()
