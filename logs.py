import logging

def iniciar_logs():
    logging.basicConfig(
        filename="registro_sistema.log",
        level=logging.INFO,
        encoding="utf-8",
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )