# pydantic without fastapi 

from pydantic import BaseModel, Field, EmailStr, ConfigDict

data = {
    "email": "wegfko@mail.ru",
    "bio": "ara",
    "age": 20
}
DataWoAge = {
    "bio": "dang",
    "age": 11,
    "email": "fdbj33@gmail.com",
    "gender": "Male",
    "date": "2020"
}


# class UserSchema(BaseModel):
#     email: str
#     bio: str | None
#     age: int 

# print(UserSchema(**data))

# как впринцапе сделать валидацию более сложной при помощи field

class UserSchema(BaseModel):
    bio: str | None = Field(max_length=10)
    age: int = Field(ge=0, le=130) # ge, le - это сокращения ge - greater or equal = , le - less or equal = 
    email: EmailStr 

    model_config = ConfigDict(extra="forbid")

# еще так же есть шикарная вещь в пайдентике это наследовательность моделей друг за другом например вот так 

class UserSchemaEmail(UserSchema):
    email: EmailStr
print(UserSchemaEmail(**data))


class UserSchemaWoAge(UserSchema):
    email: EmailStr
print(repr(UserSchema(**DataWoAge))) # тут мы просто валидируем данные через класс юзер схема и в скобках пишем что конкретно валидируем
print(repr(UserSchema(**data))) # ну тут тоже самое только валидируем в этот раз дату дефолтную

# если к нам приходят лишние данные то можно воспользоватся импортированным классом configdict что бы запретить лишние данные 
# что бы они к нам не приходили а если придут то пайдантик будет зажоватся типа че такое 
# Работает это по такому принципу если в схеме нету тех параметров которые есть в нашем словаре или джейсоне 
# Будет выдовать ошибку, в ином случае если все есть то будет все хорошо 
# изменения сделал на 30 строках, и как мы видим у нас ошибки со словами что нельзя 

