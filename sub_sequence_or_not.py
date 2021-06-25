def is_subseq(b,v):
    iteration = iter(v)
    return all(any(c == ch for c in iteration) for ch in b)
v = "coronavirus"#input()
b="c"#input()
if is_subseq(b,v):
    print("b is subsequence of v")
else:
    print("b is not a subsequence of v")