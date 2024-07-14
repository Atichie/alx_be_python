def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom = float(denominator)

        formatted_num = format(num, '.1f')
        formatted_denom = format(denom, '.1f')
        result = formatted_num / formatted_denom
        return f"The result of {formatted_num} divided by {formatted_denom} is {result:1f}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    except ValueError:
        return "Error: Please enter numeric values only."
