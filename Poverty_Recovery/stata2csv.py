from pandas.io.stata import StataReader, StataWriter

filename_all = "CHIP2013_rural_household_f_income_asset.dta"

# stata_data = StataReader(filename_all, convert_categoricals=False, encoding='utf-8')
# stata_data = StataReader(filename_all, encoding='utf8')
stata_data = StataReader(filename_all)
print(stata_data)


# varlist = stata_data.varlist
#
#
# value_labels = stata_data.value_labels()
#
# fmtlist = stata_data.fmtlist
#
# variable_labels = stata_data.variable_labels()
#
# print(data)
# print(varlist)
# print(value_labels)
# print(fmtlist)
# print(variable_labels)
#
#
# writer = StataWriter(fname='mytest_1.dta', data=data,  variable_labels=variable_labels)
# writer.write_file()

# 注意：
    # 在写入的时候
    # 没有value_labels这个选项
    # variable_labels选项数据必须是latin-1的字符集，否则报错
    # 并且不能encoding=‘utf-8’
    # 但是2.7这些都有， 但3.5已经封装程statawriter， 而2.7里面是df.to_stata
