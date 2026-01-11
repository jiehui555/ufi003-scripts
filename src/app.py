import logging
import time
import click
import schedule

from src.tasks import task_one, task_two


@click.group()
def cli():
    pass


@click.command()
def run():
    click.echo("Running...")


@click.command()
def cron():
    schedule.every(5).seconds.do(task_one)
    schedule.every().minute.do(task_two)

    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        logging.info("Exiting due to keyboard interrupt (Ctrl+C).")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")


cli.add_command(run)
cli.add_command(cron)
