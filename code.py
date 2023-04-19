# Define a class called Solution

class Solution:
    # Define a method called groupAnagrams that takes a list of strings as input and returns a list of lists of strings
    def groupAnagrams(self, strs):
        # Create an empty dictionary to store the anagrams
        anagram_dict = {}
        
        # Iterate over each word in the input list of strings
        for word in strs:
            # Sort the letters in the word and join them into a string
            sorted_word = ''.join(sorted(word))
            
            # Check if the sorted word already exists as a key in the anagram dictionary
            if sorted_word in anagram_dict:
                # If it does, append the current word to the list of anagrams
                anagram_dict[sorted_word].append(word)
            else:
                # If it doesn't, create a new key with the sorted word and a list with the current word as its value
                anagram_dict[sorted_word] = [word]
        
        # Return a list of the values in the anagram dictionary
        return list(anagram_dict.values())

# Create an instance of the Solution class
ob1 = Solution()

# Call the groupAnagrams method with the example input and print the result
print(ob1.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
