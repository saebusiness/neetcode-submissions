func minEatingSpeed(piles []int, h int) int {
    left := 1 
    right := piles[0]
    for i := 0; i < len(piles); i++ {
        if piles[i] > right {
            right = piles[i]
        }
    }
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

func minEatingSpeedHelper(piles []int, eatingRate, hours int) bool {
    curHours := 0
    for i := 0; i < len(piles); i++ {
        curHours += int(math.Ceil(float64(piles[i])/float64(eatingRate)))
    }
    return curHours <= hours
}
