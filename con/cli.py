import click
import collections
from con.commands import status, start, stop


class OrderedGroup(click.Group):
    """
    https://stackoverflow.com/questions/47972638/how-can-i-define-the-order-of-click-sub-commands-in-help
    """
    def __init__(self, name=None, commands=None, **attrs):
        super(OrderedGroup, self).__init__(name, commands, **attrs)
        self.commands = commands or collections.OrderedDict()

    def list_commands(self, ctx):
        return self.commands


@click.group(cls=OrderedGroup, help="con[trol] the system (v1) @ pabalca")
def cli():
    pass


cli.add_command(status.status)
cli.add_command(start.start)
cli.add_command(stop.stop)



if __name__ == '__main__':
    cli()
