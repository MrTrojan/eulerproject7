print("""
PROGRAMMER : Mr.Trojan
WEBLOG : mrtrojan.blog.ir

CALCUTING STARTED....

""")

multiples_nums = 0
symmetric_nums = set()



for i in range(100,1000):
    for a in range(100,1000):
        multiples_nums = i * a
       # print('{0} * {1} : {2}'.format(i,a,multiples_nums))
        def reverse(number):
            result = ""
            nums = []
            count = len(str(multiples_nums))
            for i in range(0,count):
                nums.append(int(number%10))
                number = number/10
            while nums[0] == 0:
                del(nums[0])
                count -= 1
            for a in range(0,count):
                result += str(nums[a])
            result = int(result)
            return result
        if reverse(multiples_nums) == multiples_nums:
          #  print('gooz')
            symmetric_nums.add(multiples_nums)
symmetric_nums = sorted(symmetric_nums)
symmetric_nums_len = len(symmetric_nums) -1
print('the symmetric numbers is ',symmetric_nums[symmetric_nums_len])
