from realtime_monitor import start_monitoring
from loguru import logger

def main():
    while True:
        logger.info("AI Website Blocker")
        logger.info("1. Start monitoring and blocking")
        logger.info("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            start_monitoring()
        elif choice == "2":
            logger.info("Exit")
            break
        else:
            logger.warning("Invalid choice")

if __name__ == "__main__":
    main()
