def feet_to_steps(user_feet):
    steps = int(user_feet / 2.5)
    return steps

def main():
    user_feet = float(input())
    steps = feet_to_steps(user_feet)
    print(steps)

if __name__ == "__main__":
    main()