# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_coordinate_system.py                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ayda <ayda@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/31 12:37:48 by ayda              #+#    #+#              #
#    Updated: 2026/01/01 17:07:23 by ayda             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import math

def distance_3d(p1,p2):
    return math.sqrt(
        (p2[0] - p1[0]) ** 2
        + (p2[1] - p1[1]) ** 2
        + (p2[2] - p1[2]) ** 2
    )

def parse_cordinate(s):
    try:
        parts = s.split(",")
        x = int(parts[0])
        y = int(parts[1])
        z = int(parts[2])
        return (x,y,z)
    except Exception as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")
        return None
    
def main():   
    print("=== Game Coordinate System ===")

    origin = (0 ,0 ,0)

    position = (10, 20, 5)

    if len(sys.argv) >= 2:
        user_pos = parse_cordinate(sys.argv[1])
        if user_pos is not None:
            position = user_pos
            
    print(f"\nPosition created: {position}")
    print(f"Distance between {origin} and {position}: "
          f"{distance_3d(origin, position):.2f}"
          
    )

    print('\nParsing coordinates: "3,4,0"')
    parsed = parse_cordinate("3,4,0")
    if parsed is not None:
        print(f"Parsed position: {parsed}")
        print(
        f"Distance between {origin} and {parsed}: "
        f"{distance_3d(origin, parsed)}"
        )

    print('\nParsing invalid coordinates: "abc,def,ghi"')
    parse_cordinate("abc,def,ghi")

    print("\nUnpacking demonstration:")

    if parsed is not None:
        x, y, z = parsed
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}")

if __name__ == "__main__":
    main()