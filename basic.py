# -*- coding: utf-8 -*-


'''
	Из книги Лутц - конспект

			Основы функций
	
			def является исполняемым кодом. Функции Python пишутся с помощью нового оператора def. 
		В отличие от функций в компилируемых языках, таких как С, def представляет собой исполняемый 
		оператор — ваша функция не существует до тех пор, пока Python не встретит и не выполнит def.

		Оператор def в Python является подлинным исполняемым оператором: при выполнении он создает 
		новый объект функции и присваивает его имени. (Помните, что в Python мы имеем лишь исполняющую 
		среду; понятие отдельного времени компиляции не существует.)

		global - объявляет переменные уровня модуля, предназначенные для присваивания.
			Чтобы присвоить значение имени из включающего модуля, необходимо указать его в операторе global внутри функции

	Вообще говоря, в Python мы пишем код для интерфейсов объектов, а не для типов данных1.
'''

def intersect(seq1, seq2):
	res = []
	for x in seq1:
		if x in seq2:
			res.append(x)
	return res

s1 = "SPAM"
s2 = "SCAM"
x = []
x = intersect([1, 2, 3], (1, 4))
print x
'''
	# ПЕРЕЧИТАТЬ

	Вообще говоря, в Python мы пишем код для интерфейсов объектов, а не для типов данных1.
Разумеется, определенные программы имеют уникальные требования, и суть такой полиморфной модели программирования
в том, что мы обязаны тестировать свой код с целью выявления ошибок, а не предоставлять компилятору объявления типов, 
которые он сможет использовать для обнаружения специфических разновидностей ошибок заблаговременно. Тем не менее, в
обмен на небольшое первоначальное тестирование мы получаем радикальное сокращение объема кода, который приходится писать,
и весомое увеличение гибкости результирующего кода. Как вы увидите, на практике это означает чистый выигрыш.

Контрольные вопросы
	1.
	В чем смысл написания функций?
	2.
	В какой момент Python создает функцию?
	3.
	Что функция возвращает, если в ней нет ни одного оператора return?
	4.
	Когда выполняется код, вложенный внутрь оператора определения функции?

Проверьте свои знания: ответы
	1.
	Функции — это наиболее базовый способ избегания избыточности кода в Python — вынесение кода в функции означает наличие только одной копии кода операции, 
	который возможно придется обновлять в будущем. Функции также являются базовой единицей многократного использования кода в Python — помещение кода в функции
	 делает его многократно применяемым инструментом, допускающим вызов в разнообразных программах. Наконец, функции позволяют разбивать сложную систему на
	  поддающиеся управлению части, каждая из которых может разрабатываться по отдельности.
	2.
	Функция создается, когда Python достигает оператора def; данный оператор создает объект функции и присваивает его имени функции. Обычно это происходит 
	при импортировании файла модуля, содержащего def, другим модулем (вспомните, что импортирование приводит к выполнению кода в файле от начала до конца, 
	включая любые операторы def), но может также случаться, когда def набирается в интерактивной подсказке или вкладывается в другие операторы, такие как if.
	3.
	По умолчанию функция возвращает объект None, если поток управления добрался до конца тела функции, не встретив ни одного оператора return. Такие функции
	 обычно вызываются посредством операторов выражений, поскольку присваивание переменным их результатов None в целом бессмысленно. Оператор return без 
	 выражения в нем также возвращает None.
	4.
	Тело функции (код, вложенный внутрь оператора определения функции) выполняется, когда функция впоследствии вызывается с помощью выражения вызова. 
	При каждом вызове функции ее тело выполняется заново.

'''

