from fastapi import FastAPI
import uvicorn
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
		episode_list.append({"id":episode[0], "diffusion_id":episode[1], "serie_id":episode[2], "scenarist_id":episode[3], "director_id":episode[4], "us_audience":episode[5], "fr_audience":episode[6], "epi_num":episode[7], "titre":episode[8]})
	return JSONResponse(episode_list)


@app.get("/scenarists")
async def get_all_scenarists():
	cursor.execute("""SELECT * FROM scenarists;""")
	scenarists = cursor.fetchall()
	scenarists_list = []
	for people in scenarists:
		scenarists_list.append(
			{"id": people[0], "name": people[1]})
	return JSONResponse(scenarists_list)


@app.get("/directors")
async def get_all_directors():
	cursor.execute("""SELECT * FROM directors;""")
	directors = cursor.fetchall()
	directors_list = []
	for people in directors:
		directors_list.append(
			{"id": people[0], "name": people[1]})
	return JSONResponse(directors_list)


@app.get("/series")
async def get_all_series():
	cursor.execute("""SELECT * FROM series;""")
	series = cursor.fetchall()
	series_list = []
	for serie in series:
		series_list.append(
			{"id": serie[0], "name": serie[1]})
	return JSONResponse(series_list)


@app.get("/diffusion_dates")
async def get_all_diffusion_dates():
	cursor.execute("""SELECT * FROM diffusion_dates;""")
	diffusion_dates = cursor.fetchall()
	diffusion_dates_list = []
	for date in diffusion_dates:
		diffusion_dates_list.append(
			{"id": date[0], "date": str(date[1])})
	return JSONResponse(diffusion_dates_list)


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
