anim = {"Gato Montes":2, "Yacare overo":4, "Boa acuática":5}
for i in anim:
	print(i[:anim[i]] + "_" + i[anim[i]+1:])
