import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Test that an empty list returns a streak of 0."""
    assert longest_positive_streak([]) == 0

def test_no_positive_numbers():
    """Test a list with no positive numbers."""
    assert longest_positive_streak([-1, -2, 0, -5]) == 0

def test_all_positive_numbers():
    """Test a list with all positive numbers."""
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_single_streak():
    """Test a single streak of positive numbers."""
    assert longest_positive_streak([1, 2, 0, 4, 5, 6]) == 3

def test_multiple_streaks_longest_first():
    """Test multiple streaks where the longest streak is first."""
    assert longest_positive_streak([1, 2, 3, 0, 1, 2]) == 3

def test_multiple_streaks_longest_last():
    """Test multiple streaks where the longest streak is last."""
    assert longest_positive_streak([1, 2, 0, 1, 2, 3, 4]) == 4

def test_streaks_with_negatives():
    """Test streaks separated by negative numbers."""
    assert longest_positive_streak([1, 2, -1, 3, 4, 5, -2, 1]) == 3

def test_streaks_with_zeros():
    """Test streaks separated by zeros."""
    assert longest_positive_streak([1, 0, 2, 3, 0, 4, 5, 6]) == 3

def test_single_element_list():
    """Test lists with a single element."""
    assert longest_positive_streak([1]) == 1
    assert longest_positive_streak([0]) == 0
    assert longest_positive_streak([-1]) == 0

def test_mixed_positive_and_non_positive():
    """Test a complex mix of positive and non-positive numbers."""
    assert longest_positive_streak([1, 2, 0, -1, 3, 4, 5, 0, 1, 2, -5, 6]) == 3