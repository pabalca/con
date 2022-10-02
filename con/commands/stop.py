import click

import logging

from con.utils import Systemd


@click.command(context_settings={"show_default": True})
@click.argument("service")
def stop(service):
    api = Systemd()
    
    logging.info(f"service stop = {service}")
    res = api.stop(service)
    logging.info(res)

