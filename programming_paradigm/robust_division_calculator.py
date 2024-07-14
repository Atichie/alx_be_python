def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom = float(denominator)

        result = num / denom
        return f"The result of {num} divided by {denom} is {result:2f}"

    except ZeroDivisionError:
        return "Error: Division by zero not allowed."

    except ValueError:
        return "Error: Both numerator and denominator must be numeric values."
