space_str = "  \t\n\r"
print(space_str.isspace())

alnum_str = "sjdkhj333"
print(alnum_str.isalnum())

alpha_str = "sdhajkd"
print(alpha_str.isalpha())

title_str = "Time True"
print(title_str.istitle())
title_str = "Time TRUE"
print(title_str.istitle())

# 判断字符串是否是小写字母

lower_str = "time true"
print(lower_str.islower())