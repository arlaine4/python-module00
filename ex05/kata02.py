def format_date(t):
    t[0] = f'0{t[0]}' if t[0] < 10 else t[0]
    t[1] = f'0{t[1]}' if t[1] < 10 else t[1]
    t[3] = f'0{t[3]}' if t[3] < 10 else t[3]
    t[4] = f'0{t[4]}' if t[4] < 10 else t[4]
    return t


if __name__ == "__main__":
    t = (3, 30, 2019, 9, 25)
    t = format_date(list(t))
    print(f"{t[3]}/{t[4]}/{t[2]} {t[0]}:{t[1]}")
