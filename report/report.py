"""
Для подсчёта часов в отчёте
"""

hours_2023_05 = """
8
2
2
4
6
16
2
38
2
2
50
4
4
6
2
2
4
2
2
"""
hours_2023_06 = """
2
4
10
2
3
1
6
2
8
3
8
6
3
6
2
4
4
32
6
2
4
16
6
2
2
6
2
8
2
2
2
2
"""
hours_2023_07 = """
17
20
6
2
8
2
2
5
2
1
1
3
2
1
2
16
2
2
2
2
2
2
2
72

"""
hours_2023_08 = """
48
2
2
6
2
4
3
1
2
1
1
2
3
1
1
1
2
1
1
1
3
1
7
2
1
3
1
4
12
1
1
8



2
2
2
2
2
2
2
1
2
2
2
2
1
2
2
2
4
4
2
2
2
2
2
2
2
2
4
2
2
9
2
2
2
2
2
2
2
2
2
1
1
1
1
1
2
2
2
4
1
1
1
1
1
1
1
1
1
1
1
1
"""
hours_2023_09 = """
2
2
2
2
5
2
4
2
2
1
4
74
12
4
4
8
6
1
5
2
35
5
"""
hours_2023_10 = """
1
3
2
2
2
2
2
2
4
2
2
4
1
1
1
1
2
2
2
1
1
8
8
6
6
2
2
10
8
4
2
6
2
8
2
2
2
2
4
1
3
4
4
4
4
4
2
1
1
2
6
8
8
"""
hours_2023_11 = """
2
2
4
1
2
5
10
6
4
5
2
2
7
3
4
2
6
4
2
2
2
2
4
2
2
4
2
2
4
2
2
2
2
2
2
2
1
3
2
8
1
7
2
2
2
2
2
2
2
2
8
"""
hours_2023_12 = """
32
8
4
4
2
2
2
2
3
1
4
4
12
8
1
5
2
4
4
8
2
1
4
3
2
1
4
3
1
3
2
38
"""
hours_2024_01 = """
16
12
2
2
56
2
22
16
"""
hours_2024_02 = """
17
2
2
2
1
1
1
2
2
1
2
3
1
3
1
3
4
3
2
4
2
1
2
2
2
2
3
1
8
1
7
4
2
2
3
1
6
2
1
3
3
1
2
2
3
3
1
3
4
2
3
3
2
2
1
1
9
2
2
2
3
1
"""

hours_list = [i for i in dir() if i.startswith('hours')]


def all_hours(s):
    # return sum(int(i) for i in s.split())
    return sum(map(int, s.split()))


print(hours_list)
for cur in hours_list:
    data = cur[6:].replace('_', '.')
    sum_hours = all_hours(locals()[cur])
    print(f'{data}: {sum_hours}')
