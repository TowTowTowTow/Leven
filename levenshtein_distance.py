# text1 = "string"
# text2 = "string"

# data1 = list(text1)
# data2 = list(text2)

# print(data1)
# print(data2)


# def levenshtein():
#     if data1 == data2:
#         print("0")
#     else:
#         print("5")
    
# levenshtein()



# import numpy as np

# def levenshteinDistanceDP(token1, token2):
#     distances = np.zeros((len(token1) + 1, len(token2) + 1))

#     for t1 in range(len(token1) + 1):
#         distances[t1][0] = t1

#     for t2 in range(len(token2) + 1):
#         distances[0][t2] = t2
        
#     printDistances(distances, len(token1), len(token2))
#     return 0

# def printDistances(distances, token1Length, token2Length):
#     for t1 in range(token1Length + 1):
#         for t2 in range(token2Length + 1):
#             print(int(distances[t1][t2]), end=" ")
#         print()
        
# levenshteinDistanceDP("kelm", "hello")


# def levenshtein_distance(s1, s2):
#     len_s1 = len(s1)
#     len_s2 = len(s2)
    
#     # Create a 2D array to store distances
#     distances = [[0] * (len_s2 + 1) for _ in range(len_s1 + 1)]
    
#     # Initialize the first row and column
#     for i in range(len_s1 + 1):
#         distances[i][0] = i
#     for j in range(len_s2 + 1):
#         distances[0][j] = j
    
#     # Fill in the rest of the array using dynamic programming
#     for i in range(1, len_s1 + 1):
#         for j in range(1, len_s2 + 1):
#             cost = 0 if s1[i - 1] == s2[j - 1] else 1
#             distances[i][j] = min(
#                 distances[i - 1][j] + 1,         # Deletion
#                 distances[i][j - 1] + 1,         # Insertion
#                 distances[i - 1][j - 1] + cost   # Substitution or match
#             )
    
#     return distances[len_s1][len_s2]

# # Test the function
# string1 = "kitten"
# string2 = "sitting"
# distance = levenshtein_distance(string1, string2)
# print(f"Levenshtein Distance between '{string1}' and '{string2}': {distance}")

def levenshtein_distance(s1, s2):
    len_s1 = len(s1)
    len_s2 = len(s2)
    
    distances = [[0] * (len_s2 + 1) for _ in range(len_s1 + 1)]
    
    for i in range(len_s1 + 1):
        distances[i][0] = i
    for j in range(len_s2 + 1):
        distances[0][j] = j
    
    for i in range(1, len_s1 + 1):
        for j in range(1, len_s2 + 1):
            if s1[i-1] == s2[j - 1]:
                cost = 0
            else:
                cost = 1
            
            # (this is the way chatgpt wrote it.)
            # cost = 0 if s1[i - 1] == s2[j - 1] else 1 
            # (I rewrote it in the way I know it to verify my understanding and make sure it still works)
            
            distances[i][j] = min(
                distances[i - 1][j] + 1,
                distances[i][j - 1] + 1,
                distances[i - 1][j - 1] + cost
            )
    
    return distances[len_s1][len_s2]

