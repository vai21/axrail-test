import json

def cheapest_flight(case):
    data: json
    with open(case, "r") as file:
        data = json.load(file)
    # print(data["n"])
    # print(data["flights"])

    # Create an array to store the minimum cost to reach each node.
    # Initialize the array with maximum values, except for the source node which has cost 0.
    dp = [float('inf')] * data["n"]
    dp[data["src"]] = 0

    # Iterate through each stop up to k.
    for _ in range(data["k"] + 1):
        # Create a temporary array to store the update costs for this iteration.
        temp = dp[:]
        # Iterate through each flight.
        for flight in data["flights"]:
            # Check if we can reach the starting node of the current flight from the source node.
            if dp[flight[0]] != float('inf'):
                # Update the cost to reach the destination node of the current flight if it's cheaper.
                temp[flight[1]] = min(temp[flight[1]], dp[flight[0]] + flight[2])
        # Update dp array with the temporary array for this iteration.
        dp = temp

    # Return the cost to reach the destination node.If it's still Integer.MAX_VALUE, it means it's not reachable.
    return dp[data["dst"]] if dp[data["dst"]] != float('inf') else -1
