from gurkul_student.models import *



# function to return profile data existance
def profile_data_existance(student_id):
    profile_data=student_profile_data.objects.filter(student_id=student_id)
    if len(profile_data)>0:
        profile_data_existence="True"

    else:
        profile_data_existence="False"
    return profile_data_existence

#  function to return profile data old or new
def edit_profile_status(student_id):
    profile_data=student_profile_data.objects.filter(student_id=student_id)
    if len(profile_data)>0:
        edit_profile_status='old'
    else:
        edit_profile_status='new'
    
    return edit_profile_status

# function to know educational_data_existence
def educational_data_existence(student_id):
    educational_data=student_educational_profile_data.objects.filter(student_id=student_id).all()
    if len(educational_data)>0:
        educational_data_existence='True'
    else:
        educational_data_existence='False'
        
    return educational_data_existence

# function to return empty slot of data field
def data_field_empty_slot(student_id):
    profile=student_educational_profile_data.objects.filter(student_id=student_id).all()

    empty_slots=[1,2,3,4,5]
    for item in profile:
        empty_slots.remove(item.data_field)

    return empty_slots