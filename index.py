def lengthOfLongestSubstring(s):
    lengthOfSubstring = len(s)
    result = 0
    for i in range(0, lengthOfSubstring):
        for j in range(i, lengthOfSubstring):
            if(isUnique(s, i, j)):
                result = max(result, j - i)

    return result

def isUnique(s, start, end):
    setOfStrings = set()
    for i in range(start, end):
        character = s[i]
        if(character in setOfStrings):
            return False
        setOfStrings.add(character)

    return True

if __name__ == '__main__':
    stringInput = "pwwkew"
    print(f"Input value: {stringInput}")

    answerForLength = lengthOfLongestSubstring(stringInput)
    print(f"The length of the longest substring without repeating characters is {answerForLength}")
