from bottle import route, run, template

from solveHelp import solve

from bottle import get, post, request # or route
lowercase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
@get('/letters') # or @route('/login')
def login():
    return '''
        <h1> Enter the Letters you know </h1>
        <form action="/possibilities" method="post">
            Letter 1: <input name="letter1" type="text" />
            Letter 2: <input name="letter2" type="text" />
            Letter 3: <input name="letter3" type="text" />
            Letter 4: <input name="letter4" type="text" />
            Letter 5: <input name="letter5" type="text" />
            <input value="Submit" type="submit" />
        </form>
    '''

@post('/possibilities') # or @route('/login', method='POST')
def do_login():
    letters = [[request.forms.get('letter1').lower(),1],
    [request.forms.get('letter2').lower(),2],
    [request.forms.get('letter3').lower(),3],
    [request.forms.get('letter4').lower(),4],
    [request.forms.get('letter5').lower(),5]]
    letter = []

    for i in letters:
        if lowercase.count(i[0]) > 0:
            letter.append(i)
            print(i)

    print(letter)
    return(str(solve(letter)))

run(host='10.1.68.19', port=8080)
