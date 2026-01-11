import logging
import time
import click
import schedule

from src import config
from src.tasks import demo, topfeel
from src.utils.feishu import FeiShu


@click.group()
def cli():
    pass


@click.command()
def run():
    topfeel.auto_sign_in()


@click.command()
def feishu_demo():
    feishu = FeiShu(config.FEISHU_APP_ID, config.FEISHU_APP_SECRET)
    feishu.send_text_message("这是一条测试信息", config.FEISHU_MY_OPEN_ID)


@click.command()
def cron():
    schedule.every(5).seconds.do(demo.task_one)
    schedule.every().minute.do(demo.task_two)

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
cli.add_command(feishu_demo)
