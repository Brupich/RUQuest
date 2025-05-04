from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QRadioButton, QGroupBox, QLabel, QButtonGroup
from random import shuffle, randint

class potomok(QWidget):
    def __init__ (self):
        super().__init__()
        self.score = 0
        self.total = 0

app = QApplication([])
main_win = potomok()
main_win.setWindowTitle('Memo Card')
main_win.resize(750, 500)

class Question():
    def __init__(self, right_answer, wrong_ans1, wrong_ans2, wrong_ans3, question):
        self.ra = right_answer
        self.wa1 = wrong_ans1
        self.wa2 = wrong_ans2
        self.wa3 = wrong_ans3
        self.que = question



q1 = Question('Смурфы', 'Энцы', 'Чулмыцы', 'Алеуты', 'Какой национальности не существует?')
q2 = Question('Зелёный', 'Красный', 'Синий', 'Белый', 'Какого цвета нет на флаге РФ?')
q3 = Question('988', '899', '989', '898', 'Когда было крещение Руси?')
q4 = Question('Швейцария', 'Швеция', 'Япония', 'Ничего из этого', 'Какая страна уже очень долго не вмешивается в происходящее в мире и является мемом?')
q5 = Question('Becouse 10+10=twenty and 11+11=twenty-two(too)', 'Незнаю', 'Потому что это неверно', '10-10=0 и 11-11=0, значит 10=11', 'Почему 10+10 = 11+11?')

Questions = [q1, q2, q3, q4, q5]
cur_question = randint(0, len(Questions) - 1)
q = Questions[cur_question]


question = QLabel('Какой национальности не существует?')
answer = QPushButton('Ответить')



RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чулымцы')
rbtn_4 = QRadioButton('Алеуты')
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)


AnsGroupBox = QGroupBox('Результаты теста')
Yes_or_No = QLabel('правильно/неправильно')
otvet = QLabel('абоба')
layout_otv = QVBoxLayout()
layout_otv.addWidget(Yes_or_No)
layout_otv.addWidget(otvet)

AnsGroupBox.setLayout(layout_otv)

AnsGroupBox.hide()

layout_main = QVBoxLayout()
layout_main.addWidget(question)
layout_main.addWidget(RadioGroupBox)
layout_main.addWidget(AnsGroupBox)
layout_main.addWidget(answer)
main_win.setLayout(layout_main)

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
shuffle(answers)

right_answer = 'Энцы'
wrong_ans1 = 'Смурфы'
wrong_ans2 = 'Чулмыцы'
wrong_ans3 = 'Алеуты'

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    answer.setText('Следующий вопрос')
    
def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    answer.setText('Ответить')
    RadioGroup.setExclusive(False) 
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.ra)
    answers[1].setText(q.wa1)
    answers[2].setText(q.wa2)
    answers[3].setText(q.wa3)
    question.setText(q.que)
    otvet.setText(q.ra)
    show_question()
    
def check_answer(): 
    if answers[0].isChecked():
        show_correct('Правильно')
        main_win.score += 1
    elif answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        show_correct('Неправильно')
def show_correct(Y_N):
    Yes_or_No.setText(Y_N)
    show_result()
def click_OK():
    if answer.text() == 'Ответить':
        check_answer()
    else:
        cur_question = randint(0, len(Questions) - 1)
        q = Questions[cur_question]
        ask(q)
        main_win.total += 1
        print('Статистика:', '\n-Всего вопросов: ', main_win.total, '\n-Правильных ответов:', main_win.score, '\nРейтинг:',  main_win.score/main_win.total*100)
ask(q)

answer.clicked.connect(click_OK)


main_win.show()
app.exec()