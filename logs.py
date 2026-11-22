import logging

def iniciar_logs():
    logging.basicConfig(
        filename="registro_sistema.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )