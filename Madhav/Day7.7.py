#Python program to clone or copy a list
lst=list(map(eval,input("ENTR THE VALUES SPACE SEPARATED: ").split()))
lst2=lst.copy()
print("YOUR REAL LIST ",lst)
print("YOUR COPIED LIST ",lst2)