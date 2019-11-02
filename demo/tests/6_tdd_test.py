import pytest

class Meetup:

    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time

    def status(self):
        return "running"


def test_meetup_is_running():
    start = "1"
    end = "2"
    meetup = Meetup(start, end)
    assert meetup.status() == "running"


def test_meetup_is_over():
    start = "1"
    end = "2"
    meetup = Meetup(start, end)
    assert meetup.status() == "over"