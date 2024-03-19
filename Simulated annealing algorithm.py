import random
import math

def cost_func(state):
    # Example cost function: minimize the sum of squared elements
    return sum(x**2 for x in state)

def neighbor_func(state):
    # Example neighbor function: perturb each element randomly
    return [x + random.uniform(-0.1, 0.1) for x in state]

def simulated_annealing(cost_func, neighbor_func, initial_state, initial_temp, cooling_rate):
    current_state = initial_state
    current_cost = cost_func(initial_state)
    temp = initial_temp
    while temp > 0.1:
        neighbor = neighbor_func(current_state)
        neighbor_cost = cost_func(neighbor)
        delta_cost = neighbor_cost - current_cost
        if delta_cost < 0 or random.random() < math.exp(-delta_cost / temp):
            current_state = neighbor
            current_cost = neighbor_cost
        temp *= cooling_rate
    return current_state

initial_state = [1, 2, 3, 4]  # Define the initial state
initial_temp = 100.0   # Define the initial temperature
cooling_rate = 0.95  # Define the cooling rate
final_state = simulated_annealing(cost_func, neighbor_func, initial_state, initial_temp, cooling_rate)
print("Final state:", final_state)
