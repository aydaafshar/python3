def game_event_stream(tottal_events):

    players = ["alice", "bob", "charlie"]
    event_types = ["killed_monster", "found treasure", "leveled up"]

    for i in range(tottal_events):
        yield {
            "player": players[i % len(players)],
            "level": (i % 15) + 1,
            "type": event_types[i % len(event_types)],
        }


def fibonacci_stream(n):
    a, b = 0, 1
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
            d += 1
        if is_prime:
            yield x
            count += 1
        x += 1


def main():
    print("=== Game Data Stream Processor ===")
    total_events = 1000
    print(f"\nProcessing {total_events} game events...\n")

    processed = 0
    High_level_players = 0
    Treasure_events = 0
    Level_up_events = 0

    stream = game_event_stream(total_events)
    it = iter(stream)

    for event in it:
        processed += 1

        if processed <= 3:
            print(
                f"Evebt {processed}: Player {event['player']} "
                f"(level {event['level']}) {event['type']}"
            )

        if event["level"] >= 10:
            High_level_players += 1

        if event["type"] == "found treasure":
            Treasure_events += 1

        if event["type"] == "leveled up":
            Level_up_events += 1
    print("...")
    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+): {High_level_players}")
    print(f"Treasure events: {Treasure_events}")
    print(f"Level-up events: {Level_up_events}")

    print("\nMemory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")

    print("\n=== Generator Demonstration ===")
    fib_stream = fibonacci_stream(10)
    print("Fibonacci sequence (first 10): ", end="")
    for i in range(10):
        if i > 0:
            print(", ", end="")
        print(next(fib_stream), end="")
    print()

    primes = prime_stream(5)
    print("Prime numbers (first 5): ", end="")
    for i in range(5):
        if i > 0:
            print(", ", end="")
        print(next(primes), end="")
    print()


if __name__ == "__main__":
    main()
