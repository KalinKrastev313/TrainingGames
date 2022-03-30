import time
row = ["-"] * 8
n = 0
row[n] = "O"
run = True
while run:
    print(row)
    row[n] = "-"
    n += 1
    row[n] = "O"
    time.sleep(1)