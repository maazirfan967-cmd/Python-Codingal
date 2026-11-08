Student_Data = {"ID1":{"Name:":"Maaz","Grade:":6,"Subject:":"English,Maths,Science"},
              
              "ID2":{"Name:":"Abdullah","Grade:":6,"Subject:":"English,Maths,Science"},
              
              "ID3":{"Name:":"Ayaan","Grade:":6,"Subject:":"English,Maths,Science"}
              }

print(f"Original Student Data:{Student_Data}")

print()
print(f"ID1:{Student_Data.get("ID1","Not Found")}")
print()
print(f"ID5:{Student_Data.get("ID5","Not Found")}")

Student_Data["ID5"] = {"Name:": "Aahil", "Grade:": 6, "Subject:": "Science,Arabic,PE"}
print()
print(f"After adding ID5:{Student_Data}")

Student_Data["ID2"]["Subject"] = "English,Maths,SST"
print(f"Updated ID2:{Student_Data['ID2']}")

Cleaned_Data = {}
seen_records = []

for i,j in Student_Data.items():
    unique=(j["Name:"],j["Grade:"],j["Subject:"])
    if unique not in seen_records:
            seen_records.append(unique)
            Cleaned_Data[i]=j

Student_Data.pop("ID4","Not Found")
print(f"Number of ID's:{len(Student_Data)}")

for i,j in Student_Data.items():
      print(i,j)