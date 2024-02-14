import lichess.api


def get_user_games_and_moves(lichess_id: str):
    # Get all games for a user
    games = lichess.api.user_games(lichess_id)
    return games
