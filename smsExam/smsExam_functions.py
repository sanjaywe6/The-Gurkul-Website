from smsExam.models import *


def validate_gta_questions(fname,lname,dob,email,father,mother,std_class,aadhar,mob,captcha_value,subject,institution, addr):
    lst=[]
    if len(fname)>0:
        if len(lname)>0:
            if len(dob)>0:
                if len(email)<50:
                    if len(father)>0:
                        if len(mother)>0:
                            if len(std_class)>0:
                                if len(aadhar)<15:
                                    if len(mob)>0:
                                        if len(captcha_value)>0:
                                            if len(subject)>0:
                                                if len(institution)>0:
                                                    if len(addr)>0:
                                                        verify_duplicate_data = studentRegistration.objects.filter(aadhar=aadhar)
                                                        if len(verify_duplicate_data)<1:
                                                            code=200
                                                            lst.append(code)
                                                            msg=""
                                                            lst.append(msg)
                                                        else:
                                                            code=300
                                                            lst.append(code)
                                                            msg="Student is already registered"
                                                            lst.append(msg)
                                                    else:
                                                        code=300
                                                        lst.append(code)
                                                        msg="Sorry! 'Address' field was empty..."
                                                        lst.append(msg)
                                                else:
                                                    code=300
                                                    lst.append(code)
                                                    msg="Sorry! 'Institution' field was empty..."
                                                    lst.append(msg)
                                            else:
                                                code=300
                                                lst.append(code)
                                                msg="Sorry! 'Subject' field was empty..."
                                                lst.append(msg)
                                        else:
                                            code=300
                                            lst.append(code)
                                            msg="Sorry! 'Captcha' field was empty..."
                                            lst.append(msg)
                                    else:
                                        code=300
                                        lst.append(code)
                                        msg="Sorry! 'Mobile Number' field was empty..."
                                        lst.append(msg)
                                else:
                                    code=300
                                    lst.append(code)
                                    msg="Sorry! 'Aadhar' number was wrong..."
                                    lst.append(msg)
                            else:
                                code=300
                                lst.append(code)
                                msg="Sorry! 'Student Class' field was empty..."
                                lst.append(msg)
                        else:
                            code=300
                            lst.append(code)
                            msg="Sorry! 'Mother Name' option was empty..."
                            lst.append(msg)
                    else:
                        code=300
                        lst.append(code)
                        msg="Sorry! 'Father Name' option was empty..."
                        lst.append(msg)
                else:
                    code=300
                    lst.append(code)
                    msg="Sorry! 'Email' option length was too big..."
                    lst.append(msg)
            else:
                code=300
                lst.append(code)
                msg="Sorry! 'Date of Birth' option was empty..."
                lst.append(msg)
        else:
            code=300
            lst.append(code)
            msg="Sorry! 'Last Name' option was empty..."
            lst.append(msg)
    else:
        code=300
        lst.append(code)
        msg="Sorry! 'First Name' option was empty..."
        lst.append(msg)

    return lst


def submit_std_reg_form(fname,lname,dob,email,father,mother,std_class,aadhar,mob,wmob,subject,institution, addr, captcha_value, captcha_id,new_uin_num, img):

    # field for sending form status
    fields={}

    # validating form
    validate=validate_gta_questions(fname,lname,dob,email,father,mother,std_class,aadhar,mob,captcha_value,subject,institution, addr)

    if validate[0] == 300:
        fields["code"]=300
        fields["msg"]=validate[1]
    elif validate[0]==200:
        try:
            std_reg = studentRegistration(uin_no=f'GTASMS0{new_uin_num}', fname=fname, lname=lname, email=email, mob=mob, wmob=wmob, father_name=father, mother_name=mother, dob=dob, aadhar=aadhar, std_class=std_class, subject_class=subject, institution=institution, addr=addr, img=img)
            std_reg.save()
            fields["code"]=200
            fields["msg"]="Congratulations! Form submitted successfuly."
        except Exception:
            fields["code"]=300
            fields["msg"]="Failed! An error ocured. Please try again..."

    return fields
