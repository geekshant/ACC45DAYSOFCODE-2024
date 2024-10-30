def trap(height):
    if not height:
        return 0

    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    water_trapped = 0

    while left < right:
        if height[left] < height[right]:
            left += 1
            left_max = max(left_max, height[left])
            water_trapped += left_max - height[left]
        else:
            right -= 1
            right_max = max(right_max, height[right])
            water_trapped += right_max - height[right]

    return water_trapped

def main():
    # Take input from the user
    elevation_map = list(map(int, input("Enter the elevation map as space-separated integers: ").split()))
    
    # Compute the water trapped
    result = trap(elevation_map)
    
    print(f"Total water trapped is: {result} units")

if __name__ == "__main__":
    main()
