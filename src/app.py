import logging
import time
import schedule


def task_one():
    logging.info("Executing Task One: This runs every 10 seconds.")


def task_two():
    logging.info("Executing Task Two: This runs every minute.")


def run() -> int:
    schedule.every(10).seconds.do(task_one)
    schedule.every().minute.do(task_two)

    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        logging.info("Exiting due to keyboard interrupt (Ctrl+C).")
        return 0  # 返回退出码 0，表示正常退出
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return 1
