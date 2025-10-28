# task1.py - Simple utilities and examples (>=50 lines)
def greet(name):
    for i in range(5):
        print(f"Hello {name}! iteration {i+1}")

def factorial(n):
    if n < 0:
        return None
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

def primes_up_to(n):
    sieve = [True] * (n+1)
    sieve[0:2] = [False, False]
    for p in range(2, int(n**0.5)+1):
        if sieve[p]:
            for multiple in range(p*p, n+1, p):
                sieve[multiple] = False
    return [i for i, is_prime in enumerate(sieve) if is_prime]

def summarize_numbers(numbers):
    if not numbers:
        return {}
    return {
        "count": len(numbers),
        "sum": sum(numbers),
        "min": min(numbers),
        "max": max(numbers),
        "average": sum(numbers) / len(numbers)
    }

def main():
    greet("Bekzat")
    print("5! =", factorial(5))
    print("Primes up to 30:", primes_up_to(30))
    stats = summarize_numbers([3, 7, 2, 9, 11, 4])
    print("Stats:", stats)

if __name__ == "__main__":
    main()
