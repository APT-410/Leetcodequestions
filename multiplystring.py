def multiply(num1: str, num2: str) -> str:
    # If one of the numbers is "0", the product is "0".
    if num1 == "0" or num2 == "0":
        return "0"
    
    # Get the lengths of both input numbers.
    m, n = len(num1), len(num2)
    
    # Create a list to store the result of multiplication.
    # The maximum possible length of the product is m + n.
    result = [0] * (m + n)
    
    # Loop over each digit in num1 (from right to left).
    for i in range(m - 1, -1, -1):
        # Convert the current digit from character to integer.
        digit1 = ord(num1[i]) - ord('0')
        
        # Loop over each digit in num2 (from right to left).
        for j in range(n - 1, -1, -1):
            # Convert the current digit from num2.
            digit2 = ord(num2[j]) - ord('0')
            
            # Multiply the two digits.
            product = digit1 * digit2
            
            # Calculate positions in the result list.
            # p2 is the index where the current product's unit digit goes.
            # p1 is the index where the carry (if any) will be added.
            p1, p2 = i + j, i + j + 1
            
            # Add the product to the current stored value at p2.
            # This may include a previous carry.
            sum_val = product + result[p2]
            
            # Set the current position (p2) to the units digit of sum_val.
            result[p2] = sum_val % 10
            
            # Add the tens digit (carry) to the position p1.
            result[p1] += sum_val // 10
    
    # Convert the list of digits into a string.
    # The join function creates a string from each integer in the list,
    # and lstrip('0') removes any extra zeros at the start.
    result_str = ''.join(map(str, result)).lstrip('0')
    
    return result_str

# Example usage:
print(multiply("2", "3"))      # Expected output: "6"
print(multiply("123", "456"))  # Expected output: "56088"
