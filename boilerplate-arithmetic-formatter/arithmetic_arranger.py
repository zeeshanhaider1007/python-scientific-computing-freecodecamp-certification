import re
def arithmetic_arranger(List, flag=False):
  ## operation type
  printing = dict()
  printing["first_row"] = []
  printing["second_row"] = []
  printing["third_row"] = []
  printing["fourth_row"] = []
  if len(List) > 5:
    return 'Error: Too many problems.'
  for n,arith in  enumerate(List):
    operator = ""
    if "+" in arith:
      operator += "+"
    elif "-" in arith:
      operator += "-"
    else:
      return "Error: Operator must be '+' or '-'."
    numbers = re.findall('([0-9]+)',arith)
    if len(re.findall("([a-zA-z])",arith)) > 0:
      return "Error: Numbers must only contain digits."
    if len(numbers[0])>4 or len(numbers[1])>4:
      return "Error: Numbers cannot be more than four digits."
    if operator=="+":
      answer = str(int(numbers[0]) + int(numbers[1]))
    else:
      answer = str(int(numbers[0]) - int(numbers[1]))
    message = numbers[0]
    fill = ' '
    align = '>'
    if len(numbers[0]) > len(numbers[1]):
      width = len(numbers[0]) + 2
    else:
      width = len(numbers[1]) + 2
    printing["first_row"].append(f'{message:{fill}{align}{width}}')
    message = numbers[1]
    fill = ' '
    align = '>'
    if len(numbers[0]) > len(numbers[1]):
      width = len(numbers[0]) + 1
    else:
      width = len(numbers[1]) + 1
    printing["second_row"].append(f'{operator}{message:{fill}{align}{width}}')
    printing["third_row"].append("-"*len(printing["second_row"][n]))
    message = answer
    fill = ' '
    align = '>'
    width = len(printing["second_row"][n])
    printing["fourth_row"].append(f'{message:{fill}{align}{width}}')
    # print(printing["first_row"][n])
    # print(printing["second_row"][n])
    # print(printing["third_row"][n])
    # print(printing["fourth_row"][n])
  four_spaces = "    "
  if flag:
    all_arithmatics = f"{four_spaces}".join(printing["first_row"])+"\n"+f"{four_spaces}".join(printing["second_row"])+"\n"+f"{four_spaces}".join(printing["third_row"])+"\n"+f"{four_spaces}".join(printing["fourth_row"])
  else:
    all_arithmatics = f"{four_spaces}".join(printing["first_row"])+"\n"+f"{four_spaces}".join(printing["second_row"])+"\n"+f"{four_spaces}".join(printing["third_row"])
  return all_arithmatics