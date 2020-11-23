info = {
    'CS101': {
        'Room': 3004, 
        'Instructor': 'Haynes', 
        'Time': '8:00 a.m.' 
        },
    'CS103': {
        'Room': 4501,
        'Instructor': 'Alvarado',
        'Time': '9:00 a.m.'
        },
    'CS103': {
        'Room': 6755,
        'Instructor': 'Rich', 
        'Time': '10:00 a.m.'
        },
    'CS103': {
        'Room': 1244, 
        'Instructor': 'Burke', 
        'Time': '11:00 a.m.'
        },
    'CS103': {
        'Room': 1411, 
        'Instructor': 'Lee', 
        'Time': '1:00 a.m.'
        }
}

q = str(input('Enter a course number: '))
if q in info.keys():
    print(f'{q} query successfull')
    for item in info[q].items():
        print(f'{item[0]}: {item[1]}')
        