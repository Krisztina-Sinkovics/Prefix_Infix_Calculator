from flask import Flask, render_template, request
from wtforms import Form, StringField, validators
from prefix import evaluate_prefix_notation
from infix import evaluate_infix_notation

app = Flask(__name__)
app.debug = True


class Form1(Form):
    expr_prefix = StringField('expr_prefix', [validators.InputRequired()])


class Form2(Form):
    expr_infix = StringField('expr_infix', [validators.InputRequired()])


# View
@app.route('/', methods=['GET', 'POST'])
def index():
    form_prefix = Form1(request.form)
    form_infix = Form2(request.form)
    s_prefix = None
    s_infix = None
    if request.method == 'POST':
        if form_prefix.validate():
            r_prefix = form_prefix.expr_prefix.data
            s_prefix = evaluate_prefix_notation(r_prefix)

        elif form_infix.validate():
            r_infix = form_infix.expr_infix.data
            s_infix = evaluate_infix_notation(r_infix)

    return render_template("view.html", form1=form_prefix, form2=form_infix,
                           s_prefix=s_prefix, s_infix=s_infix)


if __name__ == '__main__':
    app.run(debug=True, port=7089)
