# Challenge source https://www.hackerrank.com/challenges/crush/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

def arrayManipulation(n, queries):
    l = [0 for i in range(n)]
    for q in queries:
        l[q[0]-1] += q[2]
        if q[1] < len(l):
            l[q[1]] -= q[2]
    return max(itertools.accumulate([l[i] for i in range(len(l))]))
