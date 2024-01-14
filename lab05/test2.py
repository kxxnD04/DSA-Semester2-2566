def swap(word: str, ans="", found=False):
    for char in word:
        if not found and char in 'aeiou':
            ans += char.upper() if char.islower() else char.lower()
            found = True
        else:
            ans += char
    return ans
print(" ".join(list(map(swap, input().split()))))
