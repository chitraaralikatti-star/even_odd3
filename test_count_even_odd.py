from count_even_odd import count_even_odd
def test_count_even_odd():
    expected_output = (
        "Even Count: 3\n"
        "Odd Count: 3"
    )
    assert count_even_odd([1, 2, 3, 4, 6, 7]) == expected_output
