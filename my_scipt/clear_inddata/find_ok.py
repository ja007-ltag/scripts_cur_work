address_ok = """
16	01
16	03
16	05
16	07
16	09
16	0B
16	0D
16	0F
16	11
16	13
16	15
16	17
16	19
16	1B
16	1D
16	21
16	23
16	25
16	29
16	2B
16	2D
16	31
16	33
16	35
16	37
16	41
16	43
16	45
16	47
16	49
16	4B
16	4D
16	51
16	53
16	55
16	57
26	01
26	03
26	05
26	07
26	09
26	0B
26	0D
26	0F
26	11
26	13
26	15
26	17
26	21
26	23
26	25
26	27
26	29
26	2B
26	2D
26	2F
26	31
26	33
26	35
26	37
26	39
26	3B
26	3D
26	3F
26	41
26	43
26	45
26	47
26	49
26	4B
26	4D
26	4F
26	51
26	53
26	55
26	57
26	61
26	63
26	65
26	67
26	69
26	6B
26	6D
26	6F
26	71
26	73
26	75
26	77
26	79
26	7B
26	7D
26	7F
26	81
26	83
26	85
26	87
26	89
26	8B
26	8D
26	8F
26	91
26	93
26	95
26	97
36	01
36	03
36	05
36	07
36	09
36	0B
36	0D
36	0F
36	11
36	13
36	15
36	17
36	19
36	1B
36	1D
36	1F
46	21
46	23
46	25
46	27
46	29
46	2B
46	2D
46	2F
76	01
76	03
76	05
76	11
76	13
76	15
76	17
66	01
66	03
66	05
66	07
66	09
66	0B
66	0D
66	11
66	13
66	15

"""

address_ok = [''.join(line.split('\t')) for line in address_ok.split('\n') if line]
print(len(address_ok))
address_ok = '|'.join(address_ok)
# print(address_ok)

find_ok = f'  (Controller)((?:(?!Controller).)*)(0X({address_ok}))(.*?)(?=(  Controller|    Converter))'
print(find_ok)
