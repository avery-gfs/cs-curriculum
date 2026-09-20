nums = [5, 3, 2, 5, 1, 4, 1]


def render(index):
    print("---\n\n```")
    print(" ".join(str(n) for n in nums))
    print(" " * (2 * index) + "^ ^")
    print("```\n")


for end in range(len(nums) - 1, 0, -1):
    for index in range(end):
        render(index)

        if nums[index] > nums[index + 1]:
            tmp = nums[index]
            nums[index] = nums[index + 1]
            nums[index + 1] = tmp
            render(index)
