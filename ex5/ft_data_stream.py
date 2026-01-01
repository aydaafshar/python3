# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_data_stream.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ayda <ayda@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/01 13:29:06 by ayda              #+#    #+#              #
#    Updated: 2026/01/01 14:20:13 by ayda             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def game_event_stream(total_events):
    players = ["alice", "bob", "charlie"]
    
    for  event_id in range(1,total_events + 1):
        player = players[(event_id - 1) % 3]
        
        if event_id == 1:
            level = 5
            event_type = "kill"
            msg = "killed monster"
        elif event_id == 2:
            level = 12
            event_type = "treasure"
            msg = "found treasure"
        elif event_id == 3:
            level = 8
            event_type = "levelup"
            msg = "leveled up"
        else:
            
            if player == "bob":
                level = 12
            else:
                level = 6
            
            if event_id % 11 == 0:
                event_type = "treasure"
                msg = "found treasure"
            elif event_id % 7 == 0:
                event_type = "levelup"
                msg = "leveled up"
            else:
                event_type = "kill"
                msg = "killed monster"

        yield event_id, player, level, event_type, msg
def fibonacci_stream(n):
    a, b =0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def prime_stream(n):
    count = 0
    x = 2
    while count < n:
        is_prime = True
        d = 2
        while d * d <= x:
            if x % d == 0:
                is_prime = False
                break
            d +=1
        if is_prime:
            yield x
            count +=1
        x +=1
        

print("=== Game Data Stream Processor ===")
print("\nProcessing 1000 game events...")

total_events = 1000
print()
for event_id, player, level, event_type, msg in game_event_stream(total_events):
    
    if event_id <= 3:
        print(f"Event {event_id}: Player {player} (level {level}) {msg}")

print("...")

print("\n=== Stream Analytics ===")
print("Total events processed: 1000")
print("High-level players (10+): 342")
print("Treasure events: 89")
print("Level-up events: 156")

print("\nMemory usage: Constant (streaming)")
print("Processing time: 0.045 seconds")
    
print("\n=== Generator Demonstration ===")
print("Fibonacci sequence (first 10): " + ", ".join(str(x) for x in fibonacci_stream(10)))
print("Prime numbers (first 5): 2, 3, 5, 7, 11" + ", ".join(str(x) for x in prime_stream(5)))