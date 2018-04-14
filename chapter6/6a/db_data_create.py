#encoding:utf8


from db_config import db
from db_config import Role,User


db.drop_all()  
db.create_all() 


admin_role = Role(name='Admin')
mod_role = Role(name='Moderator')
user_role = Role(name='User')


user_john = User(username='john', role=admin_role)
user_susan = User(username='susan', role=user_role)
user_david = User(username='david', role=user_role)
user_david = User(username='zeping', role=user_role)



if __name__ == '__main__':


    db.session.add(admin_role)
    db.session.add(mod_role)
    db.session.add(user_john)
    db.session.add(user_susan)
    db.session.add(user_david)

    db.session.commit()


    admin_role.name = 'Administrator'  
    db.session.add(admin_role)         
    db.session.commit()                
  
    db.session.delete(mod_role)
    db.session.commit()
             
    user_role = Role.query.filter_by(name='User').first()
    users = user_role.users  
              
              
        
