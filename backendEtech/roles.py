from rolepermissions.roles import AbstractUserRole

class Visitors(AbstractUserRole):
    available_permissions = {
        'create_medical_record': True,
    }

class Users(AbstractUserRole):
    available_permissions = {
        'edit_patient_file': True,
    }
class Writers(AbstractUserRole):
    available_permissions = {
        'edit_patient_file': True,
    }