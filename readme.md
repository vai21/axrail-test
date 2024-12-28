Intuition
The problem requires finding the cheapest price to reach a destination from a source with a limited number of stops. This problem can be efficiently solved using dynamic programming.
Approach

    Initialize an array dp of size n to store the minimum cost to reach each city.
    Set the cost to reach the source city as 0 and all other cities' costs as Integer.MAX_VALUE.
    Iterate through each possible number of stops from 0 to k:
        Create a copy of the dp array for each iteration.
        Update the minimum cost for each destination city based on the current flight.
    Finally, return the minimum cost to reach the destination city (dp[dst]).

Complexity

    Time complexity: O(k⋅∣flights∣), where |flights| is the number of flights.
    Space complexity: O(n), where n is the number of cities.

