for(_in range3):
   runs = list[map(int,input.split())]
   strike_rate = (sum(runs) / 60) * 100
   runs_score = (sum(runs) / 60) * 120
   sixes = sum(runs) // 6

print(strike_rate)
print(runs_score)
print(sixes)

