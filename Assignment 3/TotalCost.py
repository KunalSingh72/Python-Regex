 #   Q  -- 1+2+3+4+5+6+7 +2+3+4+5+6+7+8 +3+4+5+6+7+8+9 +4+5 = 114
# 23th da
day = int(input("Enter Day : "))
total_cost = 0
for i in range(1,(day//7)+1):
    for j in range(i,i+7):
        total_cost+=j
    if (i == (day//7)):
        for k in range(1, (day%7)+1):
            total_cost += k+i
print(total_cost)