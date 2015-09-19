nums = map(int, raw_input().split())
ans = []
for i in xrange(5):
    for j in xrange(i + 1, 5):
        for k in xrange(j + 1, 5):
            ans.append(nums[i] + nums[j] + nums[k])
print sorted(ans)[-3]
