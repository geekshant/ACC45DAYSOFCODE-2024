def can_escape(ghosts, target):
    def manhattan_distance(point1, point2):
        return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
    
    my_distance = manhattan_distance([0, 0], target)
    
    for ghost in ghosts:
        ghost_distance = manhattan_distance(ghost, target)
        if ghost_distance <= my_distance:
            return False
    return True

def main():
    T = int(input("Enter the number of test cases: "))
    results = []
    
    for _ in range(T):
        G = int(input("Enter the number of ghosts: "))
        ghosts = []
        for _ in range(G):
            ghost = list(map(int, input("Enter ghost coordinates: ").split()))
            ghosts.append(ghost)
        target = list(map(int, input("Enter the target coordinates: ").split()))
        results.append(can_escape(ghosts, target))
    
    for result in results:
        print("True" if result else "False")

if __name__ == "__main__":
    main()
