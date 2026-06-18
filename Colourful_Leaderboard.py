N = int(input())
ratings = list(map(int, input().split()))

fixed_colors = set()
pro_players = 0

for r in ratings:
    if 1 <= r <= 399:
        fixed_colors.add("gray")
    elif 400 <= r <= 799:
        fixed_colors.add("brown")
    elif 800 <= r <= 1199:
        fixed_colors.add("green")
    elif 1200 <= r <= 1599:
        fixed_colors.add("cyan")
    elif 1600 <= r <= 1999:
        fixed_colors.add("blue")
    elif 2000 <= r <= 2399:
        fixed_colors.add("yellow")
    elif 2400 <= r <= 2799:
        fixed_colors.add("orange")
    elif 2800 <= r <= 3199:
        fixed_colors.add("red")
    else:
        pro_players += 1

base_colors = len(fixed_colors)
min_colors = max(1, base_colors)
max_colors = base_colors + pro_players

print(min_colors, max_colors)
