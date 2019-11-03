import pytest
from datetime import datetime, timedelta


class TimeError(Exception):
    ...


# class Meetup:
#     def __init__(self, start_time, end_time):
#         self.start_time = start_time
#         self.end_time = end_time

#     def status(self):
#         return "running"

# class Meetup:
#     def __init__(self, start_time, end_time):
#         self.start_time = start_time
#         self.end_time = end_time

#     def status(self):
#         now = datetime.now()
#         if self.start_time > now:
#             return "coming_soon"
#         return "running"


# class Meetup:
#     def __init__(self, start_time, end_time):
#         self.start_time = start_time
#         self.end_time = end_time

#     def status(self):
#         now = datetime.now()
#         if self.start_time > now:
#             return "coming_soon"
#         elif now > self.end_time:
#             return "over"
#         return "running"


class Meetup:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time

    def status(self):
        now = datetime.now()
        if self.start_time > self.end_time:
            raise TimeError("Start is bigger than end")

        if self.start_time > now:
            return "coming_soon"
        elif now > self.end_time:
            return "over"
        return "running"


def test_meetup_is_running():
    start = datetime.now() - timedelta(days=1)
    end = datetime.now() + timedelta(days=1)
    meetup = Meetup(start, end)
    assert meetup.status() == "running"


def test_meetup_is_coming_soon():
    start = datetime.now() + timedelta(days=1)
    end = datetime.now() + timedelta(days=2)
    meetup = Meetup(start, end)
    assert meetup.status() == "coming_soon"


def test_meetup_is_over():
    start = datetime.now() - timedelta(days=2)
    end = datetime.now() - timedelta(days=1)
    meetup = Meetup(start, end)
    assert meetup.status() == "over"


def test_meetup_start_bigger_end_raises_exception():
    start = datetime.now() + timedelta(days=2)
    end = datetime.now() + timedelta(days=1)
    meetup = Meetup(start, end)

    with pytest.raises(TimeError):
        meetup.status()


TIME_VARIATIONS = [
    (datetime.now() - timedelta(days=1), datetime.now() + timedelta(days=1), "running"),
    (
        datetime.now() + timedelta(days=1),
        datetime.now() + timedelta(days=2),
        "coming_soon",
    ),
    (datetime.now() - timedelta(days=2), datetime.now() - timedelta(days=1), "over"),
]


@pytest.mark.parametrize("start,end,expected", TIME_VARIATIONS)
def test_meetup_status(start, end, expected):
    meetup = Meetup(start, end)
    assert meetup.status() == expected
