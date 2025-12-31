# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_command_quest.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ayda <ayda@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/31 11:08:48 by ayda              #+#    #+#              #
#    Updated: 2025/12/31 11:34:41 by ayda             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

print("=== Command Quest ===")

if len(sys.argv) == 1:
    print("No arguments provided!")
print(f"Program name: {sys.argv[0]}")

if len(sys.argv) > 1:
    print(f"Arguments received: {len(sys.argv) - 1}")
    i=1
    for arg in sys.argv[1:]:
        print(f"Argument {i}: {arg}")
        i +=1
print(f"Total arguments: {len(sys.argv)}")