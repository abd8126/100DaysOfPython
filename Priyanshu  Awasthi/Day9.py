scores ={"Harry": 81,"Ron": 78,"Hermione": 99, "Draco": 74,"Neville": 62}
for i in scores.keys():
    if scores[i]>90:
        scores[i]="Outstanding"
    elif scores[i]>80:
        scores[i]="Exceeds Expectations"
    elif scores[i]>70:
        scores[i]="Acceptable"
    else:
        scores[i]="Fail work hard "
print(scores)