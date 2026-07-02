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

# Step 3 - pay_per_reroll_die_game (not yet solved)
# TODO: implement

# Step 4 - red_black_card_game_value (not yet solved)
# TODO: implement

# Step 5 - make_quotes (not yet solved)
# TODO: implement

# Step 6 - execute_trade (not yet solved)
# TODO: implement

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

