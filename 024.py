def permutations(digits):
	if len(digits) == 1:
		return [digits]
	else:
		results = []
		for i in range(len(digits)):
			subperms = permutations(digits[:i] + digits[i+1:])
			for s in subperms:
				results.append([digits[i]] + s)
		return results
	
digits = [0,1,2,3,4,5,6,7,8,9]
#digits = [0,1,2,3]
digits = [str(n) for n in digits]

perms = [''.join(p) for p in permutations(digits)]
#print perms

perms.sort()
print perms[999999]