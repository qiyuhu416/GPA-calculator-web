"""
  website_demo shows how to use templates to generate HTML
  from data selected/generated from user-supplied information
"""

from flask import Flask, render_template, request
app = Flask(__name__)



@app.route('/')
@app.route('/main')
def main():
    """ this returns a simple HTML page when the user visits / or /main """
    return render_template("mainbootstrap.html")


@app.route('/calculate',methods=['GET','POST'])
def calculate_grade():
    """ this shows how to use HTML forms to send data (x) to the server """
    page1 = """
    <form method="post" action="calculate">
      Participation Grade <input type="text" name="participation" placeholder="enter your grade"><br>

      Homework Grade <input type="text" name="homework" placeholder="enter your grade"><br>

      Quiz 1 Grade <input type="text" name="quiz1" placeholder="enter your grade"><br>
      Quiz 2 Grade <input type="text" name="quiz2" placeholder="enter your grade"><br>
      Quiz 3 Grade <input type="text" name="quiz3" placeholder="enter your grade"><br>
      Quiz 4 Grade <input type="text" name="quiz4" placeholder="enter your grade"><br>

      Project Grade <input type="text" name="project" placeholder="enter your grade"><br>

      <input type="submit">
      </form>
    """

    if request.method == 'POST':
        a = int(request.form['participation'])
        b = int(request.form['homework'])
        c = int(request.form['quiz1'])
        d = int(request.form['quiz2'])
        e = int(request.form['quiz3'])
        f = int(request.form['quiz4'])
        g = int(request.form['project'])
        grades=[c,d,e,f]
        pro_grade = progressive_grade(grades)
        final_quizG = final_quiz(pro_grade)

        total = a*0.1+b*0.3+final_quizG*0.4+g*0.2
        return "Your grade for this class is "+str(total)+"%"+"<hr>"+page1
    else:
        return page1;

def progressive_grade(gs):
    pgrades=[]
    for i in range(len(gs)):
        pgrades.append(max(gs[i:]))
    return pgrades

def final_quiz(grade):
    sum = 0
    for i in range(len(grade)):
        sum = sum + grade[i]
    final = sum/4
    return final



@app.route('/advice',methods=['GET','POST'])
def advice():
    page2 = """

    <h2> Some things to help with your performance</h2>
      <ul type = "disc">
        <li> "Read the textbook"</li>
        <li> "Do your homework"</li>
        <li> "Ask questions to your TA's, teachers and peers" </li>
        <li> "Quiz yourself"</li>
      </ul>
    """
    return page2

if __name__ == '__main__':
    app.run('0.0.0.0',port=5000)
