func minEatingSpeed(piles []int, h int) int {
    sort.Ints(piles)
    left := 1 
    right := piles[len(piles)-1]
    smallest := right
    for left <= right {
        mid := (left + right) / 2
        if minEatingSpeedHelper(piles, mid, h) {
            right = mid -1
            smallest = mid
        } else {
            left = mid + 1
        }
    }
    return smallest
}

func minEatingSpeedHelper(piles []int, cur, h int) bool {
    curHours := 0
    for i := 0; i < len(piles); i++ {
        if curHours > h {
            return false
        }
        curHours += int(math.Ceil(float64(piles[i])/float64(cur)))
    }
    return curHours <= h
}
