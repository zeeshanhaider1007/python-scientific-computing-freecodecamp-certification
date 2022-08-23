# This entrypoint file to be used in development. Start by reading README.md
from pytest import main
import re
from arithmetic_arranger import arithmetic_arranger

res = arithmetic_arranger(['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True)

expected = '   32         1      45      123      988\n- 698    - 3801    + 43    +  49    +  40\n-----    ------    ----    -----    -----\n -666     -3800      88      172     1028'
# Run unit tests automatically
main(['-vv'])
# print(re.findall("([a-zA-z])","1 - 3o9"))