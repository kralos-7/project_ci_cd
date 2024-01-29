from database.db import db

class User(db.Model):
    __tablename__ = 'tbl_usuarios'
    fk_carrera = db.Column(db.Integer, primary_key=True)
    correo = db.Column(db.String(30))
    contrasenia = db.Column(db.String(20))

    def getUser(self, id):
        user = db.get_or_404(self, id)
        print("--------------------")
        print(user.correo)
        print("--------------------")

        return 0
    

    def insert_user(self):
        print("--------------")
        
        db.session.add(self)
        db.session.commit()
        return 0