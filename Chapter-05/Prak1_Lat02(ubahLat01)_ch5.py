#Menentukan status kelulusan mahasiswa
bhsindo=int(input("Masukkan nilai Bhs Indonesia :"))
ipa=int(input("Masukkan nilai IPA           :"))
matematika=int(input("Masukkan nilai Matematika    :"))
print("")
if(bhsindo>=60)and(bhsindo<=100):
    if(ipa>=60)and(ipa<=100):
        if(matematika>70)and(ipa<=100):
            print("Status kelulusan             :Lulus")    
elif(bhsindo>=0)and(bhsindo<=59):
    print("Status kelulusan             :Tidak Lulus")
elif(ipa>=0)and(ipa<=59):
    print("Status kelulusan             :Tidak Lulus")
elif(matematika>=0)and(matematika<=70):
    print("Status kelulusan             :Tidak Lulus")    
else:
    print("Maaf input ada yang tidak valid")
