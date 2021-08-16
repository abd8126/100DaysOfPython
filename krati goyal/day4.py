import random
urmove=input()
moves=['rock','scissor','paper']
moves.remove(urmove)
comove=random.choice(moves)
print(comove)
if urmove=='rock' and comove=='scissor':
    print('rock wins')
elif urmove=='paper' and comove=='rock':
    print('paper wins')  
elif urmove=='paper' and comove=='scissor':
    print('scissor wins')      
