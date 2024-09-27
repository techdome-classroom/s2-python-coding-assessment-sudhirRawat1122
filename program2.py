
import unittest

class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Convert a Roman numeral to an integer.

        Args:
        s (str): A string representing a Roman numeral.

        Returns:
        int: The integer representation of the Roman numeral.
        """
        if not s:
            return 0  # Handle empty string

        # Map of Roman numerals to integer values
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0  # Total sum to return
        prev_value = 0  # Value of the previous numeral

        # Traverse the string from right to left for easier subtraction handling
        for char in reversed(s):
            if char not in roman_to_int:
                raise ValueError(f"Invalid Roman numeral character: {char}")

            current_value = roman_to_int[char]

            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value

            prev_value = current_value  # Update previous value for next iteration

        return total