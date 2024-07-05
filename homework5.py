immutable_var = (1, 2, "rok", True)
print("Immutable tuple:",immutable_var)
#immutable_var нельзя изменить так как картеж является неизменяемым обьектом (изменить можно только в случае если один из элементов картежа список
# ( можно изменять отдельные элементы), при умножении картежа (т.е t = (1, 2) * 2), при сложении (t = (1, 2) + (3, 4)))
mutable_list = [1, 2, "rok", True]
mutable_list[0] = "mMm"
print("Mutable list:",mutable_list)