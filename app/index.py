from flask import Flask, render_template
import dao
app = Flask(__name__)


@app.route("/")
def index():
    loais = dao.loai()
    sanphams = dao.sanpham()
    return render_template('index.html',loai=loais,sanpham=sanphams)


if __name__ == "__main__":
    app.run(debug=True)
