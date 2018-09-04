def zaokrozi(matrika):
    for v in range(len(matrika)):
        for s in range(len(matrika[0])):
            matrika[v][s] = round(matrika[v][s], 2)
    return matrika
            

print(zaokrozi([[0.1,0.22222],[-1,-0.888]]))
