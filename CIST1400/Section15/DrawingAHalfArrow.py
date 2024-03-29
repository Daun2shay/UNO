arrow_base_height = int(input())
arrow_base_width = int(input())
arrow_head_width = int(input())
while arrow_head_width <= arrow_base_width:
    arrow_head_width = int(input())
print('', end='')

for base_height in range(arrow_base_height):
  for base_width in range(arrow_base_width):
    print('*', end='')
  print(''  , end='')

for head_width in range(arrow_head_width):
  for head in range(arrow_head_width - head_width):
    print('*', end='')
print('', end='')