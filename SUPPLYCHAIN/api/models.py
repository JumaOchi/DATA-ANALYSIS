import numpy as np
from scipy.optimize import linprog

def optimize_routes(cost_per_route, time_per_route, max_time):
    cost_per_route = np.array(cost_per_route)
    time_per_route = np.array(time_per_route)
    
    A_ub = np.array([time_per_route])
    b_ub = np.array([max_time])
    
    x_bounds = [(0, 1) for _ in range(len(cost_per_route))]

    res = linprog(c=cost_per_route, A_ub=A_ub, b_ub=b_ub, bounds=x_bounds, method='highs')

    result = {
        "optimal_route_assignment": res.x.tolist(),
        "optimized_cost": res.fun,
        "total_time_required": np.dot(res.x, time_per_route)
    }
    
    return result

