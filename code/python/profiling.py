# https://docs.python.org/3/library/profile.html

import cProfile

# with cProfile.Profile() as pr:
#     print("blah")
#     x = 2
#     for i in range(28):
#         x *= x

# pr.print_stats()


p = cProfile.Profile()

p.enable()
print("blah")
p.disable()

p.enable()
print("blah")
p.disable()
p.print_stats()



###

# ex from above link:
# import cProfile, pstats, io
# from pstats import SortKey
# pr = cProfile.Profile()
# pr.enable()
# # ... do something ...
# pr.disable()
# s = io.StringIO()
# sortby = SortKey.CUMULATIVE
# ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
# ps.print_stats()
# print(s.getvalue())