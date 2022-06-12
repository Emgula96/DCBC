


movies = [('star wars', 1980),('gone with the wind', 1960), ('toy story', 2001), ('buglife', 2004), ('harry potter', 2018), ('glue', 2000), ('raiders', 1986), ('prince of egypt', 1990) ]

# gmovies = [title for title in movies if title.startswith('p')]
# print(gmovies)

# sub = [(title, year) for (title, year) in movies if year > 2000]

# print(sub)

# v = [2,-3,1]
# w = [4*x for x in v]
# print(w)

Apple = [1,3,5,7]
Bath= [2,4,6,8]

cartProd = [(a,b) for a in Apple for b in Bath]
    
Apple = [1,3,5,7]
Bath= [2,4,6,8]   





    #             def twoSum(nums, target):
    # for i in range(len(nums)):
    #     for j in range(i+1,len(nums)):
    #         result = nums[i]+nums[j]
    #         if result == target:
    #             return [i,j]
    # return []