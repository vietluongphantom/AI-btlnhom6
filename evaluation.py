evaluate = {
    ' ':           [[0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0]],
    'p':           [[100, 50, 10, 5, 0, 5, 5, 0],
                    [100, 50, 10, 5, 0, -5, 10, 0],
                    [100, 50, 20, 10, 0, -10, 10, 0],
                    [100, 50, 30, 25, 20, 0, -20, 0],
                    [100, 50, 30, 25, 20, 0, -20, 0],
                    [100, 50, 20, 10, 0, -10, 10, 0],
                    [100, 50, 10, 5, 0, -5, 10, 0],
                    [100, 50, 10, 5, 0, 5, 5, 0]],
    'n':             [[-50, -40, -30, -30, -30, -30, -40, -50],
                      [-40, -20, 5, 0, 5, 0, -20, -40],
                      [-30, 0, 10, 15, 15, 10, 0, -30],
                      [-30, 5, 15, 20, 20, 15, 0, -30],
                      [-30, 5, 15, 20, 20, 15, 0, -30],
                      [-30, 0, 10, 15, 15, 10, 0, -30],
                      [-40, -20, 5, 0, 5, 0, -20, -40],
                      [-50, -40, -30, -30, -30, -30, -40, -50]],
    'b':             [[-20, -10, -10, -10, -10, -10, -10, -20],
                      [-10, 0, 0, 5, 0, 10, 5, -10],
                      [-10, 0, 5, 5, 10, 10, 0, -10],
                      [-10, 0, 10, 10, 10, 10, 0, -10],
                      [-10, 0, 10, 10, 10, 10, 0, -10],
                      [-10, 0, 5, 5, 10, 10, 0, -10],
                      [-10, 0, 0, 5, 0, 10, 5, -10],
                      [-20, -10, -10, -10, -10, -10, -10, -20]],
    'r':           [[0, 5, -5, -5, -5, -5, -5, 0],
                    [0, 10, 0, 0, 0, 0, 0, 0],
                    [0, 10, 0, 0, 0, 0, 0, 0],
                    [0, 10, 0, 0, 0, 0, 0, 5],
                    [0, 10, 0, 0, 0, 0, 0, 5],
                    [0, 10, 0, 0, 0, 0, 0, 0],
                    [0, 10, 0, 0, 0, 0, 0, 0],
                    [0, 5, -5, -5, -5, -5, -5, 0]],
    'q':            [[-20, -10, -10, -5, 0, -10, -10, -20],
                     [-10, 0, 0, 0, 0, 5, 0, -10],
                     [-10, 0, 5, 5, 5, 5, 5, -10],
                     [-5, 0, 5, 5, 5, 5, 0, -5],
                     [-5, 0, 5, 5, 5, 5, 0, -5],
                     [-10, 0, 5, 5, 5, 5, 0, -10],
                     [-10, 0, 0, 0, 0, 0, 0, -10],
                     [-20, -10, -10, -5, -5, -10, -10, -20]],
    'k': {
        'early':         [[-30, -30, -30, -30, -20, -10, 20, 20],
                          [-40, -40, -40, -40, -30, -20, 20, 30],
                          [-40, -40, -40, -40, -30, -20, 0, 10],
                          [-50, -50, -50, -50, -40, -20, 0, 0],
                          [-50, -50, -50, -50, -40, -20, 0, 0],
                          [-40, -40, -40, -40, -30, -20, 0, 10],
                          [-40, -40, -40, -40, -30, -20, 20, 30],
                          [-30, -30, -30, -30, -20, -10, 20, 20]],
        'late':         [[-50, -30, -30, -30, -30, -30, -30, -50],
                         [-40, -20, -10, -10, -10, -10, -30, -30],
                         [-30, -10, 20, 30, 30, 20, 0, -30],
                         [-20, 0, 30, 40, 40, 30, 0, -30],
                         [-20, 0, 30, 40, 40, 30, 0, -30],
                         [-30, -10, 20, 30, 30, 20, 0, -30],
                         [-40, -20, -10, -10, -10, -10, -30, -30],
                         [-50, -30, -30, -30, -30, -30, -30, -50]]
    },
    'P':           [[0, -5, -5, 0, -5, -10, -50, -100],
                    [0, -10, 5, 0, -5, -10, -50, -100],
                    [0, -10, 10, 0, -10, -20, -50, -100],
                    [0, 20, 0, -20, -25, -30, -50, -100],
                    [0, 20, 0, -20, -25, -30, -50, -100],
                    [0, -10, 10, 0, -10, -20, -50, -100],
                    [0, -10, 5, 0, -5, -10, -50, -100],
                    [0, -5, -5, 0, -5, -10, -50, -100]],
    'N':             [[50, 40, 30, 30, 30, 30, 40, 50],
                      [40, 20, 0, -5, 0, -5, 20, 40],
                      [30, 0, -10, -15, -15, -10, 0, 30],
                      [30, 0, -15, -20, -20, -15, -5, 30],
                      [30, 0, -15, -20, -20, -15, -5, 30],
                      [30, 0, -10, -15, -15, -10, 0, 30],
                      [40, 20, 0, -5, 0, -5, 20, 40],
                      [50, 40, 30, 30, 30, 30, 40, 50]],
    'B':             [[20, 10, 10, 10, 10, 10, 10, 20],
                      [10, -5, -10, 0, -5, 0, 0, 10],
                      [10, 0, -10, -10, -5, -5, 0, 10],
                      [10, 0, -10, -10, -10, -10, 0, 10],
                      [10, 0, -10, -10, -10, -10, 0, 10],
                      [10, 0, -10, -10, -5, -5, 0, 10],
                      [10, -5, -10, 0, -5, 0, 0, 10],
                      [20, 10, 10, 10, 10, 10, 10, 20]],
    'R':           [[0, 5, 5, 5, 5, 5, -5, 0],
                    [0, 0, 0, 0, 0, 0, -10, 0],
                    [0, 0, 0, 0, 0, 0, -10, 0],
                    [-5, 0, 0, 0, 0, 0, -10, 0],
                    [-5, 0, 0, 0, 0, 0, -10, 0],
                    [0, 0, 0, 0, 0, 0, -10, 0],
                    [0, 0, 0, 0, 0, 0, -10, 0],
                    [0, 5, 5, 5, 5, 5, -5, 0]],
    'Q':            [[20, 10, 10, 0, 5, 10, 10, 20],
                     [10, 0, -5, 0, 0, 0, 0, 10],
                     [10, -5, -5, -5, -5, -5, 0, 10],
                     [5, 0, -5, -5, -5, -5, 0, 5],
                     [5, 0, -5, -5, -5, -5, 0, 5],
                     [10, 0, -5, -5, -5, -5, 0, 10],
                     [10, 0, 0, 0, 0, 0, 0, 10],
                     [20, 10, 10, 5, 5, 10, 10, 20]],
    'K': {
        'early' :        [[-20, -20, 10, 20, 30, 30, 30, 30],
                          [-30, -20, 20, 30, 40, 40, 40, 40],
                          [-10, 0, 20, 30, 40, 40, 40, 40],
                          [0, 0, 20, 40, 50, 50, 50, 50],
                          [0, 0, 20, 40, 50, 50, 50, 50],
                          [-10, 0, 20, 30, 40, 40, 40, 40],
                          [-30, -20, 20, 30, 40, 40, 40, 40],
                          [-20, -20, 10, 20, 30, 30, 30, 30]],
        'late' :        [[50, 30, 30, 30, 30, 30, 30, 50],
                         [30, 30, 10, 10, 10, 10, 20, 40],
                         [30, 0, -20, -30, -30, -20, 10, 30],
                         [30, 0, -30, -40, -40, -30, 0, 20],
                         [30, 0, -30, -40, -40, -30, 0, 20],
                         [30, 0, -20, -30, -30, -20, 10, 30],
                         [30, 30, 10, 10, 10, 10, 20, 40],
                         [50, 30, 30, 30, 30, 30, 30, 50]]
    }
}

pieces = {
    ' ': 0,
    'p': 10,
    'n': 30,
    'b': 30,
    'r': 50,
    'q': 90,
    'k': 900,
    'P': -10,
    'N': -30,
    'B': -30,
    'R': -50,
    'Q': -90,
    'K': -900
}

color = {
    ' ': 0,
    'p': 1,
    'n': 1,
    'b': 1,
    'r': 1,
    'q': 1,
    'k': 1,
    'P': -1,
    'N': -1,
    'B': -1,
    'R': -1,
    'Q': -1,
    'K': -1
}