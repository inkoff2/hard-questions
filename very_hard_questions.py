############################################################
#1.устанавливаем модули
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget,
        QHBoxLayout, QVBoxLayout,
        QGroupBox, QRadioButton,
        QPushButton, QLabel, QButtonGroup)
from random import shuffle
################################################################
#3.создаем класс question
class Question():
    def __init__ (self, question, right_answer, wrong1, wrong2, wrong3):
        #все строки надо задать при создании объекта, они запоминаются в свойства
        self.question =question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
#создание списка
question_list = []
#добавление в список элементов класса Question
question_list.append(Question('Государственный язык бразилии', 'Португальский', 'Бразильский', 'Испанский', 'Итальянский'))
question_list.append(Question('Какого цфета нет флаг России','зеленый','красный','белый','синий'))
question_list.append(Question('Национальная хижина якутов','ураса','','ирта','игла'))
#2.создание необходимых элементов(объектов)

app = QApplication([])

btn_OK = QPushButton('Ответить!')
lb_Question = QLabel('Самый сложный вопрос в мире!')

RadioGroupBox = QGroupBox('варианты ответов')

rbtn_1 = QRadioButton('вариант 1')
rbtn_2 = QRadioButton('вариант 2')
rbtn_3 = QRadioButton('вариант 3')
rbtn_4 = QRadioButton('вариант 4')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
##############################################
#3.расположение виджетов по линиям
layout_ans1 = QHBoxLayout()
layout_ans2 = QHBoxLayout()
layout_ans3 = QHBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

#создаем панель результата
AnsGroupBox = QGroupBox('Результат текста')
lb_Result = QLabel('прав ты или нет')
lb_Correct = QLabel('ответ будет тут!')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment =(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment =Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

#размещаем все виджеты в окне
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question, alignment=(Qt. AlignHCenter | Qt. AlignVCenter))

layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
RadioGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.addStretch(5)

##################################################
def show_result():
    '''показать панель ответов'''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')

def show_question():
    '''показать панель вопросов'''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q : Question):
    '''функция записывает значения вопроса и ответов в соответсвующие виджеты,
    при этом варианты ответов распределяются случайным образом'''
    shuffle(answers)#премешали список из кнопок, теперь на первом месте списка какая - то непредсказуемая кнопка
    answers[0].setText(q.right_answer)#первй элемент списка заполним правильным ответом, остальные - неверными
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)#вопрос
    lb_Correct.setText(q.right_answer)#ответ
    show_question()#показываем панель вопросов

def show_correct(res):
    '''показать результат - установим переданный текст в надпись "результат" и покажем нужную панель'''
    lb_Result.setText(res)
    show_result()

def check_answer():
    '''если выбран какой - то вариант ответа, то надо проверить и показать панель ответа'''
    if answers[0].isChecked():
        show_correct('правильно!')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('неверно!')
def next_question():
    '''задает следующий вопрос из списка'''
    #этой функции нужна переменная, в которой будет указыватся номер твоего вопроса
    #эту переменную можно сделать глобальной, либоже сделать свойством "глобального объекта" (app или windows)
    #мы заведем (ниже) свойство window.cur_question

    window.cur_question = window.cur_question + 1#переводим к следующему вопросу
    if window.cur_question >= len(question_list):
        window.cur_question = 0#если список вопросов закончился - идем сначала
    q = question_list[window.cur_question]#взяли вопрос
    ask(q)#спросили

def click_OK():
    '''определяет, надо ли показывать в друой вопрос либо проверить в ответ на этот'''
    if btn_OK.text() == 'Ответить':
        check_answer()#проверка ответа
    else:
        next_question()#следующий вопрос


######################################
window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')
#текущий вопрос из списка сделаем свойством объекта "окно", так мы сможем спокойно менять его из функции
window.cur_question = -1 #по хорошему такие перемещенные должны быть свойствами
#только надо писать класс, экземпляры которого получат такие свойства
#но питон не позволяет создать свойство у отдельно взятого экзепляра
btn_OK.clicked.connect(click_OK)#по нажатии на кнопку выбираем, что конкретно происходит
next_question
window.resize(400,300)
window.show()
app.exec()