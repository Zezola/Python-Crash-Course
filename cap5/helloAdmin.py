current_users = ['luiz','candido','pedro']

new_users = ['fatima', 'carlos', 'lucas','bruna']

''' Verificar se os usuarios novos sao unicos ''' 
registered = False

for new_user in new_users:
   for c_user in current_users: 
      if( new_user.lower() == c_user.lower()):
         registered = True
      else:
         registered = False
   if(registered == False):
      current_users.append(new_user)

for c_user in current_users:
   print("Welcome "+ c_user)
