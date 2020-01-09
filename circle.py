import sys
from tkinter import *
from PyQt4 import QtGui,  QtCore
app=QtGui.QApplication(sys.argv)
root=QtGui.QWidget()
root.setWindowTitle('Задача об окружности')
root.resize(650,170)
root.move(200,100)

class Point():
    def __init__(self, x=1,  y=2):
        self.x = x
        self.y = y

class Circle():
	def __init__(self, centreX=1, centreY=2, r=3):
		self.centre = Point()
		self.centre.x=centreX
		self.centre.y=centreY
		self.r = r

task_label=QtGui.QLabel(root)
task_label.move(10,10)
task_label.setText('Задача:\nДаны два множества точек на плоскости. Найти радиус и центр окружности, проходящеё через n (n>=3) точек \nпервого множества и содержащей строго внутри себя равное число точек первого и второго множеств.')				

label=QtGui.QLabel(root)
label.move(10,70)
label.setText('Введите данные о количестве точек в каждой из групп')																																																				 

entry=QtGui.QLineEdit(root)
entry.move(420,70)
entry.setText('') 

button=QtGui.QPushButton(root)
button.setText('В\nв\nо\nд')
button.move(560,65)
button.resize(30,60)

label2=QtGui.QLabel(root)
label2.move(10,100)
label2.setText('Введите, через какое количество точек должна быть построена окружность')

entry2=QtGui.QLineEdit(root)
entry2.move(420,100)
entry2.setText('')

solution_button=QtGui.QPushButton(root)
solution_button.setText('Р\nе\nш\nе\nн\nи\nе')
solution_button.move(560,150)
solution_button.resize(30,300)
solution_button.hide()# временное сокрытие, для облегчения восприятия интерфейса пользователем

mass_of_entry_M1=[]#создаем массивы для окошек
mass_of_entry_M2=[]

mass_of_data_about_point_M1=[]; #создаем массивы для каждого из множеств
mass_of_data_about_point_M2=[];

circle = Circle()
	
def EnteringCoordinates():
	root.resize(650,500)
	global entry, groupbox, mass_of_entry_M1, mass_of_entry_M2, solution_button
	groupbox.hide() #скрываем групбокс вместе со всем содержимым
	groupbox = QtGui.QGroupBox(root)  #перезаписваем групбокс новым и, причем, пустым
	groupbox.move(30, 150)
	
	n=int(entry.text())
	
	label_M1=QtGui.QLabel(groupbox)
	label_M1.move(40,20)
	label_M1.setText('Множество 1')
	label_M1.hide()

	label_M2=QtGui.QLabel(groupbox)
	label_M2.move(320,20)
	label_M2.setText('Множество 2')
	label_M2.hide()

	label_x_1=QtGui.QLabel(groupbox)
	label_x_1.move(60,30)
	label_x_1.setText('x:')
	label_x_1.hide()

	label_x_2=QtGui.QLabel(groupbox)
	label_x_2.move(340,30)
	label_x_2.setText('x:')
	label_x_2.hide()

	label_y_1=QtGui.QLabel(groupbox)
	label_y_1.move(140,30)
	label_y_1.setText('y:')
	label_y_1.hide()

	label_y_2=QtGui.QLabel(groupbox)
	label_y_2.move(420,30)
	label_y_2.setText('y:')
	label_y_2.hide()
	
	solution_button.show()
	label_M1.show()
	label_M2.show()
	label_x_1.show()
	label_x_2.show()
	label_y_1.show()
	label_y_2.show()
	
	for i in range (1, n+1): #просто нумеруем точки в соответствии с заданным пользователем количеством
		label_of_amount=QtGui.QLabel(groupbox)
		label_of_amount.move(10,10+35*i)
		label_of_amount.setText(str(i)+'.')
		label_of_amount.show()
	
	for i in range (1,n+1):#прорисовываем окошки, в которые пользователь будет вводить координаты	
		data_about_point=Point()  #если мы заполняем объект новыми данными и потом сохраняем в массив, необходимо его создавать заново перед вводом новых данных!!!!
		entryV1=QtGui.QLineEdit(groupbox)
		entryV1.move(40,10+35*i)
		entryV1.resize(50,20)
		entryV1.setText('')
		entryV1.show()
		data_about_point.x=entryV1
		
		entryV2=QtGui.QLineEdit(groupbox)
		entryV2.move(120,10+35*i)
		entryV2.resize(50,20)
		entryV2.setText('')
		entryV2.show()
		data_about_point.y=entryV2
		
		mass_of_entry_M1.append(data_about_point)
		
		data_about_point=Point()
		entryV3=QtGui.QLineEdit(groupbox)
		entryV3.move(320,10+35*i)
		entryV3.resize(50,20)
		entryV3.setText('')
		entryV3.show()
		data_about_point.x=entryV3
		
		entryV4=QtGui.QLineEdit(groupbox)
		entryV4.move(400,10+35*i)
		entryV4.resize(50,20)
		entryV4.setText('')
		entryV4.show()
		data_about_point.y=entryV4
		
		mass_of_entry_M2.append(data_about_point)
	
	groupbox.hide()
	groupbox.show()

def CircleCreating (F, S, T):# на вход подаются точки, по которым строится окружность
	T1=T.x**2-S.x**2+T.y**2-S.y**2 # просто ввведены дополнительные промежуточные выражения, чтобы формулы для вычисления А, В, С не были слишком громоздкими
	T2=(S.x**2-F.x**2+S.y**2-F.y*2)/(F.x-S.x)
	T3=((S.y-F.y)*(S.x-T.x)+(S.y-T.y)*(F.x-S.x))/(F.x-S.x)

	B=(T1-(T2*(S.x-T.x)))/T3 # определяем А и В - коэффициенты в уравнении окружности;
	A=((B*(S.y-F.y))/(F.x-S.x))+T2
	C=-T.x**2-T.y**2-A*T.x-B*T.y

	temp_circle= Circle() #создаем объект окружность
	temp_circle.centre.x=-A/2 #координаты цента окружности, которую создаёт функция по заданным точкам
	temp_circle.centre.y=-B/2

	if (F.x**2+F.y**2+A*F.x+B*F.y+C==S.x**2+S.y**2+A*S.x+B*S.y+C==T.x**2+T.y**2+A*T.x+B*T.y+C==0):
		temp_circle.r=((F.x+A/2)**2+(F.y+B/2)**2)**(1/2)

	return temp_circle # на выходе окружность, постоенная по трём точкам
	
def AmountTest(circle, fullM1, fullM2, st):#считает совпадает ли количество точек 1 и 2 множеств внутри окружности
	kM1=0
	kM2=0
	for q in range(st):
		if (circle.r>(pow((fullM1[q].x-circle.centre.x),2)+pow((fullM1[q].y-circle.centre.y),2))**(1/2)):
			kM1=kM1+1 # считаем количество точек внутри окружности из М1
		if (circle.r>(pow((fullM2[q].x-circle.centre.x),2)+pow((fullM2[q].y-circle.centre.y),2))**(1/2)):
			kM2=kM2+1	# считаем количество точек внутри окружности из М2		 
	return kM1==kM2		
	
def Solution():
	global entry, entry2, mass_of_entry_M1, mass_of_entry_M2, mass_of_data_about_point_M1, mass_of_data_about_point_M2, circle
	n=int(entry.text())
	amount=int(entry2.text())
	
	for i in range(n): #записываем введенные пользователем данные в массивы
		data_about_point=Point()
		data_about_point.x=int(mass_of_entry_M1[i].x.text())
		data_about_point.y=int(mass_of_entry_M1[i].y.text())
		mass_of_data_about_point_M1.append(data_about_point)
		
		data_about_point=Point()
		data_about_point.x=int(mass_of_entry_M2[i].x.text())
		data_about_point.y=int(mass_of_entry_M2[i].y.text())
		mass_of_data_about_point_M2.append(data_about_point)
		
	Itg=0
	for i in range(n):
		for j in range(n):
			for k in range(2,n): # последовательно перебираем все тройки точек М1;
				if (not(i==j or i==k or j==k)):
					circle=CircleCreating(mass_of_data_about_point_M1[i],mass_of_data_about_point_M1[j],mass_of_data_about_point_M1[k]) # по трем точкам создаем окружность;
					t=0
					for p in range(n):
						if (circle.r==((mass_of_data_about_point_M1[p].x-circle.centre.x)**2+(mass_of_data_about_point_M1[p].y-circle.centre.y)**2)**(1/2)):
							t=t+1  #считаем количество точек, которые удовлетворяют уравнению найденной окружности;
					if (t==amount):
						if (AmountTest(circle,mass_of_data_about_point_M1,mass_of_data_about_point_M2,n)):# проверяем равенство количеств точек М1 и М2 в окружности,истенность или ложь;
							print("Радиус = ", circle.r, " O (x,y) = (", circle.centre.x, ", ", circle.centre.y, ")")
							#QtGui.QMessageBox.warning(root,'Radius of circle = ', circle.r, ' O (x,y) = (', circle.centre.x, ', ', circle.centre.y, ')')
							Rendering_solution()
							Itg=1
	if (not Itg):
		print("К сожалению по заданным параметрам построить окружность невозможно!")
		QtGui.QMessageBox.warning(root,'Решение','К сожалению по заданным параметрам построить окружность невозможно!')

def Rendering_solution():
	global mass_of_data_about_point_M1, mass_of_data_about_point_M2, circle, entry
	n=int(entry.text())
	centerX=400
	centreY=400
	root = Tk()
	canvas = Canvas(root, width=1200, height=900, borderwidth=0, bg="white")
	canvas.grid()

	def _create_circle(self, x, y, r, **kwargs):
		return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
	Canvas.create_circle = _create_circle

	canvas.create_circle(circle.centre.x+centerX, circle.centre.y+centreY, circle.r, outline="red", width=2)
	canvas.create_text(150,20,text='Радиус = '+str(circle.r)+' O (x,y) = ('+str(circle.centre.x)+', '+str(circle.centre.y)+')')
	
	for i in range (n):
		canvas.create_circle(mass_of_data_about_point_M1[i].x+centerX, mass_of_data_about_point_M1[i].y+centreY, 2, outline="green", width=4)
		canvas.create_circle(mass_of_data_about_point_M2[i].x+centerX, mass_of_data_about_point_M2[i].y+centreY, 2, outline="blue", width=4)
		
	root.wm_title("Решение")
	root.mainloop()
	
groupbox = QtGui.QGroupBox(root)
groupbox.hide()

button.clicked.connect(EnteringCoordinates)
solution_button.clicked.connect(Solution)

root.show()
sys.exit(app.exec())