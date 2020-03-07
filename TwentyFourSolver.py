#!/usr/bin/env python3

class TwentyFourSolver:
    def __init__(self,s,target=24):
        self.permutation_list = []
        self.s = s
        self.target = target
        self.ans = set()
    def solver(self,nums,i=0,res=0,path='',pre_val=0):
#         print(i,res,path,pre_val)
        if i == len(self.s):
            if res == self.target:
                self.ans.add(path)
            return
        cur_str = str(nums[i])
        cur_val = nums[i]
        self.solver(nums,i+1,res+cur_val,path+'+'+ cur_str,cur_val)
        self.solver(nums,i+1,res-cur_val,path+'-'+ cur_str,-cur_val)
        if i > 0:
            self.solver(nums,i+1,res-pre_val+pre_val*cur_val,path+'*'+cur_str,cur_val*pre_val)
            self.solver(nums,i+1,res-pre_val+pre_val/cur_val,path+'/'+cur_str,cur_val*pre_val)
    def permutation(self,i,res):
        if i == len(self.s):
            self.permutation_list.append(res)
            return
        cur = nums[i]
        for pos in range(len(res)):
            if res[pos]==None:
                res[pos] = cur
                self.permutation(i+1,res.copy())
                res[pos] = None
    def solve(self):
        self.permutation(0,[None]*len(self.s))

        for nums in self.permutation_list:
            self.solver(nums)
        return self.ans
    
nums = [8,11,13,6]
sol = TwentyFourSolver(nums)
solution = sol.solve()
print(solution)
