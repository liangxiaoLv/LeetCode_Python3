class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_nums = nums1+nums2
        new_nums.sort()
        return (new_nums[len(new_nums)//2]+new_nums[(len(new_nums)-1)//2])/2


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        add_lenth = len(nums1) + len(nums2)
        i, j, count, new_list = 0, 0, 0, []
        if nums1 and nums2:
            while count <= ((add_lenth // 2)):
                if i >= len(nums1):
                    new_list.append(nums2[j])
                    j += 1
                    count += 1
                elif j >= len(nums2):
                    new_list.append(nums1[i])
                    i += 1
                    count += 1
                else:
                    if nums1[i] <= nums2[j]:
                        new_list.append(nums1[i])
                        i += 1
                        count += 1
                    else:
                        new_list.append(nums2[j])
                        j += 1
                        count += 1
            return (new_list[add_lenth // 2] + new_list[(add_lenth - 1) // 2]) / 2
        elif nums1:
            return (nums1[len(nums1) // 2] + nums1[(len(nums1) - 1) // 2]) / 2

        elif nums2:
            return (nums2[len(nums2) // 2] + nums2[(len(nums2) - 1) // 2]) / 2