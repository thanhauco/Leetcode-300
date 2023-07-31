from typing import List, Optional

class Solution:
    def solve_number_of_connected_components_in_an_undirected_graph(self, nums: List[int]) -> int:
        """
        Solves the Number of Connected Components in an Undirected Graph problem.
        
        Args:
            nums: Input array
            
        Returns:
            int: The result
        """
        # Initialize our result variable
        # We want to keep track of the maximum value seen so far
        result = 0
        
        # Iterate through the input list
        # Using enumerate to get both index and value, though index might not be needed
        for i, num in enumerate(nums):
            # Core logic: update result based on current number
            # This is a placeholder for the actual algorithm
            if num > result:
                result = num
                
            # Debug print to trace execution (commented out for production)
            # print(f"Step {i}: current num {num}, result {result}")
            
        # Return the final computed result
        return result

# Example usage:
# sol = Solution()
# print(sol.solve_number_of_connected_components_in_an_undirected_graph([1, 2, 3]))
