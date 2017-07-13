## `Bridge Crossing`
### Problem Statement
A group of four travelers comes to a bridge at night. The bridge can hold the weight of at most only two of the travelers at a time, and it can- not be crossed without using a flashlight.

The travelers have one flashlight among them. Each traveler walks at a different speed: The first can cross the bridge in 1 minute, the second in 2 minutes, the third in 5 minutes, and the fourth takes 10 minutes to cross the bridge. If two travelers cross together, they walk at the speed of the slower traveler.

What is the least amount of time in which all the travelers can cross from one side of the bridge to the other?

## Solution:
This is part of a common group of river crossing puzzles. Its know as the Bridge and Torch problem (sometimes the times assigned to each person are different).

The solution to this version is:

| Move                          | Time |
|-------------------------------|------|
| (1) & (2) Cross with Torch    | 2    |
| (1) Return with Torch         | 1    |
| (5) and (10) Cross with Torch | 10   |
| (2) Returns with Torch        | 2    |
| (1) & (2) Cross with Torch    | 2    |
|                               | 17   |



## `Coins and a Scale`
### Problem Statement
You have eight coins and a two-pan scale. All the coins weigh the same, except for one which is heavier than all the others. The coins are otherwise indistinguishable. You may make no assumptions about how much heavier the heavy coin is. What is the minimum number of weighings needed to be certain of identifying the heavy coin?

### Solution
Begin by dividing the coins into two groups of three, which you put on the scale, and one group of two, which you leave off. If the two sides weigh the same, the heavy coin is in the group of two, and you can find it with one more weighing, for a total of two weighings. On the other hand, if either side of the scale is heavier, the heavy coin must be in that group of three. You can eliminate all the other coins, and place one coin from this group on either side of the scale, leaving the third coin aside. If one side is heavier, it contains the heavy coin; if neither side is heavier, the heavy coin is the one you didn’t place on the scale. This is also a total of two weighings, so you can always find the heavy coin in a group of eight using two weighings.



## `Egg Drop`

### Problem Statement
A tower has 100 floors. You've been given two eggs. The eggs are strong enough that they can be dropped from a particular floor in the tower without breaking. You've been tasked to find the highest floor an egg can be dropped without breaking, in as few drops as possible. If an egg is dropped from above its target floor it will break. If it is dropped from that floor or below, it will be intact and you can test drop the egg again on another floor.

Show algorithmically how you would go about doing this in as few drops as possible. (Your answer should be a number of the fewest drops needed for testing 2 eggs on 100 floors)

### Solution
Start from the 10th floor and go up to floors in multiples of 10.

If first egg breaks, say at 20th floor then you can check all the floors between 11th and 19th with the second egg to see which floor it will not break.

In this case, the worst-case number of drops is 19. If the threshold was 99th floor, then you would have to drop the first egg 10 times and the second egg 9 times in linear fashion.

Best solution: We need to minimize this worst-case number of drops. For that, we need to generalize the problem to have n floors. What would be the step value, for the first egg? Would it still be 10? Suppose we have 200 floors. Would the step value be still 10?

The point to note here is that we are trying to minimize the worst-case number of drops which happens if the threshold is at the highest floors. So, our steps should be of some value which reduces the number of drops of the first egg.

Let's assume we take some step value m initially. If every subsequent step is m-1, then,
>+ `m + (m−1) + (m−2) +.....+1 = n`
>+ `= [m * (m + 1)]/2 = n`

If n =100, then m would be 13.65 which since we can't drop from a decimal of a floor, we actually use 14.

So, the worst case scenario is now when the threshold is in the first 14 floors with number of drops being 14.

Note that this is simply a binary search!
