#import Main_App.Input_Pack.user_inputs as u
               #OR
from Main_App.Input_Pack import user_inputs as u
from Main_App.Operations_Pack import fetch_records as d
from Main_App.Operations_Pack import fetch_branch as fb
from Main_App.Operations_Pack import update_name as un
while True:
    print("--------------MENU------------------")
    print('''
    1. Enter Participants details
    2. Fetch Participants details
    3. Fetch Participants based on branch
    4. Update wrongly enterd name change
    5. exit
    ''')
    print("Choose any option ")
    ch=int(input())
    if ch==1:
        u.input_data()
    elif ch== 2:
        d.display()
    elif ch == 3:
        input_branch=input("Enter Branch ")
        fb.fetch_based_branch(input_branch)
    elif ch == 4:
        id=input("Enter g_id")
        name=input("enter name")
        un.updName(name,int(id))
    else:
        break
