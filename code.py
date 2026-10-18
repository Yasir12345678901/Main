def percent_correct(score, total):
    """Return score as a whole-number percent of total (0 if total is 0)."""
    if total == 0:
        return 0
    return round(100 * score / total)

print(percent_correct(2,20))
