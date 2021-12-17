def fibb (count): 
  prevs = 0
  sum = 1
  output = [sum]
  countsec = 0
  while (countsec < (count-1)):
    countsec+=1
    sv=sum
    sum=sum+prevs
    prevs=sv 
    output.append(sum)
  return output
numb = int(input())
print(fibb(numb))