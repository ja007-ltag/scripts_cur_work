"""
Для быстрой замены
и генерации одинаковых объектов
"""

s = """
  Component
. ---------
. =====================================================
. || Route | Command || Parameters || Areas | Shared ||
. =====================================================
  ||  YES  |   STP   ||  PT7@EME   ||   1   |   NO   ||
. =====================================================

. ========================
. || Pretest indicators ||
. ========================
  ||                    ||
. ========================

  Main objects

. =======================================================================
. || Object  | Manouevre | Seq. | Approved || Object  | Seq. | Pretest ||
. =======================================================================
  || PT7@EME | M_SW = 3  |  1   |          || PT7@EME |  0   |  P_SWP  ||
  || PT7@EME | M_CC = 3  |  1   |          ||         |      |         ||
. =======================================================================

  Component
. ---------
. =====================================================
. || Route | Command || Parameters || Areas | Shared ||
. =====================================================
  ||  YES  |   STM   ||  PT7@EME   ||   1   |   NO   ||
. =====================================================

. ========================
. || Pretest indicators ||
. ========================
  ||                    ||
. ========================

  Main objects

. =======================================================================
. || Object  | Manouevre | Seq. | Approved || Object  | Seq. | Pretest ||
. =======================================================================
  || PT7@EME | M_SW = 4  |  1   |          || PT7@EME |  0   |  P_SWM  ||
  || PT7@EME | M_CC = 3  |  1   |          ||         |      |         ||
. =======================================================================

  Component
. ---------
. =====================================================
. || Route | Command || Parameters || Areas | Shared ||
. =====================================================
  ||  YES  |  STPZ   ||  PT7@EME   ||   1   |   NO   ||
. =====================================================

. ========================
. || Pretest indicators ||
. ========================
  ||                    ||
. ========================

  Main objects

. =======================================================================
. || Object  | Manouevre | Seq. | Approved || Object  | Seq. | Pretest ||
. =======================================================================
  || PT7@EME | M_ESW = 1 |  1   |          || PT7@EME |  0   | P_ESWP  ||
  || PT7@EME | M_CC = 2  |  1   |          ||         |      |         ||
. =======================================================================

  Component
. ---------
. =====================================================
. || Route | Command || Parameters || Areas | Shared ||
. =====================================================
  ||  YES  |  STMZ   ||  PT7@EME   ||   1   |   NO   ||
. =====================================================

. ========================
. || Pretest indicators ||
. ========================
  ||                    ||
. ========================

  Main objects

. =======================================================================
. || Object  | Manouevre | Seq. | Approved || Object  | Seq. | Pretest ||
. =======================================================================
  || PT7@EME | M_ESW = 2 |  1   |          || PT7@EME |  0   | P_ESWM  ||
  || PT7@EME | M_CC = 2  |  1   |          ||         |      |         ||
. =======================================================================

  Component
. ---------
. =====================================================
. || Route | Command || Parameters || Areas | Shared ||
. =====================================================
  ||  YES  |   STB   ||  PT7@EME   ||   1   |   NO   ||
. =====================================================

. ========================
. || Pretest indicators ||
. ========================
  ||                    ||
. ========================

  Main objects

. =======================================================================
. || Object  | Manouevre | Seq. | Approved || Object  | Seq. | Pretest ||
. =======================================================================
  || PT7@EME | M_BLK = 1 |  1   |          || PT7@EME |  0   |  P_BLK  ||
  || PT7@EME | M_CC = 3  |  1   |          ||         |      |         ||
. =======================================================================

  Component
. ---------
. =====================================================
. || Route | Command || Parameters || Areas | Shared ||
. =====================================================
  ||  YES  |   STR   ||  PT7@EME   ||   1   |   NO   ||
. =====================================================

. ========================
. || Pretest indicators ||
. ========================
  ||                    ||
. ========================

  Main objects

. =======================================================================
. || Object  | Manouevre | Seq. | Approved || Object  | Seq. | Pretest ||
. =======================================================================
  || PT7@EME | M_BLK = 2 |  1   |          || PT7@EME |  0   | P_BLKR  ||
  || PT7@EME | M_CC = 3  |  1   |          ||         |      |         ||
. =======================================================================

"""

# цель замены (что менять в предыдущем тексте в переменной 's')
target_replace = 'PT7'

# list_replace = [f'PT{i}' for i in (14, 16, 18, 20, 22, 24, 26, 28, 30)]
# list_replace = [f'N{i}P' for i in (30, 32, 34, 36, 38)]
list_replace = ['PT9']
print(list_replace)

# генерация регулярных выражений для поиска логический объектов
print(f": ({'|'.join(list_replace)})")

result = (s.strip().replace(target_replace, name) for name in list_replace)
# for name in list_replace:
#     result.append(s.strip().replace('N2P', name))

result = '\n\n  '.join(result)
# print(f'  {result}\n\n')

with open('out_replace.txt', 'w', encoding='utf8') as f:
    f.write(f'  {result}\n\n')
