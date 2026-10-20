from datetime import date

from planner import completion_rate, days_left, is_urgent, sort_by_due


# This test is already written for you. Read it, then run pytest.
def test_days_left_counts_days_until_due():
    # Arrange
    today = date(2026, 10, 19)
    due = date(2026, 10, 22)
    # Act
    result = days_left(due, today)
    # Assert
    assert result == 3


# Now write the tests below. Use the same three steps: Arrange, Act, Assert.
def test_days_left_is_negative_when_overdue():
    # Arrange
    today = date(2026, 10, 19)
    due = date(2026, 10, 17)

    # Act
    result = days_left(due, today)

    # Assert
    assert result == -2


def test_is_urgent_when_due_tomorrow():
    # Arrange
    today = date(2026, 10, 19)
    due = date(2026, 10, 20)

    # Act
    result = is_urgent(due, today)

    # Assert
    assert result is True


def test_is_urgent_when_due_in_exactly_two_days():
    # Arrange
    today = date(2026, 10, 19)
    due = date(2026, 10, 21)

    # Act
    result = is_urgent(due, today)

    # Assert
    assert result is True


def test_is_urgent_when_overdue():
    # Arrange
    today = date(2026, 10, 19)
    due = date(2026, 10, 18)

    # Act
    result = is_urgent(due, today)

    # Assert
    assert result is False


def test_sort_by_due_puts_soonest_task_first():
    # Arrange
    tasks = [
        {"title": "Assignment", "due": date(2026, 10, 25)},
        {"title": "Quiz", "due": date(2026, 10, 20)},
        {"title": "Report", "due": date(2026, 10, 22)},
    ]

    # Act
    result = sort_by_due(tasks)

    # Assert
    assert result[0]["title"] == "Quiz"


def test_completion_rate_is_zero_when_no_tasks():
    # Arrange
    done = 0
    total = 0

    # Act
    result = completion_rate(done, total)

    # Assert
    assert result == 0.0


def test_completion_rate_one_out_of_three():
    # Arrange
    done = 1
    total = 3

    # Act
    result = completion_rate(done, total)

    # Assert
    assert result == 33.3
