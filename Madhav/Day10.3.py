n=list(map(str,input("ENTER THE WORDS:").split('-')))
n.sort()
n='-'.join(n)
print(f"NEW WORD IS {n}")
