# class French:
#     def __init__(self, lang):
#         self.lg = lang
#
#     def greeting(self):
#         return f'Bonjour'
#
#
# class English:
#     def __init__(self, lang):
#         self.lg = lang
#
#     def greeting(self):
#         return f'Hello'
#
#
# class Japan:
#     def __init__(self, lang):
#         self.lg = lang
#
#     def greeting(self):
#         return f'Konnichiwa'
#
#
# french = French('French')
# eng = English('Eng')
# jap = Japan("Japan")
#
# print(french.greeting(), eng.greeting(), jap.greeting())
#
#
#
# # class Account:
# #     def __init__(self, login, password, secret_key):
# #         self.login = login
# #         self._password = password
# #         self.__sk = secret_key
# #
# #     def __str__(self):
# #         return f'login {self.login}\n' \
# #                f'pass {self.password}\n' \
# #                f'SK {self.sk}'
# #
# # acc1 = Account(login='root', _password=12345, __secret_key='dkhsfkhdskjhjkkkhk129@')
#
#
#
#
#
#
#
#
#
#
#
#
# # class Junior:
# #     def __init__(self, laptop, salary, prog_lang):
# #         self.laptop = laptop
# #         self.salary = salary
# #         self.prog_lang = prog_lang
# #
# #     def can_copy_paste(self, sourse):
# #         return f'Can copy past from-{sourse}'
# #
# #
# #     def __str__(self):
# #         return f'Laptop: {self.laptop}\n' \
# #                f'Salary: {self.salary}$\n' \
# #                f'Prog_lang: {self.prog_lang}'
# #
# # jun_prog = Junior(laptop=True, salary=350, prog_lang='Python')
# # print(jun_prog)
# # print(jun_prog.can_copy_paste('StackOverFlow'))
# # print('-------------')
# #
# # class Middle(Junior):
# #     def __init__(self, laptop, salary, prog_lang, exipirience):
# #         super().__init__(laptop, salary, prog_lang)
# #         self.exp = exipirience
# #
# #     def can_be_mentor(self):
# #         return f'Can mentor-{jun_prog}'
# #
# #
# #     def __str__(self):
# #         return super(Middle, self).__str__()+f'\nExpiriense-{self.exp}'
# #
# # middle = Middle(laptop=True, salary=1000, exipirience=2.5, prog_lang='Python, PHP')
# # print(middle.can_copy_paste('GitHub'))
# # print(middle.can_be_mentor())
# # print(middle)
# # print('-------------')
# #
# # class Senior(Middle):
# #     def __init__(self, laptop, salary, prog_lang, exipirience, arhive):
# #         super().__init__(laptop, salary, prog_lang, exipirience)
# #         self.arch = arhive
# #
# #     def advaced_skills(self, lang):
# #         if lang == 'Python':
# #             return f'Your are beautiful'
# #         elif lang== 'PHP':
# #             return f'Not bad'
# #         else:
# #             return f'I dont understand you'
# #
# #
# #     def __str__(self):
# #         return super(Senior, self).__str__()+f'\nArchive {self.arch}'
# #
# # senior = Senior(laptop=True,salary=5000,prog_lang='Python, Javascript, PHP',
# #                 exipirience=10,arhive='MVC')
# # print(senior)
# # print(senior.advaced_skills('PHP'))
# #
