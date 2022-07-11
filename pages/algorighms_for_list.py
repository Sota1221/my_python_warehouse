import streamlit as st

st.markdown("# List Algorithms")

st.markdown("## Prefix Sum")
st.markdown("先頭から特定インデックスまでの和を返す`prefixsum`リストを作ります。")
code = """
def get_prefixsum(nums):
    prefix_sum = nums[:]
    for i in range(i, len(nums)):
        prefix_sum[i] += prefix_sum[i-1]
    return prefix_sum
"""
st.code(code, language="python")
st.markdown("または、")
code = """
def get_prefixsum(nums):
    return list(accumulate(nums))
"""
st.code(code, language="python")

st.markdown("#### Related Problems")
st.markdown("* [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/description/)")


st.markdown("## Boyer-Moore Voting Algorithm")
st.markdown("過半数を占める要素を探索します。\n以下ではnumsに過半数を占める要素が存在するとします。")
code = """
def get_majority(self, nums):
        candidate = nums[0]
        cnt = 1
        for n in nums[1:]:
            if cnt == 0:
                candidate = n
            if n == candidate:
                cnt += 1
            else:
                cnt -= 1
        return candidate
"""
st.code(code, language="python")
st.markdown("#### Related Problems")
st.markdown("* [169. Majority Element](https://leetcode.com/problems/majority-element/)")


st.markdown("## Quick Select")
st.markdown("k番目に小さい要素を探索します。\nここでは「k番目に小さい要素」=「昇順に並べたリストのインデックスkの要素」とします。")
code = """
def partition(l, r, pivot_idx):
    nums[r], nums[pivot_idx] = nums[pivot_idx], nums[r]
    store_idx = l
    for i in range(l, r):
        if nums[i] < nums[r]:
            nums[store_idx], nums[i] = nums[i], nums[store_idx]
            store_idx += 1
    nums[r], nums[store_idx] = nums[store_idx], nums[r]
    return store_idx

def select(l, r, k):
    pivot_idx = random.randint(l, r)
    pivot_idx = partition(l, r, pivot_idx)
    if pivot_idx == k:
        return nums[pivot_idx]
    elif pivot_idx < k:
        return select(pivot_idx+1, r, k)
    else:
        return select(l, pivot_idx-1, k)

select(0, len(nums)-1, k)
"""
st.code(code, language="python")
st.markdown("#### Related Problems")
st.markdown("* [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)")