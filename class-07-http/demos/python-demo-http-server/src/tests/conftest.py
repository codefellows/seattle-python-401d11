from multiprocessing import Process
from src import server
import pytest


@pytest.fixture(scope='session', autouse=True)
def server_setup():
    instance = server.create_server()

    process = Process(target=instance.serve_forever)
    process.daemon = True
    process.start()
