"""
The following problem is taken from Leetcode.
Refer the link for the question: https://leetcode.com/problems/integer-to-roman/description/?envType=study-plan-v2&envId=top-interview-150

"""

"""
Accepted Solution
"""


class Solution:
    def __init__(self):
        pass

    def intToRoman(self, num: int) -> str:
        symbol_value_dict = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }

        limit_decimal = {
            0: 5,
            1: 50,
            2: 500,
            3: 1000
        }

        limit_decimal_fallback = {
            1: 1,
            2: 10,
            3: 100,
            4: 1000
        }

        num_str = str(num)
        roman_string = ""

        while num_str != '0':
            num_of_decimal_places = len(num_str) - 1
            max_symbol = num_str[0]

            if max_symbol != '4' and max_symbol != '9':
                if num_of_decimal_places == 0:
                    max_number = int(max_symbol)
                else:
                    max_number = int(max_symbol) * pow(10, num_of_decimal_places)

                if max_number >= 1000:
                    remaining_number_positions = max_number // limit_decimal_fallback[num_of_decimal_places+1]
                    roman_string += symbol_value_dict[limit_decimal_fallback[num_of_decimal_places+1]] * remaining_number_positions
                else:
                    if max_number >= limit_decimal[num_of_decimal_places]:
                        roman_string += symbol_value_dict[limit_decimal[num_of_decimal_places]]

                        remaining_number_positions = (max_number - limit_decimal[num_of_decimal_places]) // limit_decimal_fallback[num_of_decimal_places+1]

                        roman_string +=  symbol_value_dict[limit_decimal_fallback[num_of_decimal_places+1]] * remaining_number_positions
                    else:
                        remaining_number_positions = max_number // limit_decimal_fallback[num_of_decimal_places+1]
                        roman_string += symbol_value_dict[limit_decimal_fallback[num_of_decimal_places+1]] * remaining_number_positions
            else:
                max_number = int(max_symbol) * pow(10, num_of_decimal_places)

                roman_string += symbol_value_dict[max_number]

            num_str = str(int(num_str) - max_number)

        return roman_string


if __name__ == '__main__':
    # Input 1
    num = 3749

    sol = Solution()
    result = sol.intToRoman(num)
    print(result)

    # Input 2
    num = 58

    sol = Solution()
    result = sol.intToRoman(num)
    print(result)

    # Input 3
    num = 1994

    sol = Solution()
    result = sol.intToRoman(num)
    print(result)

    # Inputs
    nums = [8, 10, 40, 11, 50]

    sol = Solution()
    for num in nums:
        result = sol.intToRoman(num)
        print(result)