def lengthOfLongestSubstring(s):
    lengthOfSubstring = len(s)
    result = 0
    for i in range(0, lengthOfSubstring):
        for j in range(i, lengthOfSubstring):
            if(isUnique(s, i, j)):
                result = max(result, j - i + 1)

    return result

def isUnique(s, start, end):
    setOfStrings = set()
    for i in range(start, end):
        character = s[i]
        if(character in setOfStrings):
            return False
        setOfStrings.add(character)
        print(setOfStrings)

    return True

if __name__ == '__main__':
    stringInput = "abcabc"
    print(f"Input value: {stringInput}")

    answerForLength = lengthOfLongestSubstring(stringInput)
    print(f"The length of the longest substring without repeating characters is {answerForLength}")
