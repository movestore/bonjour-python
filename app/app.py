from sdk.moveapps_spec import hook_impl
from movingpandas import TrajectoryCollection
import logging
from app.trajectory_printer import TrajectoryPrinter


class App(object):

    def __init__(self, moveapps_io):
        self.moveapps_io = moveapps_io
        self.traj_printer = TrajectoryPrinter()

    @hook_impl
    def execute(self, data: TrajectoryCollection, config: dict) -> TrajectoryCollection:
        logging.info(f'Bonjour 🥖. I was called w/ configuration {dict}.')
        for traj in data.trajectories:
            logging.info(self.traj_printer.print(traj))
        return data
