"""
Market-Making & Betting-Game Simulator

Assembled from your step-by-step solutions.
"""

import numpy as np

# Step 1 - expected_value
def expected_value(values, probabilities):
    return float(np.sum(np.asarray(values) * np.asarray(probabilities)))

# Step 2 - one_reroll_die_value
def one_reroll_die_value(sides):
    faces = np.arange(1, sides + 1)
    probabilities = np.full(sides, 1 / sides)

    rerolL_value = expected_value(faces, probabilities)

    optimal_values = np.maximum(faces, rerolL_value)
    game_value = expected_value(optimal_values, probabilities)

    reroll_faces = [int(face) for face in faces if face < rerolL_value]

    return {
        "value": game_value,
        "reroll_faces": reroll_faces
    }

# Step 3 - pay_per_reroll_die_game
def pay_per_reroll_die_game(sides, reroll_cost):
    best_threshold = None
    best_value = float("-inf")

    for t in range(1, sides + 1):
        average_kept_roll = (t + sides) / 2
        reroll_to_keep_ratio = (t - 1) / (sides - t + 1)

        value = average_kept_roll - reroll_to_keep_ratio * reroll_cost

        if value > best_value:
            best_value = value
            best_threshold = t

    return {
        "threshold": best_threshold,
        "value": float(best_value)
    }

# Step 4 - red_black_card_game_value
from functools import lru_cache

def red_black_card_game_value(num_red, num_black):
    @lru_cache(maxsize=None)
    def V(r, b):
        if r == 0:
            return 0.0
        
        if b == 0:
            return float(r)
        
        total = r + b

        cont = (
            (r / total) * (1 + V(r - 1, b))
            +
            (b / total) * (-1 + V(r, b - 1))
        )

        return max(0.0, cont)
    
    r = num_red
    b = num_black

    if r == 0 and b == 0:
        cont = 0.0
    elif r == 0:
        cont = -1 + V(r, b - 1)
    elif b == 0:
        cont = 1 + V(r - 1, b)
    else:
        total = r + b
        cont = (
            (r / total) * (1 + V(r - 1, b))
            +
            (b / total) * (-1 + V(r, b - 1))
        )
    
    value = max(0.0, cont)

    return {
        "value": float(value),
        "stop_now": bool(cont <= 0.0)
    }

# Step 5 - make_quotes
def make_quotes(fair_value, spread_width):
    half_spread = spread_width / 2

    return {
        "bid": fair_value - half_spread,
        "ask": fair_value + half_spread
    }

# Step 6 - execute_trade
def execute_trade(state, side, bid, ask, size=1):
    cash = state["cash"]
    inventory = state["inventory"]

    if side == "buy":
        new_cash = cash + size * ask
        new_inventory = inventory - size
    
    elif side == "sell":
        new_cash = cash - size * bid
        new_inventory = inventory + size

    return {
        "cash": float(new_cash),
        "inventory": float(new_inventory)
    }

# Step 7 - mark_to_market_pnl (not yet solved)
# TODO: implement

# Step 8 - adverse_selection_loss (not yet solved)
# TODO: implement

# Step 9 - uncertainty_spread (not yet solved)
# TODO: implement

# Step 10 - inventory_skewed_quotes (not yet solved)
# TODO: implement

# Step 11 - update_fair_value_from_trade (not yet solved)
# TODO: implement

# Step 12 - update_remaining_card_value (not yet solved)
# TODO: implement

# Step 13 - run_market_making_episode (not yet solved)
# TODO: implement

# Step 14 - summarize_episode_pnls (not yet solved)
# TODO: implement

