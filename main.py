from data import db_session
from data.users import User

if __name__ == "__main__":
    db_session.global_init("db/mars_explorer.db")
    db_sess = db_session.create_session()
    captain = User(surname="Scott", name="Ridley", age=21, position="captain", speciality="research engineer",
                   address="module_1", email="scott_chief@mars.org")
    colonist1 = User(surname="Weir", name="Andy", age=25, position="pilot", speciality="spacecraft pilot",
                     address="module_1", email="andy_pilot@mars.org")
    colonist2 = User(surname="Bean", name="Sean", age=30, position="doctor", speciality="medical doctor",
                     address="module_1", email="sean_medic@mars.org")
    colonist3 = User(surname="Johnson", name="Lisa", age=27, position="scientist", speciality="geologist",
                     address="module_1", email="lisa_geology@mars.org")
    db_sess.add(captain)
    db_sess.add(colonist1)
    db_sess.add(colonist2)
    db_sess.add(colonist3)
    db_sess.commit()
