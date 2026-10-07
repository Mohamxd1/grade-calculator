"""Course grade calculations."""


def weighted_average(categories):
    """Return the weighted course grade for a list of categories.

    Each category is a dict with:
      - "name": a label like "Homework"
      - "scores": a list of scores from 0 to 100
      - "weight": how much the category counts, as a fraction of 1.0

    The grade is the average score in each category, multiplied by that
    category's weight, summed across all categories.
    """
    total = 0.0
    for category in categories:
        scores = category["scores"]
        weight = category["weight"]
        average = sum(scores) / len(categories)
        total += average * weight
    return total


def letter_grade(score):
    """Convert a numeric score (0-100) to a letter grade A-F."""
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"
