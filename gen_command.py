"""
Generate all available Azure CLI commands, parameters and help
"""

import json

from azure.cli.core import AzCli, MainCommandsLoader
from azure.cli.core._help import AzCliHelp
from azure.cli.core.commands import AzCliCommandInvoker
from azure.cli.core.file_util import create_invoker_and_load_cmds_and_args, get_all_help
from azure.cli.core.parser import AzCliCommandParser

FILENAME = 'commands.txt'


def main():
    az_cli = AzCli(cli_name='az',
                   commands_loader_cls=MainCommandsLoader,
                   invocation_cls=AzCliCommandInvoker,
                   parser_cls=AzCliCommandParser,
                   help_cls=AzCliHelp)
    create_invoker_and_load_cmds_and_args(az_cli)
    help_files = get_all_help(az_cli)
    commands = []
    for help_file in help_files:
        if not help_file.command:
            continue
        command = {
            'command': 'az ' + help_file.command,
            'help': help_file.short_summary,
            'parameters': []
        }
        if hasattr(help_file, 'parameters'):
            for parameter in help_file.parameters:
                for name in parameter.name_source:
                    command['parameters'].append({
                        'name': name,
                        'help': parameter.short_summary
                    })
        commands.append(command)
    with open(FILENAME, 'w', encoding='utf8') as f:
        f.write(json.dumps(commands, indent=2))


if __name__ == '__main__':
    main()
