from azure.cli.core import AzCli, MainCommandsLoader
from azure.cli.core._help import AzCliHelp
from azure.cli.core.commands import AzCliCommandInvoker
from azure.cli.core.file_util import create_invoker_and_load_cmds_and_args, get_all_help
from azure.cli.core.parser import AzCliCommandParser


def main():
    az_cli = AzCli(cli_name='az',
                   commands_loader_cls=MainCommandsLoader,
                   invocation_cls=AzCliCommandInvoker,
                   parser_cls=AzCliCommandParser,
                   help_cls=AzCliHelp)
    create_invoker_and_load_cmds_and_args(az_cli)
    help_files = get_all_help(az_cli)
    for help_file in help_files:
        print(help_file.command)
        print(help_file.short_summary)
        if hasattr(help_file, 'parameters'):
            for parameter in help_file.parameters:
                print(parameter.name, parameter.short_summary)
        print()


if __name__ == '__main__':
    main()
