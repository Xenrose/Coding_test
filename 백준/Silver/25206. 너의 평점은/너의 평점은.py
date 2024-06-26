score = []
grad = []
grad_dict = {'A+':4.5, 'A0':4.0,
             'B+':3.5, 'B0':3.0,
             'C+':2.5, 'C0':2.0,
             'D+':1.5, 'D0':1.0,
             'F':0.0}

for i in range(20):
    _, score_, grad_ = input().split()
    if grad_=='P': continue

    score_ = float(score_)
    score.append(score_ * grad_dict[grad_])
    grad.append(score_)

print(round(sum(score)/sum(grad),6))