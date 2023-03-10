from unittest import TestCase
from app.trajectory_printer import TrajectoryPrinter
import pandas as pd
from tests.config.definitions import ROOT_DIR
import os
import movingpandas as mpd


class TestTrajectoryPrinter(TestCase):

    def setUp(self) -> None:
        self.sut = TrajectoryPrinter()

    def test_print(self):
        # prepare
        test_data: mpd.TrajectoryCollection = pd.read_pickle(os.path.join(ROOT_DIR, 'tests/resources/app/input2.pickle'))

        # execute
        actual: str = self.sut.print(test_data.trajectories[1])

        # verify
        self.assertTrue(actual.startswith("746: Trajectory 746"))
