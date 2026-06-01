class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # step 1: edge cases and constraints the box is always 9x9 
        # step 2: constraints > stated 

        # step 3: brute force 
        # loop through every columns and every row and check every 3x3 

        # step 4: solution 
        # create a unique hash set for every single row and column
        # so far time complexity O(1), hash = O(1)

        # 3x3 
        # we create a new index way to track things 
        # the actual value divided by the actual 3
        # hash set same method 

        # create a default dict list for each check 
        # because I use the defaultdict 
        # rows itself is a dictionary where the key is the index 
        # and the value is the actual value 
        rows = defaultdict(set)
        cols = defaultdict(set)
        grid = defaultdict(set)

        # create a for loop that iterates through all of the board positions
        # if you do len(board), it gives you the index and length 
        # but range itself cannot process a 2D list which is board
        for r in range(len(board)): 
            for c in range(len(board)): 
                value = board[r][c]
                if value == ".": 
                    continue
                # have to add the value in and index ie. r
                # or else python just checks if the list are empty
                if value in rows[r] or value in cols[c] or value in grid[(r//3, c//3)]: 
                    return False
                # note append is for lists and add is for sets 
                rows[r].add(value) 
                cols[c].add(value)
                # / is regular division whereas // is integer division
                # always returning the nearest integer 
                # if i do this with the square brackets its telling the key 
                # that its a list and then an index within the list 
                # if i get rid of [] then it creates a couple which is 
                # just list but acts as coordinates 
                # tuples are immutable which is good for dict keys 
                # grid[([r//3][c//3])].add(value)
                grid[(r//3, c//3)].add(value)

        return True 
