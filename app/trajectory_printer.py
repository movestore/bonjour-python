from movingpandas import Trajectory
import logging


class TrajectoryPrinter:

    @staticmethod
    def print(traj: Trajectory) -> str:
        return f'{traj.id}: {traj.crs} [{traj.get_bbox()}]'
