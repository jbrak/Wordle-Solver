from bottle import route, run, template

from solveHelp import solve

from bottle import get, post, request # or route

@get('/letters') # or @route('/login')
def login():
    return '''
        <h1> Enter the Letters you know </h1>
        <form action="/possibilities" method="post">
            Letter 1: <input name="letter1" type="text" /> <br>
            Letter 2: <input name="letter2" type="text" /> <br>
            Letter 3: <input name="letter3" type="text" /> <br>
            Letter 4: <input name="letter4" type="text" /> <br>
            Letter 5: <input name="letter5" type="text" /> <br>
            <input value="Submit" type="submit" />
        </form>
    '''

@post('/possibilities') # or @route('/login', method='POST')
def do_login():
    letters = [[request.forms.get('letter1'),1],
    [request.forms.get('letter2'),2],
    [request.forms.get('letter3'),3],
    [request.forms.get('letter4'),4],
    [request.forms.get('letter5'),5]]

    for i in letters:
        if i[0] == "":
            letters.remove(i)

    print(letters)
    return(str(solve(letters)))

run(host='localhost', port=8080)
