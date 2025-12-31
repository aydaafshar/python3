# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_achievement_tracker.py                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ayda <ayda@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/31 13:24:54 by ayda              #+#    #+#              #
#    Updated: 2025/12/31 13:36:17 by ayda             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

print("=== Achievement Tracker System ===")

alice = {"first_kill", "level_10", "treasure_hunter", "speed_demon"}
bob = {"first_kill", "level_10", "boss_slayer", "collector"}
charlie = {
    "level_10",
    "treasure_hunter",
    "boss_slayer",
    "speed_demon",
    "perfectionist"
}

print(f"\nPlayer alice achievements: {alice}")
print(f"Player bob achievements: {bob}")
print(f"Player charlie achievements: {charlie}")

print("\n=== Achievement Analytics ===")

all_achievements = alice.union(bob).union(charlie)
print(f"All unique achievements: {all_achievements}")
print(f"Total unique achievements: {len(all_achievements)}")

common_all = alice.intersection(bob).intersection(charlie)
print(f"\nCommon to all players: {common_all}")

rare = (alice.difference(bob).difference(charlie)
        .union(bob.difference(alice).difference(charlie))
        .union(charlie.difference(bob).difference(alice))
        )
print(f"Rare achievements (1 player): {rare}")

alice_bob_common = alice.intersection(bob)
print(f"\nAlice vs Bob common: {alice_bob_common}")

alice_unique = alice.difference(bob)
print(f"Alice unique: {alice_unique}")

bob_unique = bob.difference(alice)
print(f"Bob unique: {bob_unique}")


