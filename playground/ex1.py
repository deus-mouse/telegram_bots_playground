
questions = ['assd', 'sds', 'dasd', 'asd']
answers = ['assd', 'sds', 'dasd', 'asd']

QNA = []
for i in range(len(questions)):
    qna = ': '.join([questions[i], answers[i]])
    QNA.append(qna)


print(f'{QNA=}')

result = '\n\n'.join(QNA)

print(f'{result=}')
