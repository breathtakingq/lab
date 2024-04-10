Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ege1 = "Математика — 78, Информатика — 75, Русский язык — 62"
>>> subjects=['Информатика','информатика','Физика','ФИЗИКА']
>>> def get_tested(ege1,subjects):
	ege=ege1.lower()
	subject=subjects.lower()
	False if ege.find(subject)==-1 else True

	
>>> for k in range(len(subjects)):
	if get_tested(ege1,subjects[k]):
		print('ЕГЭ по дисциплине', subjects[k],'- сдан')
	else:
		print('ЕГЭ по дисциплине', subjects[k],'- не сдан')

		
ЕГЭ по дисциплине Информатика - не сдан
ЕГЭ по дисциплине информатика - не сдан
ЕГЭ по дисциплине Физика - не сдан
ЕГЭ по дисциплине ФИЗИКА - не сдан
>>> 