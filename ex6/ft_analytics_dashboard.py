def main():
    players = {
        "alice": {
            "score": 2300,
            "active": True,
            "region": "north",
            "achievements": ["first_kill", "level_10", "kkk",
                             "speed_demon", "pvp_win"],
        },
        "bob": {
            "score": 1800,
            "active": True,
            "region": "east",
            "achievements": ["first_kill", "level_10", "boss_slayer"],
        },
        "charlie": {
            "score": 2150,
            "active": True,
            "region": "central",
            "achievements": [
                "level_10",
                "treasure_hunter",
                "boss_slayer",
                "speed_demon",
                "perfectionist",
                "combo_master",
                "no_damage",
            ],
        },
        "diana": {
            "score": 2050,
            "active": False,
            "region": "north",
            "achievements": ["jj", "hh"],
        },
    }

    print("=== Game Analytics Dashboard ===")

    print("\n=== List Comprehension Examples ===")

    high_score = [name for name,
                  data in players.items() if data["score"] > 2000]

    scores_doubled = [data["score"] * 2 for data in players.values()]

    active_players = [name for name, data in players.items() if data["active"]]

    print("High scorers (>2000):", high_score)
    print("Scores doubled:", scores_doubled)
    print("Active players:", active_players)

    print("\n=== Dict Comprehension Examples ===")

    player_scores = {
        name: data["score"] for name, data in players.items() if data["active"]
    }

    high = 0
    medium = 0
    low = 0

    for data in players.values():
        if data["score"] >= 2050:
            high += 1
        elif data["score"] > 1800:
            medium += 1
        else:
            low += 1

    score_categories = {"high": high, "medium": medium, "low": low}

    achievement_counts = {
        name: len(data["achievements"])
        for name, data in players.items()
        if data["active"]
    }

    print("Player scores:", player_scores)
    print("Score categories:", score_categories)
    print("Achievement counts:", achievement_counts)

    print("\n=== Set Comprehension Examples ===")

    unique_players = {name for name in players.keys()}

    unique_achievements = {
        it
        for data in players.values()
        if data["active"] and data["score"] < 2000
        for it in data["achievements"]
    }

    active_regions = {data["region"]
                      for data in players.values() if data["active"]}

    print("Unique players:", unique_players)
    print("Unique achievements:", unique_achievements)
    print("Active regions:", active_regions)

    print("\n=== Combined Analysis ===")

    scores = []
    for data in players.values():
        scores.append(data["score"])
    total_players = len(players)

    all_unique_achievements = set()
    for data in players.values():
        for ach in data["achievements"]:
            all_unique_achievements.add(ach)
    total_unique_achievements = len(all_unique_achievements)

    if total_players:
        average_score = sum(scores) / total_players
    else:
        average_score = 0

    top_name = None
    top_score = None

    for name, data in players.items():
        if top_name is None or data["score"] > top_score:
            top_score = data["score"]
            top_name = name

    top_achievements = len(players[top_name]["achievements"])

    print("Total players:", total_players)
    print("Total unique achievements:", total_unique_achievements)
    print("Average score:", average_score)
    print(
        f"Top performer: {top_name} ({top_score} points,"
        f" {top_achievements} achievements)"
    )


if __name__ == "__main__":
    main()
