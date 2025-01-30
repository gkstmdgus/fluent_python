# slice 활용
invoice = """
0.....6.................................40.........52...55........
1909  Pimoroni PiBrella                      $17.50    3    $52.50
1489  6mm Tactile Switch x20                  $4.95    2     $9.90
1510  Panavise Jr. -PV-201                   $28.00    1    $28.00
"""

SKU = slice(0,6)
DESCRIPTION = slice(6,40)
UNIT_PRICE = slice(40, 52)
QUANTITY = slice(52, 55)
ITEM_TOTAL = slice(55, None)
line_items = invoice.split('\n')[2:]

for item in line_items:
    print(item[UNIT_PRICE], item[DESCRIPTION])

# slice 할당하기
l = list(range(10))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

l[2:5] = [20, 30]
# [0, 1, 20, 30, 5, 6, 7, 8, 9]

del l[5:7]
# [0, 1, 20, 30, 5, 8, 9]

l[3::2] = [11, 22]
# [0, 1, 20, 11, 5, 22, 9]

# l[2:5] = 100
l[2:5] = [100]
# [0, 1, 100, 22, 9]
