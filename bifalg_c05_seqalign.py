# -*- coding: utf-8 -*-
"""
Filename: bifalg_05_seqalign.py
Date created: Fri Nov  6 12:35:18 2026
@author: LioHong710
Purpose:
Steps:
    1.
    2.
    3.

"""
# BA5A: Find the Minimum Number of Coins Needed to Make Change
def _convert_dp_change1(money, coins):
    # From textbook pseudo-code.
    minnum_coins = {0:0}
    # Mod: End-value is money+1 instead of money.
    for m in range(1,money+1):
        # Initialise as infinitely larger value.
        minnum_coins[m] = 2047
        for i in range(len(coins)):
            ci = coins[i]
            # Always true once m > coins[0].
            if m >= ci:
                new_mnc = minnum_coins[m - ci] + 1
                # Will progressively lower minnum_coins[m].
                if new_mnc < minnum_coins[m]:
                    minnum_coins[m] = new_mnc
    return minnum_coins[money]


def _convert_dp_change2(money, coins):
    # Mod: Reduce dict length to at most the value of largest coin denom.
    # Otherwise dict will always follow length of money's value.
    # Observe that after money = 11, output increments for every 5 values of money.
    # So only the last 5 values are needed.
    minnum_coins = {0:0}
    for m in range(1,money+1):
        minnum_coins[m] = 2047
        for i in range(len(coins)):
            ci = coins[i]
            if m >= ci:
                new_mnc = minnum_coins[m - ci] + coins[-1]
                if new_mnc < minnum_coins[m]:
                    minnum_coins[m] = new_mnc
        # Rolling window.
        if m >= coins[0]:
            del minnum_coins[m - coins[0]]
    return minnum_coins[money]


def _convert_dp_change3(money, coins):
    # Mod: Return types of coins.
    # Doesn't work. Tried to mod minnum_coins.
    minnum_coins = {0:[]}
    for m in range(1,money+1):
        minnum_coins[m] = [coins[0] for i in range(money//coins[0] + 2)]
        for i in range(len(coins)):
            ci = coins[i]
            if m >= ci:
                print(m)
                print(ci)
                new_mnc = minnum_coins[m - ci].copy()
                new_mnc.append(coins[-1])
                print(new_mnc)
                if sum(new_mnc) == m:
                    minnum_coins[m] = new_mnc
        if m >= coins[0]:
            del minnum_coins[m - coins[0]]
    return minnum_coins[money]


def _convert_dp_change4(money, coins):
    # Mod: Return types of coins.
    # Build on minnum_coins instead of replacing it.
    # For some reason, mnc_in_change doesn't update for small values of money.
    minnum_coins = {0:0}
    mnc_in_change = {0:[]}
    for m in range(1,money+1):
        minnum_coins[m] = 2047
        # # Minimum upper bound, but additional calc. It also creates undefined behaviour in the inequality condition.
        # minnum_coins[m] = money//coins[0] + 2
        for i in range(len(coins)):
            ci = coins[i]
            if m >= ci:
                new_mnc = minnum_coins[m - ci] + coins[-1]
                if new_mnc < minnum_coins[m]:
                    minnum_coins[m] = new_mnc
                    mnc_in_change[m] = mnc_in_change[m - ci].copy()
                    mnc_in_change[m].append(ci)
        if m >= coins[0]:
            del minnum_coins[m - coins[0]]
            del mnc_in_change[m - coins[0]]
    return mnc_in_change[money]

# roman = [5,4,1]
# _convert_dp_change4(76, roman)
# _convert_dp_change2(8074,[24,13,12,7,5,3,1])
# _convert_dp_change4(8074,[24,13,12,7,5,3,1])


# BA5B: Find the Length of a Longest Path in a Manhattan-like Grid
def _tour_manhattan1(n, m, down, right):
    # From textbook pseudo-code.
    # Assume source node is s_0,0. Sink node is s_n,m.
    # down is a matrix of n rows x m+1 columns. Reverse of x,y-notation.
    # right is a matrix of n+1 rows x m columns.
    # Wrong: IndexError.
    nodes = [[0 for b in range(m+1)] for a in range(n+1)]
    for i in range(1,n+1):
        nodes[i][0] = nodes[i-1][0] + down[i][0]
    for j in range(1,m+1):
        nodes[0][j] = nodes[0][j-1] + right[0][j]
    for i in range(1,n+1):
        for j in range(1,m+1):
            nodes[i][j] = max(nodes[i-1][j] + down[i][j], nodes[i][j-1] + right[i][j])
    return nodes[n][m]


def _tour_manhattan2(n, m, down, right):
    # Attempted fix.
    nodes = [[0 for b in range(m+1)] for a in range(n+1)]
    for i in range(n):
        nodes[i+1][0] = nodes[i][0] + down[i][0]
    for j in range(m):
        nodes[0][j+1] = nodes[0][j] + right[0][j]
    for i in range(1,n+1):
        for j in range(1,m+1):
            nodes[i][j] = max(nodes[i-1][j] + down[i-1][j], nodes[i][j-1] + right[i][j-1])
    return nodes[n][m]


def _tour_manhattan3(n, m, down, right):
    # Fixing the code so it works as intended.
    # Main difference is decrementing the indices for down and right.
    nodes = [[0 for b in range(m+1)] for a in range(n+1)]
    for i in range(1,n+1):
        nodes[i][0] = nodes[i-1][0] + down[i-1][0]
    for j in range(1,m+1):
        nodes[0][j] = nodes[0][j-1] + right[0][j-1]
    for i in range(1,n+1):
        for j in range(1,m+1):
            nodes[i][j] = max(nodes[i-1][j] + down[i-1][j], nodes[i][j-1] + right[i][j-1])
    return nodes[n][m]


# def _tour_manhattan4(n, m, down, right):
#     # Follow topological ordering on p250 Fig 5.16.
#     # topo = [[0,0],[1,0],[0,1]]
#     nodes = [[0 for b in range(m+1)] for a in range(n+1)]
#     for i in range(1,n+1):
#         nodes[i][0] = nodes[i-1][0] + down[i-1][0]
#     for j in range(1,m+1):
#         nodes[0][j] = nodes[0][j-1] + right[0][j-1]
#     for i in range(1,n+1):
#         for j in range(1,m+1):
#             nodes[i][j] = max(nodes[i-1][j] + down[i-1][j], nodes[i][j-1] + right[i][j-1])
#     return nodes[n][m]

# down = [[1, 0, 2, 4, 3], [4, 6, 5, 2, 1], [4, 4, 5, 2, 1], [5, 6, 8, 5, 3]]
# right = [[3, 2, 4, 0], [3, 2, 4, 2], [0, 7, 3, 3], [3, 3, 0, 2], [1, 3, 2, 2]]
# _tour_manhattan3(4, 4, down, right)
# dd = [[0,2,2,2,4,4,3,4,0,0,0,4,0,2,3,1,3], [1,4,0,1,3,3,0,2,3,0,1,3,2,2,2,1,4], [0,3,1,3,2,3,0,2,0,2,4,2,2,1,2,0,3], [4,1,4,3,4,3,1,4,0,4,1,3,0,3,3,0,2], [4,3,3,0,1,0,4,3,1,1,2,4,1,1,4,1,2], [3,0,3,3,2,0,3,3,0,0,4,4,2,0,2,3,3], [0,2,3,4,1,2,0,3,4,0,2,3,3,4,0,1,3], [3,4,2,3,4,2,2,4,0,4,3,3,0,2,3,0,3], [2,2,2,0,4,4,0,2,1,1,0,2,1,4,4,4,0], [0,0,0,2,2,3,0,3,3,0,2,0,0,1,0,4,4], [1,4,2,1,1,3,0,0,4,0,0,3,4,0,3,2,1], [4,3,3,3,2,1,2,1,1,1,1,1,3,2,4,3,2], [4,2,2,0,0,3,4,0,0,1,4,2,0,4,1,3,4], [1,1,4,3,4,2,4,4,1,3,3,4,0,4,3,2,3], [4,2,0,0,0,3,2,0,3,1,3,0,3,1,1,0,1], [0,2,3,4,0,3,2,4,0,2,0,1,0,0,0,4,4], [3,2,3,0,4,3,1,1,2,4,4,3,3,4,3,0,3], [2,0,3,2,0,2,3,3,4,4,1,2,1,4,2,3,3]]
# rr = [[2,4,3,3,1,1,4,3,2,2,3,4,1,3,2,2], [3,3,0,3,0,2,0,0,3,4,0,4,1,3,0,3], [2,0,1,2,1,2,4,4,2,1,1,4,0,4,2,4], [1,4,2,3,1,2,4,0,1,2,3,1,2,0,2,0], [3,0,4,1,1,3,1,4,3,2,0,2,2,1,4,0], [4,4,1,2,2,2,2,3,3,3,4,1,1,3,0,4], [0,3,1,2,4,1,0,4,4,3,2,3,0,3,0,3], [1,0,0,4,1,0,0,1,3,2,2,2,4,0,3,0], [4,1,2,1,3,0,2,4,2,2,2,2,3,4,3,4], [2,3,3,2,3,3,2,0,1,3,1,1,2,2,0,4], [0,0,3,4,0,4,0,2,3,4,3,1,0,1,3,0], [4,2,3,3,1,4,4,4,0,0,2,0,4,2,4,0], [2,3,0,4,1,4,0,2,3,0,2,3,4,1,3,2], [1,1,4,4,0,3,2,2,4,1,0,0,3,3,2,0], [3,0,2,2,2,3,3,3,4,0,0,0,3,3,4,0], [1,0,1,0,0,1,0,1,1,1,0,1,3,1,0,2], [3,3,2,3,0,3,4,3,1,4,0,3,2,3,4,0], [3,1,3,0,0,3,1,1,1,4,1,0,2,0,2,3], [4,1,2,2,4,3,1,0,0,3,4,3,1,1,0,0]]
# _tour_manhattan3(18, 16, dd, rr)


# BA5C: Find a Longest Common Subsequence of Two Strings: 1224 
def backtrack_for_longcommon_subseq(string1, string2):
    # Each entry in the matrix represents the backtracking pointer of a node.
    # First row and first column have no pointers.
    # I think this is the Needleman-Wunsch algorithm.
    nodes = [[0 for w in range(len(string2)+1)] for v in range(len(string1)+1)]
    backtrack = [[0 for w in range(len(string2)+1)] for v in range(len(string1)+1)]
    for i in range(1,len(string1)+1):
        for j in range(1,len(string2)+1):
            # Find value of the node.
            # Max over 3 values and 1 condition.
            nodes[i][j] = max(nodes[i-1][j], nodes[i][j-1])
            if string1[i-1] == string2[j-1]:
                nodes[i][j] = max(nodes[i][j], nodes[i-1][j-1] + 1)
            
            # Find the backtracking pointer of the node.
            if nodes[i][j] == nodes[i-1][j]:
                # backtrack[i][j] = 'down'
                backtrack[i][j] = '↓'
            elif nodes[i][j] == nodes[i][j-1]:
                # backtrack[i][j] = 'right'
                backtrack[i][j] = '→'
            elif nodes[i][j] == nodes[i-1][j-1]+1 and string1[i-1] == string2[j-1]:
                # backtrack[i][j] = 'downright'
                backtrack[i][j] = '↳'
    return backtrack


def output_lcs(backtrack, string1, i, j):
    # Assumes that will not go beyond the length of string1.
    v = string1
    if not i or not j:
        return ''
    # if backtrack[i][j] == 'down':
    if backtrack[i][j] == '↓':
        return output_lcs(backtrack, v, i-1, j)
    # elif backtrack[i][j] == 'right':
    elif backtrack[i][j] == '→':
        return output_lcs(backtrack, v, i, j-1)
    else:
        # print(str(i) + ',' + str(j))
        # Backtrack is offset by 1 from input strings.
        return output_lcs(backtrack, v, i-1, j-1) + v[i-1]
    

def show_backtrack(string1, string2):
    backtrack = backtrack_for_longcommon_subseq(string1, string2)
    # Header row.
    backtrack.insert(0, [0,0] + [ss for ss in string2])
    # Second row.
    backtrack[1].insert(0,0)
    # Header column.
    for s in range(len(string1)):
        backtrack[s+2].insert(0,string1[s])
    print(backtrack)
    

def find_lcs(string1, string2):
    backtrack = backtrack_for_longcommon_subseq(string1, string2)
    return output_lcs(backtrack, string1, len(string1), len(string2))

# Answer is AACTGG but my function returns AACTTG. Maybe because answer uses affine gap.
# Worked on extra dataset and test dataset which are too long to show here.
# find_lcs('AACCTTGG','ACACTGTGA')


# BA5D: Find the Longest Path in a DAG: 869
def find_longest_path(source, sink, graph):
    # Find all the nodes in the graph.
    # Sometimes had to remove incoming edge to source node.
    graph = [e for e in graph if e.split('->')[1].split(':')[0] != str(source)]
    nodes_ordered = order_graph_topologically(graph)
    s = {n:-255 for n in nodes_ordered}
    # Assume that the source node is the only node with indegree 0.
    s[str(source)] = 0
    edges_max = []
    
    # Source node has no incoming edges. Second node should have source node as predecessor.
    for b in nodes_ordered:
        edges_incoming = [e for e in graph if e.split('->')[1].split(':')[0] == b]
        values = [s[e.split('->')[0]] + int(e.split(':')[1]) for e in edges_incoming]
        if len(values):
            s[b] = max(values)
        indices = [i for i,v in enumerate(values) if v == max(values)]
        for i in indices:
            edges_max.append(edges_incoming[i])

    # Find a longest path.
    predecessor = str(sink)
    path_longest = [predecessor]
    while predecessor != str(source):
        plist = [e for e in edges_max if e.split('->')[1].split(':')[0] == predecessor]
        # Choose one path.
        predecessor = plist[0].split('->')[0]
        path_longest.append(predecessor)
    
    # predecessor = str(sink)
    # pds = [e for e in edges_max if e.split('->')[1].split(':')[0] == predecessor]
    
    return s[str(sink)], '->'.join(path_longest[::-1])

# find_longest_path(0,4,['0->1:7', '0->2:4', '2->3:2', '1->4:1', '3->4:3'])
# find_longest_path(0,44,['6->26:32', '10->39:30', '26->28:24', '3->16:19', '10->35:35', '10->37:19', '10->31:36', '10->33:32', '10->32:4', '15->23:0', '15->21:0', '22->24:0', '22->27:31', '1->3:36', '5->43:37', '8->30:23', '19->34:11', '12->13:38', '39->40:35', '12->15:29', '27->29:13', '1->42:31', '24->25:2', '1->10:4', '4->30:11', '13->35:17', '24->28:2', '23->25:37', '31->43:7', '31->40:17', '3->28:2', '5->12:39', '5->11:37', '3->4:4', '2->31:23', '14->29:13', '19->27:21', '27->36:20', '31->33:23', '30->40:27', '28->42:29', '21->35:33', '21->37:5', '20->37:24', '2->9:38', '0->14:19', '4->20:0', '1->41:8', '8->14:28', '19->20:13', '4->43:3', '14->31:25', '14->30:22', '13->41:19', '13->40:32', '14->35:10', '10->11:5', '14->38:23', '2->23:9', '2->25:1', '24->40:37', '12->38:38', '20->23:34', '20->21:29', '12->30:10', '12->37:12', '29->44:30', '33->35:15', '33->37:22', '0->36:8', '37->38:17', '10->29:13', '17->44:11', '6->14:5', '10->22:8', '22->37:19', '22->34:3', '32->43:4', '15->36:28', '11->35:20', '2->16:27', '7->10:22', '11->31:19', '16->41:24', '15->30:25', '32->37:29', '0->27:9', '0->28:7', '32->38:0', '12->43:5', '22->35:37', '24->30:7', '24->32:19', '24->38:38'])


# BA5E: Find a Highest-Scoring Alignment of Two Strings: 1175
blosum = {'A':{'A':4,'C':0,'D':-2,'E':-1,'F':-2,'G':0,'H':-2,'I':-1,'K':-1,'L':-1,'M':-1,'N':-2,'P':-1,'Q':-1,'R':-1,'S':1,'T':0,'V':0,'W':-3,'Y':-2},
          'C':{'A':0,'C':9,'D':-3,'E':-4,'F':-2,'G':-3,'H':-3,'I':-1,'K':-3,'L':-1,'M':-1,'N':-3,'P':-3,'Q':-3,'R':-3,'S':-1,'T':-1,'V':-1,'W':-2,'Y':-2},
          'D':{'A':-2,'C':-3,'D':6,'E':2,'F':-3,'G':-1,'H':-1,'I':-3,'K':-1,'L':-4,'M':-3,'N':1,'P':-1,'Q':0,'R':-2,'S':0,'T':-1,'V':-3,'W':-4,'Y':-3},
          'E':{'A':-1,'C':-4,'D':2,'E':5,'F':-3,'G':-2,'H':0,'I':-3,'K':1,'L':-3,'M':-2,'N':0,'P':-1,'Q':2,'R':0,'S':0,'T':-1,'V':-2,'W':-3,'Y':-2},
          'F':{'A':-2,'C':-2,'D':-3,'E':-3,'F':6,'G':-3,'H':-1,'I':0,'K':-3,'L':0,'M':0,'N':-3,'P':-4,'Q':-3,'R':-3,'S':-2,'T':-2,'V':-1,'W':1,'Y':3},
          'G':{'A':0,'C':-3,'D':-1,'E':-2,'F':-3,'G':6,'H':-2,'I':-4,'K':-2,'L':-4,'M':-3,'N':0,'P':-2,'Q':-2,'R':-2,'S':0,'T':-2,'V':-3,'W':-2,'Y':-3},
          'H':{'A':-2,'C':-3,'D':-1,'E':0,'F':-1,'G':-2,'H':8,'I':-3,'K':-1,'L':-3,'M':-2,'N':1,'P':-2,'Q':0,'R':0,'S':-1,'T':-2,'V':-3,'W':-2,'Y':2},
          'I':{'A':-1,'C':-1,'D':-3,'E':-3,'F':0,'G':-4,'H':-3,'I':4,'K':-3,'L':2,'M':1,'N':-3,'P':-3,'Q':-3,'R':-3,'S':-2,'T':-1,'V':3,'W':-3,'Y':-1},
          'K':{'A':-1,'C':-3,'D':-1,'E':1,'F':-3,'G':-2,'H':-1,'I':-3,'K':5,'L':-2,'M':-1,'N':0,'P':-1,'Q':1,'R':2,'S':0,'T':-1,'V':-2,'W':-3,'Y':-2},
          'L':{'A':-1,'C':-1,'D':-4,'E':-3,'F':0,'G':-4,'H':-3,'I':2,'K':-2,'L':4,'M':2,'N':-3,'P':-3,'Q':-2,'R':-2,'S':-2,'T':-1,'V':1,'W':-2,'Y':-1},
          'M':{'A':-1,'C':-1,'D':-3,'E':-2,'F':0,'G':-3,'H':-2,'I':1,'K':-1,'L':2,'M':5,'N':-2,'P':-2,'Q':0,'R':-1,'S':-1,'T':-1,'V':1,'W':-1,'Y':-1},
          'N':{'A':-2,'C':-3,'D':1,'E':0,'F':-3,'G':0,'H':1,'I':-3,'K':0,'L':-3,'M':-2,'N':6,'P':-2,'Q':0,'R':0,'S':1,'T':0,'V':-3,'W':-4,'Y':-2},
          'P':{'A':-1,'C':-3,'D':-1,'E':-1,'F':-4,'G':-2,'H':-2,'I':-3,'K':-1,'L':-3,'M':-2,'N':-2,'P':7,'Q':-1,'R':-2,'S':-1,'T':-1,'V':-2,'W':-4,'Y':-3},
          'Q':{'A':-1,'C':-3,'D':0,'E':2,'F':-3,'G':-2,'H':0,'I':-3,'K':1,'L':-2,'M':0,'N':0,'P':-1,'Q':5,'R':1,'S':0,'T':-1,'V':-2,'W':-2,'Y':-1},
          'R':{'A':-1,'C':-3,'D':-2,'E':0,'F':-3,'G':-2,'H':0,'I':-3,'K':2,'L':-2,'M':-1,'N':0,'P':-2,'Q':1,'R':5,'S':-1,'T':-1,'V':-3,'W':-3,'Y':-2},
          'S':{'A':1,'C':-1,'D':0,'E':0,'F':-2,'G':0,'H':-1,'I':-2,'K':0,'L':-2,'M':-1,'N':1,'P':-1,'Q':0,'R':-1,'S':4,'T':1,'V':-2,'W':-3,'Y':-2},
          'T':{'A':0,'C':-1,'D':-1,'E':-1,'F':-2,'G':-2,'H':-2,'I':-1,'K':-1,'L':-1,'M':-1,'N':0,'P':-1,'Q':-1,'R':-1,'S':1,'T':5,'V':0,'W':-2,'Y':-2},
          'V':{'A':0,'C':-1,'D':-3,'E':-2,'F':-1,'G':-3,'H':-3,'I':3,'K':-2,'L':1,'M':1,'N':-3,'P':-2,'Q':-2,'R':-3,'S':-2,'T':0,'V':4,'W':-3,'Y':-1},
          'W':{'A':-3,'C':-2,'D':-4,'E':-3,'F':1,'G':-2,'H':-2,'I':-3,'K':-3,'L':-2,'M':-1,'N':-4,'P':-4,'Q':-2,'R':-3,'S':-3,'T':-2,'V':-3,'W':11,'Y':2},
          'Y':{'A':-2,'C':-2,'D':-3,'E':-2,'F':3,'G':-3,'H':2,'I':-1,'K':-2,'L':-1,'M':-1,'N':-2,'P':-3,'Q':-1,'R':-2,'S':-2,'T':-2,'V':-1,'W':2,'Y':7}}
nt_simple = {'A':{'A':1,'C':-1,'T':-1,'G':-1},
             'C':{'A':-1,'C':1,'T':-1,'G':-1},
             'T':{'A':-1,'C':-1,'T':1,'G':-1},
             'G':{'A':-1,'C':-1,'T':-1,'G':1}}
def backtrack_for_global_alignment(string1, string2, seqtype='protein'):
    # Mod of 5C LCS.
    indel_penalty = 5
    nodes = [[0 for w in range(len(string2)+1)] for v in range(len(string1)+1)]
    backtrack = [[0 for w in range(len(string2)+1)] for v in range(len(string1)+1)]
    # Set first column and row according to indel penalty.
    # This solved everything by penalising large gaps.
    nodes[0] = [-5*j for j in range(len(nodes[0]))]
    backtrack[0] = ['→'*min(1,j) for j in range(len(backtrack[0]))]
    for i in range(1,len(string1)+1):
        nodes[i][0] = -5*i
        backtrack[i][0] = '↓'
        for j in range(1,len(string2)+1):
            # aa_match = blosum_rosalind[br_key.find(string1[i-1])][br_key.find(string2[j-1])]
            if seqtype == 'protein':
                match = blosum[string1[i-1]][string2[j-1]]
            # For extra dataset.
            elif seqtype == 'dna':
                match = nt_simple[string1[i-1]][string2[j-1]]
            nodes[i][j] = max(nodes[i-1][j] - indel_penalty, 
                              nodes[i][j-1] - indel_penalty,
                              nodes[i-1][j-1] + match)
            
            # Find the backtracking pointer of the node.
            if nodes[i][j] == nodes[i-1][j]-indel_penalty:
                backtrack[i][j] = '↓'
            elif nodes[i][j] == nodes[i][j-1]-indel_penalty:
                backtrack[i][j] = '→'
            elif nodes[i][j] == nodes[i-1][j-1]+match:
                backtrack[i][j] = '↳'
    return backtrack, nodes[-1][-1]


def _output_ga(backtrack, string1, i, j):
    v = string1
    # if not i or not j:
    #     return ''
    if not i:
        if backtrack[i][j] == '→':
            return '-'
        else:
            return ''
    if not j:
        return v[i-1]
    if backtrack[i][j] == '↓':
        return output_ga(backtrack, v, i-1, j) + v[i-1]
    elif backtrack[i][j] == '→':
        return output_ga(backtrack, v, i, j-1) + '-'
    else:
        # Backtrack is offset by 1 from input strings.
        return output_ga(backtrack, v, i-1, j-1) + v[i-1]


def _output_ga2(backtrack, string2, i, j):
    w = string2
    if not i:
        return w[j-1]
    if not j:
        if backtrack[i][j] == '↓':
            return '-'
        else:
            return ''
    if backtrack[i][j] == '↓':
        return output_ga2(backtrack, w, i-1, j) + '-'
    elif backtrack[i][j] == '→':
        return output_ga2(backtrack, w, i, j-1) + w[j-1]
    else:
        # Backtrack is offset by 1 from input strings.
        return output_ga2(backtrack, w, i-1, j-1) + w[j-1]


def output_ga(backtrack, string1, i, j):
    # Iterative version.
    v = string1
    string_out = []
    while i or j:
        if backtrack[i][j] == '↓':
            i -= 1 
            string_out.append(v[i])
        elif backtrack[i][j] == '→':
            j -= 1
            string_out.append('-')
        else:
            i -= 1 
            j -= 1
            string_out.append(v[i])
    if not i:
        if backtrack[i][j] == '→':
            string_out.append('-')
    # if not j:
    #     string_out.append(v[i-1])
        
    return ''.join(string_out[::-1])


def output_ga2(backtrack, string2, i, j):
    w = string2
    string_out = []
    while i or j:
        if backtrack[i][j] == '↓':
            i -= 1
            string_out.append('-')
        elif backtrack[i][j] == '→':
            j -= 1
            string_out.append(w[j])
        else:
            i -= 1 
            j -= 1
            string_out.append(w[j])
    if not j:
        if backtrack[i][j] == '↓':
            string_out.append('-')
        
    return ''.join(string_out[::-1])


def show_backtrack_ga(string1, string2):
    backtrack, _ = backtrack_for_global_alignment(string1, string2)
    backtrack.insert(0, [0,0] + [ss for ss in string2])
    backtrack[1].insert(0,0)
    for s in range(len(string1)):
        backtrack[s+2].insert(0,string1[s])
    print(backtrack)
    

def find_ga(string1, string2, seqtype='protein'):
    backtrack, score = backtrack_for_global_alignment(string1, string2, seqtype)
    align_half1 = output_ga(backtrack, string1, len(string1), len(string2))
    align_half2 = output_ga2(backtrack, string2, len(string1), len(string2))
    return score, align_half1, align_half2

# find_ga('PLEASANTLY','MEANLY')
# RecursionError: maximum recursion depth exceeded
# Extra dataset appears to be DNA, but test dataset worked.

# Same score but different alignment as below code. No separate docu, use ? on each function.
# '-ds' for dict, '-ms' for match and mismatch
# Note that `pairwise2` module has been deprecated in favour of `Bio.Align.PairwiseAligner`.
# from Bio import pairwise2
# from Bio.Align import substitution_matrices
# matrix = substitution_matrices.load("BLOSUM62")
# for a in pairwise2.align.globalds(qqqqq, wwwww, matrix, -5, -5):
#     print("{}\n{}\n{}\n\n".format(int(a[2]), a[0], a[1]))


# BA5F: Find a Highest-Scoring Local Alignment of Two Strings: 1024
pam250 = {'A':{'A':2,'C':-2,'D':0,'E':0,'F':-3,'G':1,'H':-1,'I':-1,'K':-1,'L':-2,'M':-1,'N':0,'P':1,'Q':0,'R':-2,'S':1,'T':1,'V':0,'W':-6,'Y':-3},
          'C':{'A':-2,'C':12,'D':-5,'E':-5,'F':-4,'G':-3,'H':-3,'I':-2,'K':-5,'L':-6,'M':-5,'N':-4,'P':-3,'Q':-5,'R':-4,'S':0,'T':-2,'V':-2,'W':-8,'Y':0},
          'D':{'A':0,'C':-5,'D':4,'E':3,'F':-6,'G':1,'H':1,'I':-2,'K':0,'L':-4,'M':-3,'N':2,'P':-1,'Q':2,'R':-1,'S':0,'T':0,'V':-2,'W':-7,'Y':-4},
          'E':{'A':0,'C':-5,'D':3,'E':4,'F':-5,'G':0,'H':1,'I':-2,'K':0,'L':-3,'M':-2,'N':1,'P':-1,'Q':2,'R':-1,'S':0,'T':0,'V':-2,'W':-7,'Y':-4},
          'F':{'A':-3,'C':-4,'D':-6,'E':-5,'F':9,'G':-5,'H':-2,'I':1,'K':-5,'L':2,'M':0,'N':-3,'P':-5,'Q':-5,'R':-4,'S':-3,'T':-3,'V':-1,'W':0,'Y':7},
          'G':{'A':1,'C':-3,'D':1,'E':0,'F':-5,'G':5,'H':-2,'I':-3,'K':-2,'L':-4,'M':-3,'N':0,'P':0,'Q':-1,'R':-3,'S':1,'T':0,'V':-1,'W':-7,'Y':-5},
          'H':{'A':-1,'C':-3,'D':1,'E':1,'F':-2,'G':-2,'H':6,'I':-2,'K':0,'L':-2,'M':-2,'N':2,'P':0,'Q':3,'R':2,'S':-1,'T':-1,'V':-2,'W':-3,'Y':0},
          'I':{'A':-1,'C':-2,'D':-2,'E':-2,'F':1,'G':-3,'H':-2,'I':5,'K':-2,'L':2,'M':2,'N':-2,'P':-2,'Q':-2,'R':-2,'S':-1,'T':0,'V':4,'W':-5,'Y':-1},
          'K':{'A':-1,'C':-5,'D':0,'E':0,'F':-5,'G':-2,'H':0,'I':-2,'K':5,'L':-3,'M':0,'N':1,'P':-1,'Q':1,'R':3,'S':0,'T':0,'V':-2,'W':-3,'Y':-4},
          'L':{'A':-2,'C':-6,'D':-4,'E':-3,'F':2,'G':-4,'H':-2,'I':2,'K':-3,'L':6,'M':4,'N':-3,'P':-3,'Q':-2,'R':-3,'S':-3,'T':-2,'V':2,'W':-2,'Y':-1},
          'M':{'A':-1,'C':-5,'D':-3,'E':-2,'F':0,'G':-3,'H':-2,'I':2,'K':0,'L':4,'M':6,'N':-2,'P':-2,'Q':-1,'R':0,'S':-2,'T':-1,'V':2,'W':-4,'Y':-2},
          'N':{'A':0,'C':-4,'D':2,'E':1,'F':-3,'G':0,'H':2,'I':-2,'K':1,'L':-3,'M':-2,'N':2,'P':0,'Q':1,'R':0,'S':1,'T':0,'V':-2,'W':-4,'Y':-2},
          'P':{'A':1,'C':-3,'D':-1,'E':-1,'F':-5,'G':0,'H':0,'I':-2,'K':-1,'L':-3,'M':-2,'N':0,'P':6,'Q':0,'R':0,'S':1,'T':0,'V':-1,'W':-6,'Y':-5},
          'Q':{'A':0,'C':-5,'D':2,'E':2,'F':-5,'G':-1,'H':3,'I':-2,'K':1,'L':-2,'M':-1,'N':1,'P':0,'Q':4,'R':1,'S':-1,'T':-1,'V':-2,'W':-5,'Y':-4},
          'R':{'A':-2,'C':-4,'D':-1,'E':-1,'F':-4,'G':-3,'H':2,'I':-2,'K':3,'L':-3,'M':0,'N':0,'P':0,'Q':1,'R':6,'S':0,'T':-1,'V':-2,'W':2,'Y':-4},
          'S':{'A':1,'C':0,'D':0,'E':0,'F':-3,'G':1,'H':-1,'I':-1,'K':0,'L':-3,'M':-2,'N':1,'P':1,'Q':-1,'R':0,'S':2,'T':1,'V':-1,'W':-2,'Y':-3},
          'T':{'A':1,'C':-2,'D':0,'E':0,'F':-3,'G':0,'H':-1,'I':0,'K':0,'L':-2,'M':-1,'N':0,'P':0,'Q':-1,'R':-1,'S':1,'T':3,'V':0,'W':-5,'Y':-3},
          'V':{'A':0,'C':-2,'D':-2,'E':-2,'F':-1,'G':-1,'H':-2,'I':4,'K':-2,'L':2,'M':2,'N':-2,'P':-1,'Q':-2,'R':-2,'S':-1,'T':0,'V':4,'W':-6,'Y':-2},
          'W':{'A':-6,'C':-8,'D':-7,'E':-7,'F':0,'G':-7,'H':-3,'I':-5,'K':-3,'L':-2,'M':-4,'N':-4,'P':-6,'Q':-5,'R':2,'S':-2,'T':-5,'V':-6,'W':17,'Y':0},
          'Y':{'A':-3,'C':0,'D':-4,'E':-4,'F':7,'G':-5,'H':0,'I':-1,'K':-4,'L':-1,'M':-2,'N':-2,'P':-5,'Q':-4,'R':-4,'S':-3,'T':-3,'V':-2,'W':0,'Y':10}}
def backtrack_for_local_alignment(string1, string2, seqtype='protein'):
    # Mod of 5D global alignment.
    indel_penalty = 5
    nodes = [[0 for w in range(len(string2)+1)] for v in range(len(string1)+1)]
    backtrack = [[0 for w in range(len(string2)+1)] for v in range(len(string1)+1)]
    # Set first column and row according to indel penalty.
    nodes[0] = [-5*j for j in range(len(nodes[0]))]
    backtrack[0] = ['→'*min(1,j) for j in range(len(backtrack[0]))]
    for i in range(1,len(string1)+1):
        nodes[i][0] = -5*i
        backtrack[i][0] = '↓'
        for j in range(1,len(string2)+1):
            if seqtype == 'protein':
                # match = blosum[string1[i-1]][string2[j-1]]
                match = pam250[string1[i-1]][string2[j-1]]
            # For extra dataset.
            elif seqtype == 'dna':
                match = nt_simple[string1[i-1]][string2[j-1]]
            nodes[i][j] = max(nodes[i-1][j] - indel_penalty, 
                              nodes[i][j-1] - indel_penalty,
                              nodes[i-1][j-1] + match,
                              nodes[0][0])
            
            # Find the backtracking pointer of the node.
            if nodes[i][j] == nodes[i-1][j]-indel_penalty:
                backtrack[i][j] = '↓'
            elif nodes[i][j] == nodes[i][j-1]-indel_penalty:
                backtrack[i][j] = '→'
            elif nodes[i][j] == nodes[i-1][j-1]+match:
                backtrack[i][j] = '↳'
            elif nodes[i][j] == nodes[0][0]:
                backtrack[i][j] = '>'
    
    # Find max value in nodes.
    rows_max = [max(r) for r in nodes]
    nodes[-1][-1] = max(rows_max)
    # Find coordinates of max(nodes).
    ci_max = [nodes[ri] for ri,rm in enumerate(rows_max) if rm == nodes[-1][-1]]
    indices_max = {nodes.index(c):c.index(n) for c in ci_max for n in c if n == nodes[-1][-1]}
    
    # Ignore multiple local alignments for now.
    k = list(indices_max.keys())[0]
    # Check if indices_max is different from coordinates of sink.
    if k != len(string1) or indices_max[k] != len(string2):
        backtrack[-1][-1] = str(k) + ',' + str(indices_max[k])

    return backtrack, nodes[-1][-1]


def output_la(backtrack, string1, i, j):
    v = string1
    string_out = []
    while i or j:
        if backtrack[i][j] == '↓':
            i -= 1 
            string_out.append(v[i])
        elif backtrack[i][j] == '→':
            j -= 1
            string_out.append('-')
        elif backtrack[i][j] == '↳':
            i -= 1 
            j -= 1
            string_out.append(v[i])
        # Jump back to source.
        elif backtrack[i][j] == '>':
            i = 0
            j = 0
        # Jump from sink to other node.
        else:
            iiiii = int(backtrack[i][j].split(',')[0])
            j = int(backtrack[i][j].split(',')[1])
            i = iiiii
    if not i:
        if backtrack[i][j] == '→':
            string_out.append('-')
        
    return ''.join(string_out[::-1])


def output_la2(backtrack, string2, i, j):
    w = string2
    string_out = []
    while i or j:
        if backtrack[i][j] == '↓':
            i -= 1
            string_out.append('-')
        elif backtrack[i][j] == '→':
            j -= 1
            string_out.append(w[j])
        elif backtrack[i][j] == '↳':
            i -= 1 
            j -= 1
            string_out.append(w[j])
        # Jump back to source.
        elif backtrack[i][j] == '>':
            i = 0
            j = 0
        # Jump from sink to other node.
        else:
            iiiii = int(backtrack[i][j].split(',')[0])
            j = int(backtrack[i][j].split(',')[1])
            i = iiiii
    if not j:
        if backtrack[i][j] == '↓':
            string_out.append('-')
        
    return ''.join(string_out[::-1])


def show_backtrack_la(string1, string2):
    backtrack, _ = backtrack_for_local_alignment(string1, string2)
    backtrack.insert(0, [0,0] + [ss for ss in string2])
    backtrack[1].insert(0,0)
    for s in range(len(string1)):
        backtrack[s+2].insert(0,string1[s])
    print(backtrack)
    

def find_la(string1, string2, seqtype='protein'):
    backtrack, score = backtrack_for_local_alignment(string1, string2, seqtype)
    align_half1 = output_la(backtrack, string1, len(string1), len(string2))
    align_half2 = output_la2(backtrack, string2, len(string1), len(string2))
    return score, align_half1, align_half2

# find_la('MEANLY','PENALTY')
# Again, extra dataset seems to be DNA. Provided alignment doesn't match the score, but my own longer alignment does.

# Same score but different alignment from below code.
# from Bio import pairwise2
# for a in pairwise2.align.localms(s1, s2, 1, -1, -5, -5):
#     print("{}\n{}\n{}\n\n".format(int(a[2]), a[0], a[1]))


# BA5G: Compute the Edit Distance Between Two Strings: 1033
# BA5H: Find a Highest-Scoring Fitting Alignment of Two Strings: 764
# BA5I: Find a Highest-Scoring Overlap Alignment of Two Strings: 628
# BA5J: Align Two Strings Using Affine Gap Penalties: 988
# BA5K: Find a Middle Edge in an Alignment Graph in Linear Space: 518
# BA5L: Align Two Strings Using Linear Space: 449
# BA5M: Find a Highest-Scoring Multiple Sequence Alignment: 518


# BA5N: Find a Topological Ordering of a DAG
def _order_graph_topologically(graph, nodes_missing=[]):
    # Graph is a list of edges, each in format '0->1:7'. From node 0 to node 1.
    # Max num of edges is triangular(len(nodes)).
    def find_candidates(graph_in):
        from_nodes = [edge.split('->')[0] for edge in graph_in]
        to_nodes = [edge.split('->')[1] for edge in graph_in]
        no_in_nodes = [n for n in from_nodes if n not in to_nodes]
        candidates = list(set(no_in_nodes))
        return candidates
    
    nodes_ordered = []
    # Remove the weights since not needed.
    graph_unweighted = [edge.split(':')[0].replace(' ','') for edge in graph]
    candidates = find_candidates(graph_unweighted)

    from_nodes = [edge.split('->')[0] for edge in graph_unweighted]
    to_nodes = [edge.split('->')[1] for edge in graph_unweighted]
    nodes_all = from_nodes + to_nodes
    nodes_all = list(set(nodes_all))
    # Unsafe to modify length of container while iterating over it. Can lead to undefined behaviour.
    while candidates:
        node_a = candidates[0]
        nodes_ordered.append(node_a)
        # candidates.remove(node_a)
        selected_edges = [edge for edge in graph_unweighted if edge.split('->')[0] == node_a]
        for se in selected_edges:
            graph_unweighted.remove(se)
            candidates = find_candidates(graph_unweighted)
            
            # Check if a node is a candidate.
            successor = se.split('->')[1]
            # Account for nodes with no outgoing edges.
            # check = [e for e in graph_unweighted if e.split('->')[1] == successor]
            check = [e for e in graph_unweighted if successor in e]
            # if successor in nodes_missing:
            #     print(successor)
            #     print(check)
            # Apparently it's not safe to add items to a list while iterating through it.
            # if not check:
            #     candidates.append(successor)
            #     print('=====')
            #     print(candidates)
    if len(graph_unweighted):
        return 'The input graph is not a DAG.'
    else:
        delta = [n for n in nodes_all if n not in nodes_ordered]
        if len(delta):
            print(str(len(delta)) + ' nodes have not been ordered.')
            print(delta)            
        # return nodes_ordered


def order_graph_topologically(graph):
    # Graph is a list of edges, each in format '0->1:7'. From node 0 to node 1.
    # Max num of edges is triangular(len(nodes)).
    def find_candidates(graph_in):
        from_nodes = [edge.split('->')[0] for edge in graph_in]
        to_nodes = [edge.split('->')[1] for edge in graph_in]
        no_in_nodes = [n for n in from_nodes if n not in to_nodes]
        candidates = list(set(no_in_nodes))
        return candidates
    
    nodes_ordered = []
    # Remove the weights since not needed.
    graph_unweighted = [edge.split(':')[0].replace(' ','') for edge in graph]
    candidates = find_candidates(graph_unweighted)

    from_nodes = [edge.split('->')[0] for edge in graph_unweighted]
    to_nodes = [edge.split('->')[1] for edge in graph_unweighted]
    nodes_all = from_nodes + to_nodes
    nodes_all = list(set(nodes_all))
    # Unsafe to modify length of container while iterating over it. Can lead to undefined behaviour.
    # Instead, modify elements.
    # https://stackoverflow.com/questions/44864393/modify-a-list-while-iterating
    # https://sqlpey.com/python/python-modify-list-during-iteration/
    others = [n for n in nodes_all if n not in candidates]
    iterables = candidates + others
    for i in range(len(iterables)):
        node_a = iterables[i]
        nodes_ordered.append(node_a)
        selected_edges = [edge for edge in graph_unweighted if edge.split('->')[0] == node_a]
        for se in selected_edges:
            graph_unweighted.remove(se)
            c2 = find_candidates(graph_unweighted)
            
            # Check if a node is a candidate.
            successor = se.split('->')[1]
            # Account for nodes with no outgoing edges.
            check = [e for e in graph_unweighted if e.split('->')[1] == successor]
            if not check:
                c2.append(successor)
                # This prevents duplicate elements.
                c2 = list(set(c2))
            # Modify elements in place.
            c2 = [c for c in c2 if c not in candidates]
            clen = len(candidates)
            for j in range(len(c2)):
                iterables[clen+j] = c2[j]
                candidates.append(c2[j])
                # if c2[j] not in candidates:
                #     # iterables[clen+j] = c2[j]
                #     candidates.append(c2[j])
            # try:
            #     for j in range(len(c2)):
            #         iterables[clen+j] = c2[j]
            #         candidates.append(c2[j])
            # except:
            #     print(candidates)
            #     print(c2)
    
    delta = [n for n in nodes_all if n not in nodes_ordered]
    if len(delta):
        print(str(len(delta)) + '/' + str(len(nodes_all)) + ' nodes have not been ordered.')
        print(delta)
    if len(graph_unweighted):
        print(graph_unweighted)
        return 'The input graph is not a DAG.'
    else:
        return nodes_ordered


def convert_dict_to_edges(edge_dict):
    # For the input of the extra dataset.
    edges = []
    for e in edge_dict:
        for num in edge_dict[e]:
            edges.append(str(e) + '->' + str(num))
    return edges

# order_graph_topologically(['1 -> 2', '2 -> 3', '4 -> 2', '5 -> 3'])