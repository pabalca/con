import click

import logging

from con.utils import Systemd


@click.command(context_settings={"show_default": True})
@click.argument("service")
def status(service):
    api = Systemd()
    
    logging.info(f"service status = {service}")
    active, loaded = api.status(service)
    logging.info(f"{service} active={active} loaded={loaded}")

