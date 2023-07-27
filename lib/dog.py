from models import Dog

def create_table(base, engine):
    base.metadata.create_all(bind=engine)

def save(session, dog):
    session.add(dog)
    session.commit()

def get_all(session):
    return session.query(Dog).all()


def find_by_name(session, name):
    dog = session.query(Dog).filter_by(name=name).first()
    return dog

def find_by_id(session, id):
    dog = session.query(Dog).filter_by(id=id).first()
    return dog 

def find_by_name_and_breed(session, name, breed):
    dog = session.query(Dog).filter(Dog.name == name, Dog.breed == breed).first()
    return dog 

def update_breed(session, dog, breed):
    dog = session.query(Dog).filter_by(id=dog.id).first()
    dog.breed = breed
    session.commit()