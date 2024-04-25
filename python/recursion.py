def recursive_function(n):
    if n == 0:
        return 0
    else:
        print(f"Before recursive call with n={n}")
        result = recursive_function(n - 1)
        print(f"After recursive call with n={n}, result={result}")
        return n + result

result = recursive_function(3)
print("Final result:", result)


if __name__ == "__main__":
    result = ""