def compute_co2_efficiency(co2_reduction: float, investment_cost: float) -> float | str:
    try:
        # Ensure investment_cost is treated as a number.
        # Convert to float and handle potential non-numeric inputs gracefully.
        numeric_investment_cost = float(investment_cost)

        if numeric_investment_cost == 0:
            # Explicitly handle division by zero for clarity
            return "Cannot compute: Investment Cost is zero."
        else:
            # Compute the ratio. Investment_Cost is assumed to be in millions,
            # so multiply by 1,000,000 to get the actual cost in the denominator.
            efficiency = co2_reduction / (numeric_investment_cost * 1_000_000)
            return efficiency
    except ValueError:
        # Handle cases where investment_cost cannot be converted to a float
        return "Cannot compute: Invalid Investment Cost (not a number)."
    except Exception as e:
        # Catch any other unexpected errors during computation
        return f"Cannot compute: An unexpected error occurred - {e}"