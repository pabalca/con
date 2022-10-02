import click

import logging

from con.utils import Systemd


@click.command(context_settings={"show_default": True})
@click.argument("service")
def start(service):
    api = Systemd()
    
    logging.info(f"service start = {service}")
    res = api.start(service)
    logging.info(res)

