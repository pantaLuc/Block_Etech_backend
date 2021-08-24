from rolepermissions.roles import AbstractUserRole

class Visitor(AbstractUserRole):
    available_permissions = {
        'consult_blog': True,     
    }

class User(Visitor):
    available_permissions=Visitor.available_permissions
    available_permissions.update({
        'signin_blog': True,
        'edit_profil':True,
        'read_article':True,
        'write_comment':True,
        'ask_to_become_writer':True
    })
class Writer(User):
    available_permissions=User.available_permissions
    available_permissions.update(
        {
         'write_article':True,
         'delete_article': True,
         'update_article':True 
        }
    )
    
class Admin(Writer):
    available_permissions=Writer.available_permissions
    available_permissions.update({
        'change_user_role':True,
        'delete_user':True,
        'publish_user_article':True
    })
