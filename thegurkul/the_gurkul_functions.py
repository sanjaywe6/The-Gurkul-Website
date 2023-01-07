from gurkul_admin.models import *


# function to fetch user ip addres
def get_client_ip_address(request):
    req_headers = request.META
    x_forwarded_for_value = req_headers.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for_value:
        ip_addr = x_forwarded_for_value.split(',')[-1].strip()
    else:
        ip_addr = req_headers.get('REMOTE_ADDR')
    return ip_addr

# fuction to verify captcha
def captcha_verification(id,value):
    status="False"
    get_captcha=captcha_data.objects.filter(sno=id)
    if get_captcha[0].value==value:
        status="True"

    return status

# function to determine usertype
def gurkul_user_type(username):
    user_type='anon'
    general_user=all_usrs.objects.filter(username=username)
    super_user=gurkul_all_superuser.objects.filter(username=username)
    if len(general_user)>0:
        user_type=general_user[0].visitor_type
    elif len(super_user)>0:
        user_type=super_user[0].visitor_type

    return user_type




# function to generate captcha codes
# def generate_captcha_codes():

    # lst=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','0','1','2','3','4','5','6','7','8','9']
    # for item in lst:
    #     for val in lst:
    #         result=f"{val}{item}"
    #         captcha=captcha_data(first_character=val,second_character=item,value=result)
    #         captcha.save()
    # pass
