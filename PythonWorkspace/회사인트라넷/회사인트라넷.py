from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "your_secret_key"  # 세션에 사용할 비밀 키
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# 데이터베이스 모델
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

# 데이터베이스 초기화
with app.app_context():
    db.create_all()

# 로그인 페이지
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            session["user_id"] = user.id
            flash("로그인 성공!", "success")
            return redirect(url_for("dashboard"))
        
        flash("로그인 실패: 올바른 ID와 PW를 입력하세요.", "danger")
    return render_template("login.html")

# 회원가입 페이지
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # 사용자 중복 확인
        if User.query.filter_by(username=username).first():
            flash("이미 사용 중인 사용자 ID입니다.", "warning")
            return render_template("register.html")

        # 비밀번호 해시화 후 저장
        # hashed_password = generate_password_hash(password, method="sha256")
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        # new_user = User(username=username, password=hashed_password)
        new_user = User(username=username, password=generate_password_hash(password))

        db.session.add(new_user)
        db.session.commit()

        flash("회원가입이 완료되었습니다. 로그인 해주세요.", "success")
        return redirect(url_for("login"))
    
    return render_template("register.html")

# 대시보드 페이지
@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect(url_for("login"))
    return "로그인 성공! 대시보드 페이지입니다."

# 로그아웃
@app.route("/logout")
def logout():
    session.pop("user_id", None)
    flash("로그아웃 되었습니다.", "info")
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
