from fastapi import FastAPI
import uvicorn
from bson.objectid import ObjectId
from typing import List, Optional
import psycopg2
from fastapi.responses import JSONResponse


app = FastAPI()

conn = psycopg2.connect(dbname="d4cd6ggafr9d27", host="ec2-52-48-65-240.eu-west-1.compute.amazonaws.com", user="adytqcrkolageu", password="97a16fa1a6d9bf1cbe925bcfe86d53fbac12d2a8acec3dcb4f88860a9c14a3cb")
cursor = conn.cursor()


@app.get("/")
async def root():
	return {"message": "Welcome to the Stargate API"}


@app.get("/episodes")
async def get_all_episodes():
	cursor.execute("""SELECT * FROM episodes;""")
	episodes = cursor.fetchall()
	episode_list = []
	for episode in episodes:
		episode_list.append({"id":episode[0], "serie":episode[1], "title":episode[2], "epi_num":episode[3]})
	return JSONResponse(episode_list)


@app.get("/staff")
async def get_all_staff():
	cursor.execute("""SELECT * FROM staff;""")
	staff = cursor.fetchall()
	staff_list = []
	for people in staff:
		staff_list.append({"id":people[0], "epi_id":people[1], "realisateur":people[2], "scenariste":people[3]})
	return JSONResponse(staff_list)

# @app.get("/audiences")
# async def get_all_audiences():
#   audiences = AUDIENCES_SG.find()
#   audience_list = []
#   for audience in audiences :
#     audience["_id"] = str(audience["_id"])
#     audience_list.append(audience)
#   return audience_list


# @app.get("/students/id/{student_id}")
# async def get_student_by_id(student_id):
# # SELECT * FROM STUDENTS WHERE id = student_id
# 	student = COLLECTION_STUDENTS.find_one({"_id" : ObjectId(student_id)})
# 	if student :
# 		student["_id"] = str(student["_id"])
# 		return student
# 	else :
# 		return f"Student with id = {student_id} not exist"


# @app.get("/students/name/{lastname}")
# async def get_student_by_name(lastname):
# 	student = COLLECTION_STUDENTS.find_one({"name" : lastname})
# 	if student :
# 		student["_id"] = str(student["_id"])
# 		return student
# 	else :
# 		return f"No student named {lastname}"


# @app.post("/students")
# async def create_student(student: Student):
# 	student_id = str(COLLECTION_STUDENTS.insert_one(student.dict()).inserted_id)
# 	# TODO : Envoyer un mail de confirmation
# 	return {"student_id": student_id}


# @app.post("/students/bulk")
# async def insert_many_students(students: List[Student]):
#   students_list = []
#   for s in students :
#     students_list.append(s.dict())
#   students_ids = COLLECTION_STUDENTS.insert_many(students_list).inserted_ids
#   list_ids = []
#   for student_id in students_ids :
#     list_ids.append(str(student_id))
#   return list_ids


# @app.put("/students/id/{id}")
# async def update_student(id, student: Student):
#   COLLECTION_STUDENTS.find_one_and_replace({"_id" : ObjectId(id)}, student.dict())
#   student = COLLECTION_STUDENTS.find_one({"_id" : ObjectId(id)})
#   student["_id"] = str(student["_id"])
#   return student


# @app.delete("/students/id/{id}")
# async def delete_student_by_id(id):
# 	student = COLLECTION_STUDENTS.find_one({"_id" : ObjectId(id)})
# 	if student :
# 		COLLECTION_STUDENTS.find_one_and_delete({"_id" : ObjectId(id)})
# 		return f"Student {student['name']} has been deleted"
# 	else :
# 		return "Please enter a valid id"


# @app.delete("/students/name/{lastname}")
# async def delete_student_by_name(lastname):
#   return {"lastname": lastname}


if __name__ == "__main__":
	uvicorn.run(app, host="0.0.0.0", port=8000)
