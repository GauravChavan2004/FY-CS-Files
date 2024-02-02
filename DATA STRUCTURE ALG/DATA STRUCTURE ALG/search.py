#Programs to find a pattern in a given string - general way and brute force technique.
#string - general way and brute force

# Searching algorithm


def search(pat, txt):
	M = len(pat)
	N = len(txt)

	# A loop to slide pat[] one by one */
	for i in range(N - M + 1):
		j = 0

		# For current index i, check
		# for pattern match */
		while(j < M):
			if (txt[i + j] != pat[j]):
				break
			j += 1

		if (j == M):
			print("Pattern found at index ", i)



txt = "AABAACAADAABAAABAA"
pat = "AABA"	
	
search(pat, txt)


