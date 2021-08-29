#!/usr/bin/env python3

from icecream import ic

#ic.disable() # Disable logs

def distribute_load(count, avail_num):
  " Load balancing "
  if avail_num > 0 and count > 0:
    whole = count // avail_num
    modulo = count % avail_num
  else:
    whole = 0
    modulo = 0

  arr = [whole for _ in range(avail_num)]

  if modulo > 0:
    for i in range(modulo):
      arr[i] += 1

  #ic(arr)

  return arr

if __name__ == "__main__":
  # Tests
  arr = (
    [125, 4],
    [33, 0],
    [35, -1],
    [0, 4],
    [1, 5]
  )
  expected_res = (
  [32, 31, 31, 31],
  [],
  [],
  [0, 0, 0, 0],
  [1, 0, 0, 0, 0]
  )

  for i in range(len(arr)):
    res = distribute_load(*arr[i])
    ic(res)
    assert res == expected_res[i]
