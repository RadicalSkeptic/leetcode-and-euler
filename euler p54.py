hand = "8C TS KC 9H 4S 7D 2S 5D 3S AC"

play1=hand.split()[:5]
play2=hand.split()[5:]


if set([a[0] for a in play1])==set(['T','J','Q','K','A']) and len(set([a[1] for a in play1])==1):
    score1=(10,0)