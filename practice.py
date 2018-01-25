# class CategoryTree:
#
#     def __init__(self):
#         self.list1 = []
#
#     def add_category(self, category, parent):
#         dic = {
#             'category': category,
#             'parent': parent
#         }
#         self.list1.append(dic)
#
#     def get_children(self, parent):
#         list2 = []
#         for i in self.list1:
#             try:
#                 if i.get('parent') == parent:
#                     list2.append(i.get('category'))
#             except KeyError as e:
#                 print(e)
#         return list2
#
#
# c = CategoryTree()
# c.add_category('A', None)
# c.add_category('B', 'A')
# c.add_category('C', 'A')
# print(', '.join(c.get_children('A') or []))


