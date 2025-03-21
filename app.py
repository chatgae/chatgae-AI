from flask import Flask, request, jsonify, render_template
from flask_migrate import Migrate

migrate=Migrate()

app = Flask(__name__)

#flask 애플리케이션 팩토링 -> app 전역변수 지양
def create_app():
    app = Flask(__name__)

    # blueprint 객체 등록
    from views import nose_views
    app.register_blueprint(nose_views.bp)
    

    @app.route('/' ,methods=['GET', 'POST'])
    def connect_with_android():
        return "Flask Server & Android are Working Successfully"
    return app


#중복없이 reg_num 생성
alist=[]

app = create_app()

if __name__ == "__main__":
    # app.config['TRAP_HTTP_EXCEPTIONS']=True
    # app.register_error_handler(Exception,serverErrorHandler)
    app.run(host='0.0.0.0', port = 8000 , debug=True)