from firebase import firebase
firebase = firebase.FirebaseApplication(
    "https://python-firebase-demo01-default-rtdb.asia-southeast1.firebasedatabase.app/",None

)
mydata = {
    'fname' : 'RamBas',
    'lname' : 'BBAS',
    'email' : 'Kridtirat@mitsubishifa.co.th',
    'phone' : '0654641989'
}
#Insert Data
# result = firebase.post('/data1/customer',mydata)
# print(result)

#Get data
# result = firebase.get('/data1/customer','')
# # print(result['-MtvjWTBXAvQdOTNeg28']['email'])
# for data in result['-MtvjWTBXAvQdOTNeg28']:
#     print(data)

#Update data
# firebase.put('/data1/customer/-MtvjWTBXAvQdOTNeg28',
# 'email','rambas@gmail.com'
# )
# print('record updated')

#Delete data
# firebase.delete('/data1/customer/-MtvjWTBXAvQdOTNeg28','' # use '' for delete all document
# # 'email','rambas@gmail.com' #delete email only
# )

firebase.delete('/data1/customer/','-MtvlytKauygG8WgeEcN')
print('record deleted')
